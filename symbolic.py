import code;
class Symbolic():
    def __init__(self,string, single = False, dic = None):
        if single == True:
            self.singleInit(string)
        elif string == None:
            self.dict = dic
        else:
            self.parse(string)
    
    def singleInit(self,string):
        self.dict = {}
        j = 0
        for i in string:
            if i.isdigit():
                j += 1
        self.dict[string[j:len(string)]] = int(string[0:j])
    
    def parse(self,string):
        pass
    
    def __repr__(self):
        return f'{self.dict}'

    def __mul__(self,other):
        dic = {}
        for var in self.dict:
            for otherVar in other.dict:
                dic[var+otherVar] = self.dict[var]*other.dict[otherVar]
        return Symbolic(None, dic = dic)
        
    def __add__(self,other):
        dic = {}
        for var in self.dict:
            if var in other.dict:
                dic[var] = self.dict[var] + other.dict[var]
            if var not in other.dict:
                dic[var] = self.dict[var]
        for var in other.dict:
            if var not in self.dict:
                dic[var] = other.dict[var]
        return Symbolic(None,dic = dic)
    
    def __sub__(self,other):
        dic = {}
        for var in self.dict:
            if var in other.dict:
                dic[var] = self.dict[var] - other.dict[var]
            if var not in other.dict:
                dic[var] = -1*self.dict[var]
        for var in other.dict:
            if var not in self.dict:
                dic[var] = -1*other.dict[var]
        return Symbolic(None,dic = dic)

x = Symbolic("12a",True)
y = Symbolic("4a",True)
z = Symbolic("3b",True)
k = Symbolic("43b",True)
code.interact(local=locals())