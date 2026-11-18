def fare(stops,price=2.5):
    return stops * price

def main():
    stops = int(input("How many stops: "))
    total = fare(stops)
    print(f"Total fare: ${total:.2f}")
if __name__ == "__main__":
    main()
    