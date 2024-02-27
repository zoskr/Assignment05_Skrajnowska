class BasicMathOperations:
    def greetUser(self):
        print("What is your first name?")
        self.firstName = input()
        print("What is your last name?")
        self.lastName = input()
        print("Hello ", self.firstName, " ", self.lastName)
    
    def addNumbers(self):
        print("Enter first number to add:")
        a = float(input())
        print("Enter second number to add:")
        b = float(input())
        sum = a + b
        return sum
    
    def preformOperations(self,num1, num2, operation):
        if(operation == "+"): output = num1 + num2
        elif(operation == "-"): output = num1 - num2
        elif(operation == "*"): output = num1 * num2
        elif(operation == "/"): output = num1 / num2
        print("Output is ", output)
    
    def squareNumber(self,num):
        square = num ** 2;
        return square
    
    def factorial(self,num):
        fact = 1
        for i in range(1,num + 1):
            fact *= i
        return fact
    
    def counting(self,start,end):
        for i in range(start,end+1):
            print(i)
    def computeHyponenuse(self):
        print("Enter length of base: ")
        base = float(input())
        print("Enter length of perpendicular: ")
        perpendicular = float(input())
        hypo = self.calculateHypotensuse(base, perpendicular)
        print("Hypotensuse is ", hypo)
        
    def calculateSquare(self,num):
        return self.squareNumber(num)
    
    def calculateHypotensuse(self,base,perpendicular):
        hypo = (self.calculateSquare(base) + self.calculateSquare(perpendicular))**0.5
        return hypo
    
    def areaOfRect(self,width,height):
        area = width * height
        return area
    def power(self,base,exp):
        val = base ** exp
        return val
    def typeOfArg(self,arg):
        return type(arg)

def main():
    obj = BasicMathOperations()
    
    print("Choose function: \n[A]Greet User \n[B]Add Numbers \n[C]Preform Operation")
    print("[D]Square Number\n[E]Factorial\n[F]Counting\n[G]Compute Hypotense")
    print("[H]Area of Rectangle\n[I]Power of Number\n[J]Type of Arguement\n[K]End Program")
    ans = input()
    
    while(ans != "K"):
        if(ans == "A"): obj.greetUser()
        elif(ans == "B"): 
            val = obj.addNumbers()
            print("Sum is ", val)
        elif(ans == "C"):
            print("Enter first number: ")
            num1 = float(input())
            print("Enter second number: ")
            num2 = float(input())
            print("Enter an operation:[+,-,*,/]")
            operation = input()
            obj.preformOperations(num1,num2, operation)
        elif(ans == "D"): 
            print("Enter number to square: ")
            num = float(input())
            val = obj.squareNumber(num)
            print("Square is", val)
        elif(ans == "E"):
            print("Enter number to calculate factorial: ")
            num = int(input())
            val = obj.factorial(num)
            print("Factorial is ", val)
        elif(ans == "F"):
            print("Enter number to start counting:")
            start = int(input())
            print("Enter nuber to end counting: ")
            end = int(input())
            obj.counting(start,end)
        elif(ans == "G"): obj.computeHyponenuse()
        elif(ans == "H"):
            print("Enter a length: ")
            l = float(input())
            print("Enter a width: ")
            w = float(input())
            A = obj.areaOfRect(l,w)
            print("Area is", A)
        elif(ans == "I"):
            print("Enter base value: ")
            base = float(input())
            print("Enter exponential value: ")
            exp = float(input())
            val = obj.power(base,exp)
            print("The value is ", val)
        elif(ans == "J"): 
            print("Enter arguement: ")
            arg = input()
            print(obj.typeOfArg(arg))
        else:    
            print("Invalid function.")
          
        print("Choose function: \n[A]Greet User \n[B]Add Numbers \n[C]Preform Operation")
        print("[D]Square Number\n[E]Factorial\n[F]Counting\n[G]Compute Hypotense")
        print("[H]Area of Rectangle\n[I]Power of Number\n[J]Type of Arguement\n[K]End Program")
        ans = input()
            
main()


