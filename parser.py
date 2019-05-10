class ParseTree():
    def __init__(self,left,right,type, value):
        self.value = value
        self.type = type
        self.left = left
        self.right = right
        self.n = 0
        self.i = 0
    
    def parse(self,string):
        tree = self.parseExpr(string)
        self.value = tree.value
        self.type = tree.type
        self.left = tree.left
        self.right = tree.right
        self.i = 0
    
    def parseExpr(self,string):
        p1 = self.parseTerm(string)
        if self.i > len(string)-1:
            return p1
        if string[self.i] == '+':
            self.i += 1
            p2 = self.parseExpr(string)
            return ParseTree(p1,p2,'ADD',None)
        elif string[self.i] == '-':
            self.i += 1
            p2 = self.parseExpr(string)
            return ParseTree(p1,p2,'MIN',None)
        elif string[self.i] == '^':
            self.i += 1
            p2 = self.parseExpr(string)
            return ParseTree(p1,p2,'POW',None)
        else:
            return p1

    
    def parseTerm(self,string):
        p1 = self.parseFac(string)
        if self.i > len(string)-1:
            return p1
        if string[self.i] == '*':
            self.i += 1
            p2 = self.parseTerm(string)
            return ParseTree(p1,p2,'MUL',None)
        elif string[self.i] == '/': 
            self.i += 1
            p2 = self.parseTerm(string)
            return ParseTree(p1,p2,'DIV',None)
        else:
            return p1
    
    def parseFac(self,string):
        self.i += 1
        if string[self.i-1] == '(':
            tmp = self.parseExpr(string)
            if string[self.i] != ')':
                raise ValueError(f"Missing closing parentheses: {string}")
            self.i += 1
            return tmp
        return self.parseNum(string)
    
    def parseNum(self,string):
        j = self.i-1
        while self.i < len(string) and (string[self.i].isdigit() or string[self.i].isalpha()):
            self.i += 1
        return ParseTree(None, None, 'NUM', string[j:self.i])


    def evaluate(self):
        if self.type == 'ADD':
            p1 = self.left.evaluate()
            p2 = self.right.evaluate()
            return p1 + p2
        if self.type == 'MIN':
            p1 = self.left.evaluate()
            p2 = self.right.evaluate()
            return p1 - p2
        if self.type == 'POW':
            p1 = self.left.evaluate()
            p2 = self.right.evaluate()
            return p1**p2
        if self.type == 'MUL':
            p1 = self.left.evaluate()
            p2 = self.right.evaluate()
            return p1 * p2
        if self.type == 'DIV':
            p1 = self.left.evaluate()
            p2 = self.right.evaluate()
            return p1 / p2
        if self.type == 'NUM':
            return int(self.value)

tree = ParseTree(None,None,None,None)
tree.parse("12a+4*3")
x=tree.evaluate()
print(x)

"""  
<expr> ::= <term> "+" <expr> 
        |  <term> "-" <expr> 
        |  <term> "^" <expr>
        |  <term>

<term> ::= <factor> "*" <term>
        |  <factor> "/" <term>
        |  <factor>

<factor> ::=  "(" <expr> ")"
        |  <const><variable>
        |  <const>

<const> ::= integer

<variable ::= char

 """
