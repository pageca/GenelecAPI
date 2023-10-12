# Genelec Smart IP API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Device Discovery](#device-discovery)
- [API Protocol](#api-protocol)
- [Smart IP API for Genelec Devices (v1)](#smart-ip-api-for-genelec-devices-v1)

---

## Introduction

This document specifies how Genelec Smart IP devices can be controlled through the public API contained in the Smart IP loudspeaker products.

### Definitions, Acronyms, and Abbreviations

- **JSON:** JavaScript Object Notation
- **DNS-SD:** DNS Service Discovery
- **HTTP:** Hypertext Transfer Protocol
- **MAC Address:** Media Access Control Address
- **mDNS:** Multicast DNS
- **OUI:** Organizationally Unique Identifier
- **REST:** Representational State Transfer
- **URI:** Uniform Resource Identifier

---

## Device Discovery

### Device MAC Address

Generally, the manufacturer of the device can be identified by checking the first three bytes of the MAC address. These bytes form a 24-bit OUI number that identifies the vendor, manufacturer, or organization. OUI number `AC-47-23` is registered for Genelec Oy.

### mDNS Query

Devices can be found by using mDNS protocol, which resolves hostnames to IP addresses within small networks that do not include a local name server. Genelec devices automatically send the mDNS standard query response after booting.

### Ping

The device can be pinged using the following commands:

- `ping 192.168.0.79`
- `ping 4430-00-01-22`

---

## API Protocol

### Communication Format

The Smart IP devices use REST-style communication with a reduced set of HTTP/1.1 protocol. Only the HTTP methods `GET` and `PUT` are implemented, and the URI can't contain a query.

### Request Message

The request message consists of a header and an optional message body.

#### Header

The header starts with the request line having the format:

method /public/<version>/path HTTP/1.1\r\n


Then, the list of request header fields follows (Table 2) and finally an empty line.

#### Body

The `PUT` message always has a message body, but the `GET` message usually does not need a body.

#### Supported Header Fields

| Field Name      | Field Value                     |
|-----------------|---------------------------------|
| Accept          | application/json                |
| Connection      | keep-alive (Keep connection open) or close (Close connection) |
| Authorization   | Basic                           |
| Content-Length  | The length of the request body  |
| Host            | The domain name of the server   |

---

## Smart IP API for Genelec Devices (v1)

The API version can be read by sending a request to `GET {ip}:{port}/device/info`. The device will not respond to all commands during `ISS_SLEEP` and `STANDBY` states.

**Notice!** Do not use the Smart IP API at the same time with Smart IP Manager software.

- `ip: required (string)` IP address (e.g., 192.168.0.79).
- `port: required (string)` IP port number (default 9000).
- `versionstring: required (string)` API version string, e.g., v1.

### /audio

#### Get List of Selected Inputs

- **URL:** `http://{ip}:{port}/public/v1/audio/inputs`
- **Method:** `GET`
- **Media Type:** `application/json`

**Properties:**
- `input: required (array of )`
  - A: analog input connector
  - AoIP01: AoIP input channel 1
  - AoIP02: AoIP input channel 2

#### Select Inputs

- **URL:** `http://{ip}:{port}/public/v1/audio/inputs`
- **Method:** `PUT`
- **Media Type:** `application/json`

**Properties:**
- `input: required (array of )`
  - A: analog input connector
  - AoIP01: AoIP input channel 1
  - AoIP02: AoIP input channel 2

#### Set Loudspeaker Level and Mute

- **URL:** `http://{ip}:{port}/public/v1/audio/volume`
- **Method:** `PUT`
- **Media Type:** `application/json`

**Properties:**
- `level: (number - minimum: -200 - maximum: 0)` Volume level in 0.1 dB resolution.
- `mute: (boolean)` Mute audio

#### Get Loudspeaker Level and Mute State

- **URL:** `http://{ip}:{port}/public/v1/audio/volume`
- **Method:** `GET`
- **Media Type:** `application/json`

**Properties:**
- `level: (number - minimum: -200 - maximum: 0)` Volume level in 0.1 dB resolution.
- `mute: (boolean)` Mute audio

### /device

#### Get Device Information

- **URL:** `http://{ip}:{port}/public/v1/device/id`
- **Method:** `GET`
- **Media Type:** `application/json`

**Properties:**
- `barcode: required (string - minLength: 7 - maxLength: 20)` Bar code value. Defined during production.
- `mac: required (string - maxLength: 17)` MAC address. Defined during production.
- `hwId: required (string - maxLength: 32)` Hardware version number.
- `model: required (string - maxLength: 32)` Device model name.
- `modId: required (string - maxLength: 32)` Model specific configuration.

#### Get API Version, Model Name, and Version Information

- **URL:** `http://{ip}:{port}/public/v1/device/info`
- **Method:** `GET`
- **Media Type:** `application/json`

**Properties:**
- `fwId: (string)` Firmware identification number.
- `build: (string)` Committed GIT revision number.
- `baseId: (string)` Platform software version number.
- `hwId: (string)` Hardware version string.
- `model: (string)` Device model name.
- `category: (string)` SAM_1W, SAM_2W, SAM_3W, MICR.
- `technology: (string)` SAM_IP
- `upgradeId: (integer)` Compatibility information for upgrading firmware.
- `apiVer: (string)` API version.
- `confirmFwUpdate: (boolean)` New firmware is running and waiting for confirmation from the user.

#### Switch Between Sleep and Active State

- **URL:** `http://{ip}:{port}/public/v1/device/pwr`
- **Method:** `PUT`
- **Media Type:** `application/json`

**Properties:**
- `state: (one of STANDBY, ACTIVE, BOOT, AOIPBOOT)`

#### Get Power State

- **URL:** `http://{ip}:{port}/public/v1/device/pwr`
- **Method:** `GET`

