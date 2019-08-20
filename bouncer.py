from pprint import pprint

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer

chain.set_active_chain(chain.TestNet)  
# load account from wallet address
account = Account(address="zil1sf2t9jdvmuvp6ht8jmtrxg8mkgx5ahgj6h833r")
balance = account.get_balance()
print("{}: {}".format(account, balance))

# load account from private key
# private key is required to send ZILs
account = Account(private_key="05C3CF3387F31202CD0798B7AA882327A1BD365331F90954A58C18F61BD08FFC")
balance2 = account.get_balance()
print("Account balance: {}".format(balance2))

# to_addr must be bech32 address or 20 bytes checksum address
to_addr = "zil147a08dxa4pc3jhls8ydl2mmmz4nfar8kxyxx79"
# send ZILs
txn_info = account.transfer(to_addr=to_addr, zils=2.718)
pprint(txn_info)
txn_id = txn_info["TranID"]

# wait chain confirm, may takes 2-3 minutes on MainNet
txn_details = account.wait_txn_confirm(txn_id, timeout=300)
pprint(txn_details)
if txn_details and txn_details["receipt"]["success"]:
    print("Txn success: {}".format(txn_id))
else:
    print("Txn failed: {}".format(txn_id))