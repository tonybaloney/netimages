NetImages - tool for sniffing images over HTTP traffic and showing them on the console.
Designed for remote shells.

Uses an 8-bit greyscale for relaying over telnet, file pipes, etc.

Uses ANSI 256 color codes for relaying on a color-supported shell (e.g. Xterm)

Supports either a recorded PCAP file (from Wireshark or similar), or listening to traffic on a specified interface.

## Installation

Install via PyPi using python pip:

```console
 $ python3 -m pip install netimages
```

## Usage

```console
usage: netimages [-h] [-i IFACE] [-f FILTER] [--no-colors] [pcap]

NetImages - tool for sniffing images over HTTP traffic and showing them on the console. Designed for remote shells

positional arguments:
  pcap                  Path to a pcap file

optional arguments:
  -h, --help            show this help message and exit
  -i IFACE, --iface IFACE
                        Interface to capture
  -f FILTER, --filter FILTER
                        BPF filter string
  --no-colors           No ANSI colorings

```

## Screenshot

![screenshot](screenshot.png)

## Handling TLS (HTTPS)

To capture and decrypt TLS packets, use [Wireshark TLS decrypytion](https://wiki.wireshark.org/TLS).
