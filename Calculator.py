class Calculator():
    def __init__(self,name,num_1,num_2):
        self.name = name
        self.num_1 = num_1
        self.num_2 = num_2
        
    def multiply(self):
        print(f"Hey {self.name} the solution is:",self.num_1 * self.num_2)
    def sub(self):
        print(f"Hey {self.name} the solution is:",self.num_1 - self.num_2)
    def divide(self):
        print(f"Hey {self.name} the solution is:",self.num_1 / self.num_2)
    def add(self):
        print(f"Hey {self.name} the solution is:",self.num_1 + self.num_2)
        
    calc=Calculator("prem chand",7,2)
    
   calc.multiply()
   
   calc.sub()
   
   calc.divide()
   
   calc.add()
