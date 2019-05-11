class Symbolic():
    def __init__(self,string, single = False, dic = None):
        if single == True:
            self.singleInit(string)
        elif string == None:
            self.dict = dict
        else:
            self.parse(string)
    
    def singleInit(self,string):
        self.dict = {}
        j = 0
        for i in string:
            if i.isidigit():
                j += 1
        self.dict[string[j:len(string)]] = int(string[0:j])
    
    def parse(self,string):
        pass

    
    def __mul__(self,other):
        for var in self.dict:
            for otherVar in other.dict:
                pass
        
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