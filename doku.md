# Genelec Smart IP API Documentation

This document specifies the API endpoints and requests for controlling Genelec Smart IP devices.

## API Endpoints

| Method | URL                                              | Headers                                                                                                                                                                            | Message Options                                      | Description                                          |
| ------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| GET    | `http://device-ip:port/public/v1/audio/inputs`  | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Retrieve the list of selected inputs.                |
| PUT    | `http://device-ip:port/public/v1/audio/inputs`  | `{ "Content-Type": "application/json", "Content-Length": <length>, "Authorization": "Basic YWRtaW46YWRtaW4=", "Connection": "keep-alive" }`                                         | `{ "input": ["AoIP01", "AoIP02"] }`                  | Select inputs.                                      |
| PUT    | `http://device-ip:port/public/v1/audio/volume`  | `{ "Content-Type": "application/json", "Content-Length": <length>, "Authorization": "Basic YWRtaW46YWRtaW4=", "Connection": "keep-alive" }`                                         | `{ "level": -5.2, "mute": false }`                  | Set loudspeaker level and mute.                     |
| GET    | `http://device-ip:port/public/v1/audio/volume`  | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Get loudspeaker level and mute state.               |
| GET    | `http://device-ip:port/public/v1/device/id`     | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Retrieve device information.                        |
| GET    | `http://device-ip:port/public/v1/device/info`   | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Retrieve API version, model name, and version info. |
| PUT    | `http://device-ip:port/public/v1/device/pwr`    | `{ "Content-Type": "application/json", "Content-Length": <length>, "Authorization": "Basic YWRtaW46YWRtaW4=", "Connection": "keep-alive" }`                                     | `{ "state": "STANDBY" }`                           | Switch between sleep and active state.               |
| GET    | `http://device-ip:port/public/v1/device/pwr`    | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Get the power state.                                 |
| GET    | `http://device-ip:port/public/v1/events`        | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Read measurement data.                               |
| GET    | `http://device-ip:port/public/v1/network/zone`  | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Get zone info.                                      |
| GET    | `http://device-ip:port/public/v1/profile/list`  | `{ "Accept": "application/json", "Authorization": "Basic YWRtaW46YWRtaW4=" }`                                                                                                     | None (GET Request)                                   | Get the list of profiles.                           |
| PUT    | `http://device-ip:port/public/v1/profile/restore` | `{ "Content-Type": "application/json", "Content-Length": <length>, "Authorization": "Basic YWRtaW46YWRtaW4=", "Connection": "keep-alive" }` | `{ "id": 1, "startup": false }`                    | Restore a profile from flash and set it as active.  |

## Headers

Headers should be sent as JSON key-value pairs.

```json
{
  "Accept": "application/json",
  "Authorization": "Basic YWRtaW46YWRtaW4=",
  "Content-Type": "application/json",
  "Content-Length": "0"
  "Connection": "keep-alive"
}
```


In the table, I've included headers in JSON format, provided complete URLs, and added examples for PUT and GET requests. Make sure to replace `http://device-ip:port/public/v1/` with the actual IP address and port of your Genelec device and set the orrect API version (v1 or v2)

