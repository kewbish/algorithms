with open("input.txt") as x:
    raw_numbers = list(x.read().strip())
    packet = "".join([f"{int(r, 16):04b}" for r in raw_numbers])

versions = 0


def parse_packet(packet):
    global versions
    version = int(packet[:3], 2)
    versions += version

    packet = packet[3:]
    type_id = int(packet[:3], 2)

    packet = packet[3:]
    if type_id == 4:
        literal = ""
        while True:
            bstart = packet[0]
            literal += packet[1:5]
            packet = packet[5:]
            if bstart == "0":
                break
        literal = int(literal, 2)
    elif packet[0] == "0":
        length_in_bits = int(packet[1:16], 2)
        packet = packet[16:]
        subpackets = packet[:length_in_bits]
        while subpackets:
            subpackets = parse_packet(subpackets)
        packet = packet[length_in_bits:]
    elif packet[0] == "1":
        num_sub_packets = int(packet[1:12], 2)
        packet = packet[12:]
        for _ in range(num_sub_packets):
            packet = parse_packet(packet)
    return packet


parse_packet(packet)
print(versions)
