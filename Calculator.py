########################
# ADVANCED CALCULATOR  #
########################

def NormalCalculator():
    print("\n=============== Normal Calculator ===============")
    # Inputs
    Num1 = float(input("Enter first number:"))
    Num2 = float(input("Enter second number:"))

 # Menu card
    print("*****************************")
    print("*  1. For Addition          *")
    print("*  2. For Subtraction       *")
    print("*  3. For Multiplication    *")
    print("*  4. For Division          *")
    print("*  5. To go Back            *")
    print("*****************************")
    ask = int(input("Enter you choice(corresponding number):"))

     # Operations
    if (ask == 1):
        Ans = Num1 + Num2
        print(Num1," + ",Num2," = ",Ans)
    elif (ask == 2):
        Ans = Num1 - Num2
        print(Num1," - ",Num2," = ",Ans)
    elif (ask == 3):
        Ans = Num1*Num2
        print(Num1,"*",Num2," = ",Ans)
    elif (ask == 4):
        Ans = Num1/Num2
        print(Num1,"/",Num2," = ",Ans)
    elif (ask == 5):
        Main()
    else:
        print("Wrong choice. Try agian")
        
    NormalCalculator()

def UnitConversions():
    print("\n=============== Unit Convertor ===============")
    
    # Inputs
    Num1 = float(input("Enter the unit value to convert:"))
    
    # Menu card
    print("***************************************")
    print("*  NOTE:- Give -ve values for reverse *")
    print("*  1. For Kilograms to Grams          *")
    print("*  2. For Liter to Mili-Liter         *")
    print("*  3. For Rupees to Dollars           *")
    print("*  4. To go Back                      *")
    print("***************************************")
    ask = int(input("Enter you choice(corresponding number):"))

 # Operations
    if (ask == 1):
        Ans = Num1*1000   # 1kg = 1000g
        print(Num1,"kg = ",Ans,"g")
    elif (ask == 2):
        Ans = Num1*1000   # 1L = 1000ml
        print(Num1,"L = ",Ans,"ml")
    elif (ask == 3):
        Ans = Num1*0.0125   # 1₹ = 1/80$ = 0.0125$
        print(Num1,"₹ = ",Ans,"$")
    elif (ask == 4):
        Main()
    elif (ask == -1):
        Ans = Num1*0.001   # 1g = 1/1000kg = 0.001kg
        print(Num1,"g = ",Ans,"kg")
    elif (ask == -2):
        Ans = Num1*0.001   # 1ml = 1/1000ml = 0.001ml
        print(Num1,"ml = ",Ans,"L")
    elif (ask == -3):
        Ans = Num1*0.0125   # 1$ = 80₹ 
        print(Num1,"$ = ",Ans,"₹")
    else:
        print("Wrong choice. Try agian")
        
    UnitConversions()

def BMICalculator():
    print("\n=============== BMI Calculator ===============")
    # Input
    wt = float(input("Enter the weight (in Kg):"))
    ht = float(input("Enter the height (in  m):"))

    # BMI calculation.
    BMI = wt/(ht*ht)
    
    # Output
    print("\nYour BMI is:",BMI)
    if (BMI < 18.5):
        print("That means you are undernourished")
    elif (BMI > 26.5):
        print("You are a bit over weighed")
    else:
        print("You are physically fit as per BMI")

    Main()

def LoanCalculator():
    print("\n=============== Loan Calculator ===============")
    # Input
    P   = float(input("Enter the principle:"))
    R = float(input("Enter the Intrest Rate:"))
    IntrestTime = float(input("Intrest Time period(in Months):"))   # Like 5% Rate of Intrest per annum.
    T        = float(input("Time period(in yrs):"))
    IntrestType = input("Intrest Type (Simple,Compund):")

    if (IntrestType.lower() == "simple"):

        # Simple intrest formula.
        Amount = (P*T*R)*(IntrestTime)/12*100
    elif (IntrestType.lower() == "compound"):

        # Compound Intrest.
        Amount = P*((1 + (R/100)*(IntrestTime/12))**(T*(12/IntrestTime)))

    else:
        print("Sorry! There is no such option.")
        Main()
    print("\nThe Amount after ",T,"yrs will be:",Amount)
    Main()

#======== Main function =============
def Main():
    print("\n=============== Main Function ===============")
    print("*****************************")
    print("*  1. For Normal calculator *")
    print("*  2. For Unit conversions  *")
    print("*  3. For BMI calculations  *")
    print("*  4. For Loan calculations *")
    print("*  5. For Exit              *")
    print("*****************************")
    ask = int(input("Enter you choice(corresponding number):"))

    if (ask == 1):
        NormalCalculator()
    elif (ask == 2):
        UnitConversions()
    elif (ask == 3):
        BMICalculator()
    elif (ask == 4):
        LoanCalculator()
    elif (ask == 5):
        exit()
    else:
        print("Wrong choice. Try agian")
        Main()

# Intiator ( starting of the program)
Main()
