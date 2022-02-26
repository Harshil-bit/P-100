class atm(object):
    def __init__(self,cardNum,pinNum):
        self.cardNum=cardNum
        self.pinNum=pinNum
    
    def CashWithdrawal(self):
        print("Cash is being withdrawed")

    def BalanceEnquiry(self):
        print("This is balance enquiry")
    
obj=atm(156829,1407)
obj.CashWithdrawal()
obj.BalanceEnquiry()
