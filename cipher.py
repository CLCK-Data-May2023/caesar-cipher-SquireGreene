abc = "abcdefghijklmnopqrstuvwxyz"
plain_sentence = input("Please enter a sentence: ")
plain_sentence = plain_sentence.lower
shift = int(input("Please enter the number of places to shift "))

cypher = ""
for char in plain_sentence():
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
        cypher += char

print(cypher)
