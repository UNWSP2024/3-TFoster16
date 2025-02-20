#Timothy Foster, Hot Dog Price Calculator, 2/20/25

def calculateHotDogPrice():
    #Define the function

    #Define the variable.
    pretaxPrice = 0.00

    #Get input for what kind of hot dog the user would like.
    chilidogAnswer = input("Would you like a chili dog? Answer 'Yes' if so.")

    #Assign the variable a starting price based off the answer.
    if chilidogAnswer == "Yes":
        pretaxPrice = 4.50
    else:
        pretaxPrice = 3.50

    cheeseAnswer = input("Would you like cheese? Answer 'Yes' if so.")

    #Add more charge if the answer is yes.
    if cheeseAnswer == "Yes":
        pretaxPrice = pretaxPrice + 0.50

    peppersAnswer = input("Would you like peppers? Answer 'Yes' if so.")

    #Add more charge if the answer is yes.
    if peppersAnswer == "Yes":
        pretaxPrice = pretaxPrice + 0.75

    grilledonionsAnswer = input("Would you like grilled onions? Answer 'Yes' if so.")

    #Add more charge if the answer is yes.
    if grilledonionsAnswer == "Yes":
        pretaxPrice = pretaxPrice + 1.00

    #Display the cost of the hot dog before tax.
    print("The cost of your hot dog is",pretaxPrice,".")

    #Calculate and round the price of the tax.
    taxPrice = pretaxPrice * 0.07
    taxPrice = round(taxPrice, 2)

    #Display the price of the tax.
    print("The cost of the tax is",taxPrice,".")

    #Calculate the final price.
    finalPrice = pretaxPrice + taxPrice

    #Display the final price.
    print("The final price is",finalPrice,".")

#Call the above function.
calculateHotDogPrice()
