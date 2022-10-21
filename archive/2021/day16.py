from math import prod

with open('day16.txt') as file:
    data = ''.join(f"{bin(int(i, 16))[2:]:0>4}" for i in file.read())

versionTotal = 0


# OOP go brrrrrr
class Packet:
    versionTotal = 0
    
    def __init__(self, version, packetType, data):
        self.version = version
        Packet.versionTotal += version
        self.type = packetType
        self.data = data


# Literal packet (with set value)
class DataPacket(Packet):
    def evaluate(self) -> int:
        return self.data


# Operator packet (with subpackets)
class OperatorPacket(Packet):
    operations = [sum, prod, min, max, None, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]]
    
    def evaluate(self) -> int:
        subpackets = [packet.evaluate() for packet in self.data]
        operation = OperatorPacket.operations[self.type]
        return operation(subpackets)


def parse(packet: str, getEnd: bool = False) -> tuple[Packet, str] | Packet:
    """
    Parses packet from input and returns Packet object
    :param packet: Data to parse from
    :param getEnd: Whether to include remaining bits after the packet terminates
    :return: Packet object parsed from input
    """
    v = int(packet[:3], 2)  # Fetch packet version (Part 1)
    
    if (t := int(packet[3:6], 2)) == 4:  # Literal value
        data, i = '', 1
        while packet[(i := i + 5)] == "1":
            data += packet[i + 1: i + 5]
        data += packet[i + 1: i + 5]  # Include the bit padded with 0
        data, remaining = int(data, 2), packet[i + 5:]
        if getEnd:
            return DataPacket(v, t, data), remaining
        else:
            return DataPacket(v, t, data)
    
    else:  # Operation
        data = []
        
        if packet[6] == "0":  # Length type 0 (set length)
            subpackets = packet[22:22 + (bits := int(packet[7:22], 2))]
            while subpackets:
                subpacket, subpackets = parse(subpackets, True)
                data.append(subpacket)
            remaining = packet[22 + bits:]
        
        else:  # Length type 1 (set amount of packets)
            subpackets = packet[18:]
            for _ in range(int(packet[7:18], 2)):
                subpacket, subpackets = parse(subpackets, True)
                data.append(subpacket)
            remaining = subpackets
        
        if getEnd:
            return OperatorPacket(v, t, data), remaining
        else:
            return OperatorPacket(v, t, data)


packet = parse(data)
print(f'Part 1: {Packet.versionTotal}\nPart 2: {packet.evaluate()}')
