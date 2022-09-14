"""
Basic listener to read the UDP packet and convert it to a known packet format.
"""

import platform
import socket
from packets import PacketHeader
from packets import HEADER_FIELD_TO_PACKET_TYPE

def resolve(packet):
    header = PacketHeader.from_buffer_copy(packet)
    key = (header.packet_format, header.packet_version, header.packet_id)
    return HEADER_FIELD_TO_PACKET_TYPE[key].unpack(packet)



class PacketListener:
    def __init__(self, host: str = "", port: int = 20777):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        if platform.system() == "Windows":
            self.socket.settimeout(0.5)
        self.socket.bind((host, port))

    def get(self):
        while True:
            try:
                return resolve(self.socket.recv(2048))
            except socket.timeout:
                pass

    def __iter__(self):
        while True:
            yield self.get()
