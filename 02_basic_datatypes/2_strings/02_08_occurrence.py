'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
rope_val = input('Why did the chicken cross the road: ')
letter_val = input('what letter does your name start with: ')
where_val = rope_val.find(letter_val)
print(where_val)
