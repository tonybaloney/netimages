import argparse

from scapy.all import sniff, TCPSession

from netimages.extractor import extract_http_images
from netimages.render import render
from netimages import __doc__ as description

DEFAULT_FILTER = "tcp port 80"


def main():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('pcap', type=str, nargs='?',
                        help='Path to a pcap file')
    parser.add_argument('-i', '--iface', action='store', help='Interface to capture', default="any")
    parser.add_argument('-f', '--filter', action='store', help='BPF filter string', default=DEFAULT_FILTER)
    parser.add_argument('--no-colors', dest='colors', action='store_false', help='No ANSI colorings')

    args = parser.parse_args()

    def show_images(packets):
        for img, name in extract_http_images(packets):
            try:
                print(render(img, colorize=args.colors))
                print('\n')
            except Exception as ex:
                print("Bad image", ex)

    if not args.pcap:
        print("Capturing directly from network on interface {0}".format(args.iface))
        print("Press CTRL+C to stop capturing")
        sniff(filter=args.filter, iface=args.iface, session=TCPSession, prn=lambda pkt: show_images([pkt]), store=False)

    else:
        print("Replaying from pcap file {0}".format(args.pcap))
        capture = sniff(offline=args.pcap, session=TCPSession)
        try:
            show_images(capture)
        except GeneratorExit:
            pass


if __name__ == "__main__":
    main()
