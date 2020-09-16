secret_word = "Hello World"
guess = ""
guess_count = 0
guess_limit = 1
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("If you guess the secret word i'll spare your life!: ")
        if guess != secret_word and not out_of_guesses:
            guess = input("Nope, try again!: ")
            if guess != secret_word and not out_of_guesses:
                guess = input("This is your last chance!: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Haha, You Lose, Any Last Words!")
else:
    print("Congratulations, You Win!, Now you are free!")
