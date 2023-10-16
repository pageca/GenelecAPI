#include <Bela.h>
#include <curl/curl.h>
#include <iostream>
#include <cstring>
#include <libraries/OscReceiver/OscReceiver.h>

OscReceiver oscReceiver;
int localPort = 7562;
const char* remoteIp = "192.168.178.56";

// Callback function to write response data
static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    size_t totalSize = size * nmemb;
    std::string* response = static_cast<std::string*>(userp);
    response->append(static_cast<char*>(contents), totalSize);
    return totalSize;
}

// OSC to API Wrapper
void on_receive(oscpkt::Message* msg, void*) {
    oscpkt::Message::<Arg>Reader arg(msg->arg());
    std::string url;
    std::string body_json;
    struct curl_slist* headers = NULL;

    if (msg->match("/put")) {
        if (arg.isStr()) {
            arg.popStr(url);
        }
        if (arg.isStr()) {
            arg.popStr(body_json);
        }
    } else if (msg->match("/get")) {
        if (arg.isStr()) {
            arg.popStr(url);
        }
    } else {
        std::cerr << "Unsupported path: " << msg->addressPattern() << std::endl;
        return;
    }

    CURL* curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        if (msg->match("/put")) {
            curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
            if (!body_json.empty()) {
                curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body_json.c_str());
                curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, body_json.c_str().size());
            }
        } else if (msg->match("/get")) {
            curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "GET");
        }

        std::string response;
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

        CURLcode res = curl_easy_perform(curl);

        if (res == CURLE_OK) {
            long response_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
            if (response_code == 200) {
                std::cout << "Request was successful." << std::endl;
            } else {
                std::cout << "Request failed with status code " << response_code << ": " << response << std::endl;
            }
        } else {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        }

        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }
}

bool setup(BelaContext *context, void *userData) {
    oscReceiver.setup(localPort, on_receive);
    curl_global_init(CURL_GLOBAL_ALL);
    return true;
}

void render(BelaContext *context, void *userData) {
}

void cleanup(BelaContext *context, void *userData) {
    curl_global_cleanup();
}
