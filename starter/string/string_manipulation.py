# Prompts the user to enter a sentence.
# Converts the entire sentence to uppercase and prints the result.

sentence=input("Please Enter a sentence: ")

sentence=sentence.upper()
print("Upper cased: ",sentence)


#print in reverse order
words= sentence.split()

words.reverse()
backToNormal=" ".join(words)

print("Reveresed: ",backToNormal)

# get the vowles
count=0
for word in sentence:
    for letter in word.lower():
        if letter=="o" or letter =="e"or  letter =="a"or letter =="i"or letter =="u":
            count+=1
print("Number of vowels: ",count)


# replace the space with hiphen

words=sentence.split()

new_sentence="-".join(words)

print("New sentence with hyphen: ",new_sentence)