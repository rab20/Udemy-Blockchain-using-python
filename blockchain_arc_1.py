# Initializing blochchain list
blockchain = []


def get_last_value():
    """ Returns last value of the blockchain list - This type of comment appears when hovered over 
        the function. Its called DOC STRING, used for detailing functions """
    if len(blockchain) < 1:
        return None
        # None is a special value. It does not mean empty. But that the value being returned is None.
    else:
        return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    return float(input('Your transaction amount : '))


def get_user_choice():
    user_input = input('Your choice : ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console using For Loop
    # print(blockchain)   -- directly print the blockchain

    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 30)


def verify_chain():
    # block_index = 0
    is_valid = True
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index-1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         print('Blockchain modified at' + str(block[0]))
    #         break
    #     block_index += 1

    # Above code using range function --- range(5) -> 0 1 2 3 4
    # range(starting value, ending value, steps). Eg: range(5,20,2) -> 5 7 9 11 13 15 17 19
    # ending value is not included

    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            print('Blockchain modified at' + str(blockchain[block_index][0]))
            break

    return is_valid


#tx_amount = get_transaction_value()
# add_value(tx_amount)                     -- No longer required due to while loop below

#tx_amount = get_user_input()
# add_value(tx_amount, get_last_value())  -- No longer required due to while loop below

#tx_amount = get_user_input()
# add_value(tx_amount, get_last_value())  -- No longer required due to while loop below

waiting_for_input = True

while waiting_for_input:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain block')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid. Please choose a value from the list')

    if not verify_chain():
        print('Invalid blockchain!')
        break
else:
    print('User left')

print('Done!')
