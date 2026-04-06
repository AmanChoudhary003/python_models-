from models.operations import Calculator
from models.result import result


calc= Calculator();


num= calc.add(1, 3)
num3= calc.sub(10, 5)
num5= calc.divide(15, 5)
num6= calc.sq_root(25)
num2= calc.history


print(result(num))
print(num2)