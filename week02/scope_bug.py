def add_tip(bill,tip):
    total = bill + tip
    return total

def main():
    result = add_tip(100, 10)
    print(f"{result:.2f}")
main()    