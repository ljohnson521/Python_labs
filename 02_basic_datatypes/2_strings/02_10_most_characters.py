'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
test1 = input("Enter sentence here: ")
test_one = len(test1)
test2 = input("Enter sentence here: ")
test_two = len(test2)
test3 = input("Enter sentence here: ")
test_three = len(test3)
final_test = {test_three: test3, test_two: test2, test_one: test1}
for test in final_test.items():
    print(test)
test_values = final_test.values()
max_values = max(test_values)
print(max_values)
