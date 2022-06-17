user_name = input(
    "Hey there ! type in your name as shown eg- 'Himanshu Lahoti'")

#space_index = user_name.find(' ')
# user_firstname = (user_name[:space_index])             i used this self made code first
# user_lastname = (user_name[space_index + 1:])          then realised when can do in 1 line why go for 3.

#words = user_name.split(" ")
user_firstname, user_lastname = user_name.split(" ")

print(f'Welcome Mr.{user_lastname}😇!')


while True:
    user_input = input('''
Type 'Add' to perform Addition.
Type 'Subtract' to perform Subtraction.
Type 'Multiply' to perform Multiplication.
Type 'Div' to perform Division.
Type 'Quit' to Quit.

Note: Words are not case sensative. Type Unwisely

''').lower()
    if user_input == "add":
        x, y = input(
            "Enter two numbers to add seperated by a space. eg '5  10': ").split()
        ans = int(x) + int(y)
        print(f'The sum is: {ans}')
    elif user_input == "subtract":
        x, y = input(
            "Enter two numbers to subtract seperated by a space. eg '5  10': ").split()
        ans = int(x) - int(y)
        print(f'The ans is: {ans}')
    elif user_input == "multiply":
        x, y = input(
            "Enter two numbers to multiply seperated by a space. eg '5  10': ").split()
        ans = int(x) * int(y)
        print(f'The ans is: {ans}')
    elif user_input == "div":
        x, y = input(
            "Enter two numbers to divide seperated by a space. eg '5  10': ").split()
        ans = int(x) / int(y)
        print(f'The ans is: {ans}')
    elif user_input == "quit":
        break
    else:
        print("Wrong input")
