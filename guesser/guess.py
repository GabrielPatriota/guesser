import generate
while 1:
    guess = int(input())

    difference = generate.x - guess

    if difference <= 10:
        if difference >= 0:
            print("Close!\n")
        if difference >= -10:
            print("Close!\n")
        if difference <= -11:
            print("Oh that's a bad guess\n")
    if difference > 10:
        if difference <= 100:
            print("Oh that's a bad guess\n")

    if guess == generate.x:
        print("Wow you got it!\n")
        generate.x