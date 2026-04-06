class Calculator:
    def __init__(self):
        self.result= 0
        self.history= []

    def add(self, a, b):
        self.result= a+b 
        self.append_history()
        return self.result
    
    def sub(self, a, b):
        self.result= a-b
        self.append_history()
        return self.result

    def multiply(self, a, b):
        self.result= a*b
        self.append_history()
        return self.result
    
    def divide(self, a, b):
        if(b<=0):
            return "Error: Invalid Input"
        self.result= a/b
        self.append_history();
        return self.result
    
    def square(self, a):
        self.result=a**2
        self.append_history();
        return self.result
    
    def sq_root(self, a):
        self.result= a**0.5
        self.append_history()
        return self.result
    
    def append_history(self):
        self.history.append(self.result)


