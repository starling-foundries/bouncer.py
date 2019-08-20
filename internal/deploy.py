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
        "vname" : "_scilla_version",
        "type" : "Uint32",
        "value" : "0"
    },
    {
        "vname" : "name",
        "type" : "String",
        "value" : "ERC777"
    },
    {
        "vname" : "symbol",
        "type" : "String",
        "value" : "Merkalise"
    },
    {
        "vname" : "totalSupply",
        "type" : "Uint128",
        "value" : "1000"
    },
    {
        "vname" : "owner",
        "type" :  "ByStr20",
        "value" :  "0x263C4CA003235AF83C4F4BC065D00D4A67FFB617"
    },
    {
        "vname" : "granularity",
        "type" : "Uint128",
        "value" : "4"
    },
    {
        "vname" : "_creation_block",
        "type" : "BNum",
        "value" : "100"
    }
]

contract = Contract.new_from_code(code=code)
print(contract)

# set account before deploy
contract.account = account

contract.deploy(init_params=init_params, gas_limit=1000000,timeout=2200, sleep=10)
assert contract.status == Contract.Status.Deployed