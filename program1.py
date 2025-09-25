# calculater with class
class calculator:
    def __init__(self,a:float,b:float,operation:str):
        self.a=a
        self.b=b
        self.operation=operation.lower()
    def calculate(self):
        if self.operation=='add':
            return self.a+self.b
        elif self.operation=='subtract':
            return self.a-self.b
        elif self.operation=='multiply':
            return self.a*self.b
        elif self.operation=='divide':
            if self.b!=0:
                return self.a/self.b
            else:
                return "Error : Division by zreo"
        else:
            return 'Invalid operation'
cal1=calculator(10.5,2.5,'add')
cal2=calculator(10,5,'subtract')
cal3=calculator(10.5,2.5,'multiply')
cal4=calculator(10,0,'divide')
print("Result",cal1.calculate())
print("Result",cal2.calculate())
print("Result",cal3.calculate())
print("Result",cal4.calculate())



        