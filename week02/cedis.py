def to_cedis(dollars):
    return dollars * 15.5
def main():
    dollars = float(input("Enter amount in US dollars: "))
    cedis = to_cedis(dollars)
    print(f"GHS   {cedis:.2f}")
main()    