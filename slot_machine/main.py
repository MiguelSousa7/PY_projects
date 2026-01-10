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

def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns =[[],[],[]]

    

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
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a number.")
        
    return amount 

def main():
    print("""
You will be playing in a slot machine like this
          
        ╔════════════════════════════╗
        ║      ★ SLOT MACHINE ★      ║
        ╠════════════════════════════╣
        ║    ╔═══╗  ╔═══╗  ╔═══╗     ║
        ║    ║ A ║  ║ A ║  ║ D ║     ║
        ║    ╚═══╝  ╚═══╝  ╚═══╝     ║
        ║----------------------------║
        ║    ╔═══╗  ╔═══╗  ╔═══╗     ║
        ║    ║ B ║  ║ D ║  ║ C ║     ║
        ║    ╚═══╝  ╚═══╝  ╚═══╝     ║
        ║----------------------------║
        ║    ╔═══╗  ╔═══╗  ╔═══╗     ║
        ║    ║ D ║  ║ D ║  ║ A ║     ║
        ║    ╚═══╝  ╚═══╝  ╚═══╝     ║ 
        ╠════════════════════════════╣
        ║ BALANCE: $250   BET: $25   ║
        ╚════════════════════════════╝
          
""")

    balance = deposit()
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"\nYou don't have enough money to bet ${total_bet}, yout current balance is only ${balance}\n")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

main()