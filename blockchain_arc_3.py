import functools
import hashlib
import json

MINING_REWARD = 10

# Initializing blochchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Bharat'
# A set to store the participant names. This will only save unique values and will ignore duplicates
participants = {'Bharat'}


def hash_block(block):
    """Hashes a bloack and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed."""
    
    # List Comprehensions
    # return('-'.join([str(block[key]) for key in block]))
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    # balance for a sender in the open transactions list i.e they are not yet mined (part of the blockchain)
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)

    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += int(tx[0])
    # reduction logic using reduce function for the above code
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]

    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += int(tx[0])
    # reduction logic using reduce function for the above code
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

    return (amount_received - amount_sent)


def get_last_value():
    """ Returns last value of the blockchain list - This type of comment appears when hovered over 
        the function. Its called DOC STRING, used for detailing functions """
    if len(blockchain) < 1:
        return None
        # None is a special value. It does not mean empty. But that the value being returned is None.
    else:
        return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    if sender_balance >= int(transaction['amount']):
        return True
    else:
        return False


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.
    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with the transaction(Defaut = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    else:
        return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    # Chapter 78
    # [:] is a range selector to select all the values in the list - [starting index:ending index]  **ending index element is excluded
    # copied_transaction (local copy) is created so that open_transactions is not affeceted if mining fails post adding rewards.
    # This will leave the open_ transactions (global copy) uneffected.
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input of the user as a tuple. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input('Enter the recipient of the transaction : ')
    tx_amount = input('Enter the transaction amount : ')
    return (tx_recipient, tx_amount)


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
    """Verify the current blockchain and return True if valid"""
    for (index, block) in enumerate(blockchain):  # enumerate rrturns a tuple with index and value
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True


def verify_open_transactions():
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid

    # Return True if all the transactions in open_transactions is valid
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain block')
    print('4: Output the particaipants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data  # Unpacking tuple
        if add_transaction(recipient, amount=amount):
            print('Transaction successful')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_open_transactions():
            print('All transactions are valid')
        else:
            print('Invalid transactions found')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Max', 'recipient': 'Chris', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid. Please choose a value from the list')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        # Break out of the loop
        break
    print('Balance of {} : {:6.2f}'.format('Bharat', get_balance('Bharat')))
else:
    print('User left')

print('Done!')
