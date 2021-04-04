import generate
guesses = 0
while 1:
    guess = int(input())

    difference = generate.x - guess

    if difference <= 10:
        if difference >= 0:
            print("Close!\n")
            guesses += 1
        if difference >= -10:
            print("Close!\n")
            guesses += 1
        if difference <= -11:
            print("Oh that's a bad guess\n")
            guesses += 1
    if difference > 10:
        if difference <= 100:
            print("Oh that's a bad guess\n")
            guesses += 1

    

    if guess == generate.x:
        print("Wow you got it!\n")
        print("Hmmm... " + str(guesses) + " guesses...")
        generate.x