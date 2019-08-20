import random
import dataset

import service_pb2 as pb
from service_twirp_srv import (Errors, OperatorImpl, OperatorServer,
                                   TwirpServerException)

class Operator(OperatorImpl):
    def SendCheck(self, checkTx):
        if size.Inches <= 0:
            raise TwirpServerException(Errors.InvalidArgument,
                                 "I can't make a hat that small")
        return pb.queueID(Size=size.Inches,
                      Color=random.choice("white", "black", "brown", "red"),
                      Name=random.choice("bowler", "top hat", "derby"))
    
    def Status(self, queueID):
    
    def GetLastTransaction(self, client):
    
    def OperatorTarget(self):

    def GetMinFee(self):
    
if __name__ == "__main__":
    app = HaberdasherServer(MadHaberdasher())
    bjoern.run(app, "0.0.0.0", 8080)