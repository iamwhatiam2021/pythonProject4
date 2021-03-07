import datetime
fp = open("mydiary.txt", "a")
while True:
    entry = input("What are you doing now (type quit to exit)")
    now = datetime.datetime.now()
    today = now.strftime("%d/%m/%y %H:%M")
    print(today)
    if entry == "quit":
        break
    # \n means new line
    fp.write(f"{today} {entry}\n")
fp.close()
