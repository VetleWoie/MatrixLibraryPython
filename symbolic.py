class Symbolic():
    def __init__(self,string):
        self.dict = {}
        j = 0
        for i in string:
            if i.isidigit():
                j += 1
        self.dict[string[j:len(string)]] = int(string[0:j])

    
    def __mul__(self,other):
        pass
        
        
