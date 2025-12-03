SIZE = 12

def sum_batteries(batteries: list[str]):
    number_str = "".join(batteries)
    return int(number_str)

def main():
    banks: str = []
    joltage_total_answer = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    for bank in lines:
        banks.append(bank.strip())
    
    for bank in banks:
        stack = []
        to_remove = len(bank) - 12
        for battery in bank:
            while stack and to_remove > 0 and int(battery) > int(stack[-1]):
                stack.pop()
                to_remove -= 1
            stack.append(battery)

        while to_remove:
            stack.pop()
            to_remove -= 1
        joltage_total_answer += sum_batteries(stack)
    print(joltage_total_answer)



            


    
        
        

if __name__ == '__main__':
    main()