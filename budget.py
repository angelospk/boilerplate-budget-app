class Category:
  def __init__(self,name):
    self.name=name
    self.ledger=[]
    self.funds=0
  def deposit(self, amount, desc=""):
    temp={"amount": amount, "description": desc}
    self.ledger.append(temp)
    self.funds+=amount
  def check_funds(self, amount):
    if (self.funds>amount): return True
    else: return False
  def withdraw(self, amount, desc=""):
    if not (self.check_funds(amount)):
      return False
    else:
      amount=amount*(-1)
      temp={"amount":amount,"description":desc}
      self.funds+=amount
      self.ledger.append(temp)
      return True

  def get_balance(self):
    return self.funds
  def transfer(self,amount, other):
    descr="Transfer to "+other.name
    if(self.withdraw(amount, descr)):
      descr="Transfer from "+self.name
      other.deposit(amount,descr)
      return True
    else:
      return False
    
  def __repr__(self):
    l=(30-len(self.name))//2
    #print(self.ledger)
    ret="*"*l+self.name+"*"*l+"\n"
    for item in self.ledger:
      if (len(item["description"])>23):
        l=7
        tmp=item["description"][:23]
      else:
        l=30-len(item["description"])
        tmp=item["description"]
      ret+=tmp
      text="{:>"+str(l)+"}"
      ret+=text.format(float(item["amount"]))+"\n"
    ret+="Total: "+str(self.funds)
    return ret
      
    
def create_spend_chart(categories):
  
  return True