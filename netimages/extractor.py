from scapy.all import load_layer
from scapy.layers.http import HTTP, HTTPResponse

load_layer("http")


def extract_http_images(packets):
    for packet in packets:
        if packet.haslayer(HTTPResponse):
            p = packet[HTTP]
            if p.Content_Type and b"image" in p.Content_Type:
                yield packet.load, p.Location
