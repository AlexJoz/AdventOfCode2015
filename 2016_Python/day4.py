import re
import collections
import string

if __name__ == '__main__':

    with open('/home/yakimbee/Desktop/input_day4.txt') as f:
        total_sum=0

        real_names = []
        for line in f:
            s = re.search("(([a-z]+-?)+)+(\d+)(\[.+)",line)
            first = s.group(1)
            numb = s.group(3)
            checksum = s.group(4)

            count = collections.Counter(first.replace('-', ''))
            cnt = sorted(count.items(), key=lambda x: (-x[1], x[0]))[:5]
            checksum_predicted = "".join([a for a, let in cnt])
            checksum = "".join(checksum.replace("[", "").replace("]", ""))

            if checksum_predicted == checksum:
                real_names.append((first, numb))
                total_sum += int(numb)

            cipher=''
            alphabet = string.ascii_lowercase
            part2_ans=None
            for f, k in real_names:
                for c in f:
                    if c == "-":
                        cipher += " "
                    else:
                        cipher += alphabet[(alphabet.index(c) + int(k)) % (len(alphabet))]
                if cipher == "northpole object storage ":
                    part2_ans=k
                cipher=''

        print("Part1: {}".format(total_sum))
        print("Part2: {}".format(part2_ans))

        '''
        --- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

Your puzzle answer was 158835.
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

Your puzzle answer was 993.
'''