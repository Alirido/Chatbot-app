class Questions:
    def __init__(self,q,a):
        self.q = q
        self.a = a
    
    def __repr__(self):
        return "Questions('{}','{}')".format(self.q,self.a)