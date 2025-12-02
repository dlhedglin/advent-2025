from dataclasses import dataclass

@dataclass
class DialMove:
    direction: str
    count: int

def parse_input_file(file_name: str) -> list[DialMove]:
    moves = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    for line in lines:
        direction = line[0]
        count = int(line[1::])
        moves.append(
            DialMove(direction=direction, count=count)
        )
    return moves

class SafeDial:
    def __init__(self):
        self.position = 50
        self.zero_count = 0
    
    def get_position(self):
        return self.position
    
    def rotate(self, dial_move: DialMove):
        for _ in range(dial_move.count):
            if dial_move.direction == "R":
                self.position += 1
                if self.position == 100:
                    self.position = 0
            elif dial_move.direction == "L":
                self.position -= 1
                if self.position == -1:
                    self.position = 99
            if self.position == 0:
                self.zero_count += 1


def main():
    safe_dial = SafeDial()
    moves = parse_input_file('input.txt')
    for move in moves:
        safe_dial.rotate(move)
    print(safe_dial.zero_count)
    



if __name__ == '__main__':
    main()


