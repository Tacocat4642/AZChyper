def solution(phrase):
    phraseInNumbers = []

    # Convert string to array of corresponding numbers (ex: a=1, b=2)
    # (Ignore anything other than lowercase numbers)
    for letter in phrase:
        if letter.islower():
            number = ord(letter) - 96
        else:
            number = ord(letter)
        phraseInNumbers.append(number)

    # Invert lowercase numbers
    # (Again, ignore anything other than lowercase numbers)
    for number in range(len(phraseInNumbers)):
        if phraseInNumbers[number] <= 26 and phraseInNumbers[number] > 0:
            phraseInNumbers[number] = 27 - phraseInNumbers[number]
        else:
            phraseInNumbers[number] = phraseInNumbers[number]

    # Convert array back into string and return value
    newPhrase = ""
    for letter in phraseInNumbers:
        if letter <= 26 and letter > 0:
            newPhrase = newPhrase + (chr(letter + 96))
        else:
            newPhrase = newPhrase + (chr(letter))

    return (newPhrase)
