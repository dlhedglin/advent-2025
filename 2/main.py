

def parse_input(file_name: str):
    res = []
    with open(file_name, 'r') as f:
        line = f.readline()
    ranges = line.split(',')
    for r in ranges:
        numbers = r.split('-')
        start, end = numbers[0], numbers[1]
        res.append((int(start), int(end)))
    return res

    



def main():
    ranges = parse_input('input.txt')
    invalid_codes = set()
    for r in ranges:
        range_start, range_end = r
        for number in range(range_start, range_end+1):
            number_str = str(number)
            for chunk_size in range(1, len(number_str)):
                chunks = [number_str[i:i+chunk_size] for i in range(0, len(number_str), chunk_size)]
                first_chunk = chunks[0]
                for i, chunk in enumerate(chunks):
                    if i == 0:
                        continue
                    # print(first_chunk, chunk)
                    if chunk != first_chunk:
                        break
                    if i == len(chunks)-1:
                        invalid_codes.add(number)
                        
    print(sum(invalid_codes))


if __name__ == '__main__':
    main()