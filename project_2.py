#PROJECT_2 :- SUPER MARKET BILL GENERATION.

print(25*"=","WELCOME TO SUPER MARKET",25*"=")
#Created Date and Time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y || %H:%M:%S")
print("Date and Time :- ",dt_string)

#Details of Customer
name = input("Enter Your Name: ")
mobile_number = int(input("Enter Your Mobile Number: "))

#Declaration
cost = 0
total_cost = 0
final_cost = 0
costlist = []
item_list = []
qnt_list = []
cost_list = []

#Declaration of prices for items
grocery_items ={'rice':25,'wheat':40,'sugar':35,'coffe':57,'tea':48,
'salt':18,
'milk':32,
'oil':117,
'masala':42,
'dal':43,
'onions':22,
'chillies':18,
'eggplant':42,
'occra':22,
'potatoes':45,
'tomatoes':37,
'capcicum':21,
'carrot':54,
'lemons':30,
'mangoes':105,
'apples':125,
'pineapple':43,
'grapes':56,
'oranges':60,
'mosambi':56,
'bananas':25,
'chikku':80} 
a=True
while a:

      print('''
      1.list of items
      2.choose item
      3.exit
             ''')
    
      choice = int(input('enter your choice:'))
      choices =[1,2,3]
      if choice in choices:
         d = grocery_items
         if choice == 1: 
            c=1
            for i,j in d.items():
                print('\t',c,'.',i,'₹',j)
                c+=1
         if choice == 2:
             q =True
             while q:
                print("press 'q' to to see main menu.")
                item = input('enter item:')
                if item in d.keys():
                    qnt = input('enter Quantity:')
                    if qnt.isdigit():
                            
                        qnt = int(qnt)
                        cost = float(d[item]*qnt)
                        costlist.append((item,qnt,cost))
                        total_cost += cost
                        sgst = float(total_cost*5)/100
                        cgst = float(total_cost*3)/100
                        discount = float(total_cost*5)/100
                        final_cost = float(sgst)+(cgst)+(total_cost)-(discount)
                    else:
                         print('Invalid Input Quantity..')
                elif item == 'q':
                        q=False
                else:
                        print('item not present.')

         if choice == 3:
            a = False
      else:  
         print('Invalid Input..Please Enter a valid input.')

bill = input("Generate Bill? ")
if bill == "yes":
   pass 
if total_cost !=0:
    print(28*"=", 'MADHULOKA SUPER MART' ,28*"=")    
    print(31*"-", "TANUKU",31*"-")
    print("NAME: ",name,33*" ","DATE & TIME: ",now.strftime("%d/%m/%Y || %H:%M:%S"))
    print("MOBILE_NUMBER: ",mobile_number)
    print(80*"-")
    print("ITEMS:", 10*" ","QUANTITY:", 10*" ","COST:")
    for j in costlist:
        print(j[0],14*" ",j[1],14*" " ,j[2])
    print(80*"-")
    print(53*" ","TOTAL_AMOUNT: ",total_cost," Rs/-")
    print(80*" ")
    print("SGST_AMOUNT: ", 54*" ", sgst," Rs/-")
    print("CGST_AMOUNT: ", 54*" ", cgst," Rs/-")
    print("DISCOUNT_AMOUNT: ", 51*" ", discount," Rs/-")
    print(80*"-")
    print(53*" ","FINAL_AMOUNT: ", final_cost," Rs/-")
    print(80*"-")
    print(30*" ","THANK YOU VISIT AGAIN")
    print(80*"-")
else:
    print("Hey, You weren't Brought anything...Please Buy something you want.")
       
    
        
    
