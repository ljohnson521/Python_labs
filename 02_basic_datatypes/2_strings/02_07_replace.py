'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
practice = input('what is your favorite symbol: ')
practice1 = input('what is your favorite quote: ')
more_practice = practice1.replace(practice1[0], practice)
print(more_practice)
