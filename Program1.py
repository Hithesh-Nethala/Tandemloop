class Cal:
    def __init__(self,a,b,method):
        self.a=a
        self.b=b
        self.method=method
    
    def opr(self):
        if self.method=='add':
            return self.a + self.b
        elif self.method=='sub':
            return self.a - self.b
        elif self.method == 'multiply':
            return self.a * self.b
        elif self.method == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return 'Invalid'
a=int(input('Enter a: '))
b=int(input('Enter b: '))
operation=input('Enter Operation: ')
cal1=Cal(a,b,operation.lower())
res=cal1.opr()
print(res)