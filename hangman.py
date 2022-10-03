


word = "Batman"

# Allowed errors the user can make
allowed_errors = 3

# letters the user has gussed
guessed_letters = []

# indication flag
done = False

while not done:
    for letter in word:

        if letter.lower() in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"health remaning{allowed_errors}, Nest Guess is:")
    guessed_letters.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -=1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in  guessed_letters:
            done = False
if done:
    print(f"health remaning{allowed_errors}, You won, the word was {word}:")
else:
    print(f"health remaning{allowed_errors}, Game Over, the word was {word}:")
