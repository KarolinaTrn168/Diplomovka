import json
import pyshark
import time

networkInterface = 'enp0s3'
capture = pyshark.LiveCapture(interface=networkInterface)
print("listening on %s." % networkInterface)

for packet in capture.sniff_continuously(packet_count=10):
    try:
        localtime = time.asctime(time.localtime(time.time()))
        protocol = packet.transport_layer       # protocol type
        src_addr = packet.ip.src                # source address
        src_port = packet[protocol].srcport     # source port
        dst_addr = packet.ip.dst                # destination address
        dst_port = packet[protocol].dstport     # destination port

        # output packet info
        print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
    except AttributeError as e:
        # ignore packets other than TCP, UDP and IPv4
        pass