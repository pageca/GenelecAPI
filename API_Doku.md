# Genelec Smart IP API Documentation

This document specifies the API endpoints and requests for controlling Genelec Smart IP devices.

## API Endpoints

| Method | URL                                              | Headers                                                                                                            | Message Options                                      |
| ------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| GET    | `/audio/inputs`                                 | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| PUT    | `/audio/inputs`                                 | Content-Type: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=<br>Connection: keep-alive             | `{ "input": ["AoIP01", "AoIP02"] }`                  |
| PUT    | `/audio/volume`                                 | Content-Type: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=<br>Connection: keep-alive             | `{ "level": -5.2, "mute": false }`                  |
| GET    | `/audio/volume`                                 | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| GET    | `/device/id`                                    | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| GET    | `/device/info`                                  | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| PUT    | `/device/pwr`                                  | Content-Type: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=<br>Connection: keep-alive             | `{ "state": "STANDBY" }`                           |
| GET    | `/device/pwr`                                  | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| GET    | `/events`                                      | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| GET    | `/network/zone`                                | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| GET    | `/profile/list`                                | Accept: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=                                             | None (GET Request)                                   |
| PUT    | `/profile/restore`                             | Content-Type: application/json<br>Authorization: Basic YWRtaW46YWRtaW4=<br>Connection: keep-alive             | `{ "id": 1, "startup": false }`                    |

## Headers

- `Accept`: application/json
- `Authorization`: Basic YWRtaW46YWRtaW4=
- `Content-Type`: application/json
- `Connection`: keep-alive

Note: Make sure to replace the Authorization value with your actual credentials.

This table provides an overview of the API endpoints, required headers, and example message options for each request. Ensure you replace the placeholders with actual values and credentials when making requests to the Genelec Smart IP API.
