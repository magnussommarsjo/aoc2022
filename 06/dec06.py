

with open("06/data.txt") as file:
    data = file.read()


def is_all_unique(chars: str) -> bool:
    return len(chars) == len(set(chars))

assert is_all_unique("abcd")
assert not is_all_unique("abbd")

def get_marker(data: str, number_unique: int) -> tuple[int, str]:
    for i in range(len(data)):
        # First 4 characters
        if i < number_unique:
            continue
        
        chars = data[i-number_unique:i]
        if is_all_unique(chars):
            return i, chars

start_of_packet, packet_char = get_marker(data, 4)
print(f"{start_of_packet=}, {packet_char=}")

#  PART TWO
start_of_messge, message_char = get_marker(data, 14)
print(f"{start_of_messge=}, {message_char=}")
