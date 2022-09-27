import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction


def generate_algorand_keypair():
    global private_key, my_address
    private_key, my_address = account.generate_account()
    print("My address: {}".format(my_address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    print("Private key type: {}".format(type(private_key)))

# Write down the address, private key, and the passphrase for later usage
# generate_algorand_keypair()


my_address_w3 = 'FESYQ3KZ7J3SPRFYW4RD3NVJZ3VECXUD2JR4AEKISR7SJURIJL3IHA746U'
private_key_w3 = "IOiOOnoazJfFqBNDtoDJHGPvxrv7dOPjk8wZe4uLLBdI7jhwv7vrmqogdCcpFKFK1BpRortLqPVXOzqkVzlY5A=="

my_address_w1 = 'OMT4JDUEYPFMJTJG5BLTBWFKXHP3XILKIT76BXAKSZF4JXM7VCM2Q7MIFY'
private_key_w1 = "JxQ0q/ZxcXhl/OV7jnHzdjW2HADs7e6BtV+78VzKJIFVihd2VQAxxY93tZYX9HqSxKzvgAVcFzYGFY3MLYiFUA=="

my_address = 'WF7P5H6IJM34MWAQYDNNKADTPHPB3AUZAEMEZHWCI6OT7C46XGRQCWJJGU'
private_key = 'UVTpeCs0sT2hJg4cStwO463BJ1zP3+Bfqw6eRDL7PG+xfv6fyEs3xlgQwNrVAHN53h2CmQEYTJ7CR50/i565ow=='


def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    print("Sender address: {}".format(my_address))
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = constants.MIN_TXN_FEE
    params.fee = 1000
    receiver_w1 = "OMT4JDUEYPFMJTJG5BLTBWFKXHP3XILKIT76BXAKSZF4JXM7VCM2Q7MIFY"
    amount = 100000
    note = "Initial transaction example".encode()

    print("Receiver address: {}".format(receiver_w1))
    account_info = algod_client.account_info(receiver_w1)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver_w1,
                                          amount, None, note)

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
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(
        account_info.get('amount')))
    print("Amount transferred: {} microAlgos".format(amount))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")


# replace private_key and my_address with your private key and your address.
first_transaction_example(private_key, my_address)
print('--- over and out ---')
