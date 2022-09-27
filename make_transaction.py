import os
from dotenv import load_dotenv
from transaction_helpers import commit_transaction, get_mnemonic
from transaction_helpers import get_balance, generate_algorand_key_pair
load_dotenv()

# DEV NET ADDRESSES
wallet_1 = os.getenv('my_address_w1')
key_1 = os.getenv('private_key_w1')
wallet_3 = os.getenv('my_address_w3')
key_3 = os.getenv('private_key_w3')

# TEST NET ADDRESSES
test_address = os.getenv('test_address')
to_address = os.getenv('and_address')
test_key = os.getenv('test_private_key')

# Write down the address, private key, and the passphrase for later usage
# generate_algorand_key_pair()

get_mnemonic(test_key)

# check account balance
get_balance(test_address)
get_balance(to_address)
# get_balance(wallet_3)

# replace private_key and sender_address with your private key and sender
# address.
# Send from wallet_1 ---> wallet_3 in this case
# commit_transaction(test_key, test_address, to_address)
print('--- over and out ---')
