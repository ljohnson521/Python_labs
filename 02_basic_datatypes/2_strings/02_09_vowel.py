'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
input_string = input("enter sentence here: ")
string = input_string.lower()
print(string)
count = 0
list1 = ['a', 'e', 'i', 'o', 'u']
for char in string:
    if char in list1:
        count = count+1
print(count)

new_string = input('enter sentence here: ')
new_string1 = new_string.lower()

vowels = "aeiou"

vowelsdata = {}.fromkeys(vowels, 0)

for character in new_string1:
    if character in vowels:
        vowelsdata[character] += 1
for vowel in vowelsdata:
    print(vowel, " -> " , vowelsdata[vowel])

