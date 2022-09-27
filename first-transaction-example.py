import os
import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
from dotenv import load_dotenv
load_dotenv()

wallet_1 = os.getenv('my_address_w1')
key_1 = os.getenv('private_key_w1')

wallet_3 = os.getenv('my_address_w3')
key_3 = os.getenv('private_key_w3')

test_address = os.getenv('test_address')
test_key = os.getenv('test_private_key')


# Write down the address, private key, and the passphrase for later usage
# generate_algorand_key_pair()

# get_mnemonic(test_key)





# replace private_key and sender_address with your private key and sender
# address.
# Send from wallet_1 ---> wallet_3 in this case
first_transaction_example(key_1, test_address, wallet_3)
print('--- over and out ---')
