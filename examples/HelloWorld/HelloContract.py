from pprint import pprint

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer
chain.set_active_chain(chain.MainNet)

#handles abstraction of calling contract as wallet
 class HelloContract:
     def __init__(self, zilliqa_chain, bouncer_wallet, deployed=false):
         self.chain = zilliqa_chain
         self.wallet = bouncer_wallet
    
    # Calls the Hello {Name} transition on this contract
    def call_hello(self, ):
        pass

    #Imports a .scilla file to deploy to the targeted chain and retauns
    def deploy_contract()
