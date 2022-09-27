import os
import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
from dotenv import load_dotenv
load_dotenv()


def generate_algorand_key_pair():
    """
    A method to generate an algorand key pair
    """
    global private_key, my_address
    private_key, my_address = account.generate_account()
    print("My address: {}".format(my_address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    print("Private key type: {}".format(type(private_key)))


def get_mnemonic(private_key: str) -> str:
    """
    A method to get mnemonic given a private key

    Parameters
    =--------=
    private_key: string
        The private key from which we are going to generate th mnemonic

    Returns
    =-----=
    string
        The mnemonic
    """
    print('Private key: *******')
    print(f"Mnemonic key: {mnemonic.from_private_key(private_key)}")
    return mnemonic.from_private_key(private_key)


def first_transaction_example(private_key, sender_address, receiver_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    print("\nSender address: {}".format(sender_address))
    account_info = algod_client.account_info(sender_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    # params.flat_fee = constants.MIN_TXN_FEE
    # params.fee = 1000
    amount = 100000
    note = "Initial transaction example".encode()

    print("\nReceiver address: {}".format(receiver_address))
    account_info = algod_client.account_info(receiver_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    unsigned_txn = transaction.PaymentTxn(sender_address, params,
                                          receiver_address, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Signed transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid,
                                                          4)
    except Exception as err:
        print("A damn error occurred: {}".format(err))
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(
        account_info.get('amount')))
    print("Amount transferred: {} microAlgos".format(amount))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(sender_address)
    print("Final Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")
