from pprint import pprint
from pyzil.zilliqa import chain
from pyzil.account import Account
from pyzil.contract import Contract


chain.set_active_chain(chain.TestNet)

account = Account(private_key="c4e0d95cc91d4cd72c68c9cf58eec49eb9e5c2cbc63fec61e7bef5e7555de0f0")
print(account)
code = open("contract.scilla").read()
contract = Contract.new_from_code(code)
print(contract)

# set account before deploy
contract.account = account

contract.deploy(timeout=300, sleep=10, gas_limit=1000000)
assert contract.status == Contract.Status.Deployed