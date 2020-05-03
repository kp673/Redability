
read = input("Text: ")


readLst = read.split()
words = len(readLst)
letters = 0
sentences = 0

for i in range(len(read)):
    if (read[i].isalpha()):
        letters += 1
    elif (read[i] in "?!."):
        sentences += 1
    else:
        continue

l = (100 * letters)/ words

s = (100 * sentences)/ words


index = (0.0588 * l) - (0.296 * s) - 15.8

if (index < 1):
    print("Before Grade 1")
elif (index > 16):
    print("Grade 16+")
else:
    print(f"Grade: {round(index)}")
