from pprint import pprint
from pyzil.zilliqa import chain
from pyzil.account import Account
from pyzil.contract import Contract


chain.set_active_chain(chain.TestNet)

account = Account(private_key="c4e0d95cc91d4cd72c68c9cf58eec49eb9e5c2cbc63fec61e7bef5e7555de0f0")
print(account)

contract_addr = "zil13mf5zaahphzxk228u0kadk09z6plf8cuppv0df"
contract = Contract.load_from_address(contract_addr)

contract.account = account

resp = contract.call(method="getHello", params=[])
pprint(resp)
pprint(contract.last_receipt)

resp = contract.call(method="setHello", params=[Contract.value_dict("msg", "String", "hi contract.")])
pprint(resp)
pprint(contract.last_receipt)

resp = contract.call(method="getHello", params=[])
pprint(resp)
pprint(contract.last_receipt)

# see more examples in test_contract.py
