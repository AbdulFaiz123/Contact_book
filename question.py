class Question:

 def __init__(self,qdata,op1,op2,op3,op4,canswer):
    self.qdata = qdata
    self.op1 = op1
    self.op2 = op2
    self.op3 = op3
    self.op4 = op4
    self.canswer = canswer
 
 def __str__(self):
     return f"{self.qdata}\n a.{self.op1}\n b.{self.op2} \n c.{self.op3}\n d.{self.op4}"
 
