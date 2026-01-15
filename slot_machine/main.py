import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 1,   # very rare (jackpot symbol)
    "B": 3,
    "C": 6,
    "D": 10   # very common
}

symbol_values = {
    "A": 10,   # 10x multyplier (jackpot symbol)
    "B": 6,
    "C": 3,
    "D": 1   # very common
}

def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns =[]

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]#copy of array
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row])


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number.")
        
    return amount 

def get_num_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number.")
        
    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"\n Bet must be between ${MIN_BET} and ${MAX_BET}!\n")
        else:
            print("Please enter a number.")
        
    return amount 

def spin(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"\nYou don't have enough money to bet ${total_bet}, yout current balance is only ${balance}\n")
        else:
            break

    print(f"\nYou're betting ${bet} on {lines} lines. Your total bet is ${total_bet}\n")

    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print (f"\nYou won ${winnings}!")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet



def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        play = input("\n----Press Enter to play or \"q\" to quit----\n").lower()
        if play == "q":
            break
        balance += spin(balance)

    print(f"\nYou left with ${balance}!")
    

main()