print("-----------------------------------------")
print("    Welcome to the currency converter    ")
print("-----------------------------------------")
#Initialising the exchange rate variables
USD_Rate = 79.56
Euro_Rate = 80.81
Yen_Rate = 0.60
Ruble_Rate = 1.28

#Taking USD input from the user
USD_amount = input("How many USD does Paxton have? ")

#Taking other currency inputs from the user
Yen_amount = input("How many Yen does Akio have? ")
Euro_amount = input("How many Euro does Karl have? ")
Ruble_amount = input("How many Ruble does Boris have? ")

#Type casting the values to fliat
USD_amount = float(USD_amount)
Yen_amount = float(Yen_amount)
Euro_amount = float(Euro_amount)
Ruble_amount = float(Ruble_amount)

#Calculating the INR equivalent
USD_INR = USD_amount * USD_Rate
Yen_INR = Yen_amount * Yen_Rate
Euro_INR = Euro_amount * Euro_Rate
Ruble_INR = Ruble_amount * USD_Rate

#Displaying the results
print("\nPaxton has",USD_amount,"USD =",USD_INR,"INR")
print("Akio has",Yen_amount,"Yen =",Yen_INR,"INR")
print("Karl has",Euro_amount,"Euro =",Euro_INR,"INR")
print("Boris has",Ruble_amount,"Ruble =",Ruble_INR,"INR")

#Calculating and displaying total trip fund
Total_trip_fund = USD_INR+Yen_INR+Euro_INR+Ruble_INR
print("\nTotal amount all 4 friends have in India are =",Total_trip_fund)
