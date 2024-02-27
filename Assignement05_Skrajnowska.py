class BasicMathOperations:
    def _init_(self):
        self.name = ""
    
    def greetUser():
        print("What is your first name?")
        self.firstName = input()
        print("What is your last name?")
        self.lastName = input()
        print("Hello ", self.firstName, " ", self.lastName)
    
    def addNumbers():
        print("Enter first number to add:")
        a = float(input())
        print("Enter second number to add:")
        b = float(input())
        sum = a + b
        return sum
    
    def preformOperations(num1, num2, operation):
        if(operation == "add"): output = num1 + num2
        elif(operation == "subtract"): output = num1 - num2
        elif(operation == "multiply"): output = num1 * num2
        elif(operation == "divide"): output = num1 / num2
        else: print("Invalid operation.")
        if(output): print("Output is ", output)
    
    def squareNumber(num):
        square = num ^ 2;
        return square
    
    def factorial(num):
        fact = 1
        for i in range(1,num + 1):
            fact *= i
        return fact
    
    def counting(start,end):
        for i in range(start,end):
            print(i)
    def computeHyponenuse(self):
        print("Enter length of base: ")
        base = float(input())
        print("Enter length of perpendicular: ")
        perpendicular = float(input())
        self.calculateHypotensuse(base, perpendicular)
        
    def calculateSquare(self,num):
        return self.squareNumber(num)
    
    def calculateHypotensuse(self,base,perpendicular):
        hypo = (self.calculateSquare(base) + self.calculateSquare(perpendicular))^0.5
        return hypo
    
    def areaOfRect(width,height):
        area = width * height
        return area
    def power():
        
    def typeOfArg():
        

def main():
    
    
    
main()
