import sys
import re

LINE_RE = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
OVERLAP = 'x'

def parse_line(line):
    return [int(i) for i in LINE_RE.match(line).groups()]

def main(size, input_file):
    fabric = [[0 for _ in range(size)] for _ in range(size)]
    claims = set()
    with open(input_file) as input_values:
        for line in input_values:
            n, x, y, width, height = parse_line(line)
            claims.add(n)
            for claim_y in range(y, y+height):
                for claim_x in range(x, x+width):
                    val = fabric[claim_y][claim_x]
                    if val:
                        claims.discard(val)
                        claims.discard(n)
                        fabric[claim_y][claim_x] = OVERLAP
                    else:
                        fabric[claim_y][claim_x] = n

    print(sum([l.count(OVERLAP) for l in fabric]))
    print(f"The claim(s) with ids {', '.join([str(c) for c in claims])} are intact")

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
