from pprint import pprint
from pyzil.zilliqa import chain
from pyzil.account import Account
from pyzil.contract import Contract


chain.set_active_chain(chain.TestNet)

account = Account(private_key="c4e0d95cc91d4cd72c68c9cf58eec49eb9e5c2cbc63fec61e7bef5e7555de0f0")
print(account)
code = open("HelloWorld.scilla").read()
init_params = [
      {
        "vname": "_scilla_version",
        "type": "Uint32",
        "value": "0",
      },
      {
        "vname": "owner",
        "type": "ByStr20",
        # NOTE: all byte strings passed to Scilla contracts _must_ be prefixed with 0x. Failure to do so will result in the network rejecting the transaction while consuming gas!
        "value": "0xafdb4c759eff9d894af75abfb6bde2c7fc3623a9",
      }
    ]

contract = Contract.new_from_code(code)
print(contract)

# set account before deploy
contract.account = account

# contract.deploy(init_params=init_params, gas_limit=10000000,timeout=2200, sleep=10)
contract.deploy(timeout=300, sleep=10)
assert contract.status == Contract.Status.Deployed