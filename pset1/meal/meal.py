def main():
    time = input("what time is it? ")
    if(7 <= convert(time) <= 8):
        print("breakfast")
    elif(12 <= convert(time) <= 13):
        print("lunch")
    elif(18 < convert(time) <= 19):
        print("dinner")

    return 0

def convert(time):
    hours,minutes = time.split(":")
    hours=float(hours)
    minutes = float(minutes)/60
    time = hours+minutes
    return time

if __name__ == "__main__":
    main()