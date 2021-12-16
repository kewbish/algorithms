from functools import reduce

with open("input.txt") as x:
    raw_numbers = list(x.read().strip())
    packet = "".join([f"{int(r, 16):04b}" for r in raw_numbers])

# is this what the cool eopl kids are doing


def parse_packet(packet):
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
        return [packet, literal]
    else:
        sub_values = []
        if packet[0] == "0":
            length_in_bits = int(packet[1:16], 2)
            packet = packet[16:]
            subpackets = packet[:length_in_bits]
            while subpackets:
                new_subs, value = parse_packet(subpackets)
                subpackets = new_subs
                sub_values.append(value)
            packet = packet[length_in_bits:]
        elif packet[0] == "1":
            num_sub_packets = int(packet[1:12], 2)
            packet = packet[12:]
            for _ in range(num_sub_packets):
                new_subs, value = parse_packet(packet)
                packet = new_subs
                sub_values.append(value)
        if type_id == 0:
            return [packet, sum(sub_values)]
        elif type_id == 1:
            return [packet, reduce(lambda x, y: x * y, sub_values)]
        elif type_id == 2:
            return [packet, min(sub_values)]
        elif type_id == 3:
            return [packet, max(sub_values)]
        elif type_id == 5:
            return [packet, 1 if sub_values[0] > sub_values[1] else 0]
        elif type_id == 6:
            return [packet, 1 if sub_values[0] < sub_values[1] else 0]
        elif type_id == 7:
            return [packet, 1 if sub_values[0] == sub_values[1] else 0]


_, value = parse_packet(packet)
print(value)
