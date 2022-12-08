#J&K Recreational center Ticket

print('Welcome to the ticket box')
Height=float(input('\nPlease enter your height in cm:  '))

#First condition
if Height< 120:
    print('\nSorry, you are not eligible to buy ticket')
else: #Other Conditions on age
    Age = int(input('\nPlease enter your age: '))
    if Age > 45:
        print('\nHurray, ticket cost is on the house!')
        Ticket_price = 0.00
    
    elif Age < 12:
        Ticket_price = 5.00
    
    elif Age >= 12 and Age <= 18:
        Ticket_price = 7.00
        
    elif Age > 18 and Age < 45:
        Ticket_price = 10.00
    
#Second Phase - Extra Cost Conditions
    print ('\nWill you take a picture? Yes or No \n\nNote:Taking a picture comes with an additional charge of $3.00')
    picture = input('\n')

    if picture.capitalize() =='Yes':
       Extra_Charge= 3.00
       Total_cost = Ticket_price + Extra_Charge
       print(f'\nTicket cost = ${Ticket_price} \nExtra Charge = ${Extra_Charge} \nTotal Charge = ${Total_cost}')
    
    else:
       Extra_Charge =0.00
       Total_cost = Ticket_price + Extra_Charge
       print(f'\nTicket cost = ${Ticket_price}\nExtra charge = ${Extra_Charge}\nTotal Charge for ride = ${Total_cost}')

    print('\nThank you. Enjoy your time')
    
