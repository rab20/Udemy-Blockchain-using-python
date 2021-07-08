
import json
import pickle

# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Provide an input')
    # 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
    print('2: Output data from file')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        # 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file
        #  – both with pickle and json.
        input_data = [input('Please provide an input: ')]
        #  Pickle
        with open('assign6.p', mode='wb') as f:
            f.write(pickle.dumps(input_data))
        # JSON
        with open('assign6.txt', mode='w') as f:
            f.write(json.dumps(input_data))
        print('The data has been written to a file')

    elif user_choice == '2':
        # 4) Adjust the logic to load the file content to work with pickled/ json data.
        with open('assign6.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            print('Using Pickle')
            print(file_content)
        with open('assign6.txt', mode='r') as f:
            file_content = f.readlines()
            print('Using JSON')
            print(json.loads(file_content[0]))

    else:
        waiting_for_input = False

print('Thank you for using the service')
