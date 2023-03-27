#PYTHON PROJECT: Waiter-less Management Restaurant App
print("\n" * 5) 

import datetime 

import time 

import os 

import mysql.connector as ms 

a=ms.connect(host='localhost', user='root', 

        password='root', database='Project') 

amt=0 

list_foods = [] 

c=a.cursor() 

def made_by(): 

    msg = '''  

            Waiterless Restaurant app made by     : Divyaansh Vats, Joshua Maries C and Yashwanth P 

            School Name                                 : Kensri School 

            Session                                     : 2021-22 

             

             

        ''' 

 

    for x in msg: 

        print(x, end='') 

        time.sleep(0.002) 

made_by() 

def def_main(): 

    while True:                                             

        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"      

              "\t(O) ORDER\n"                               

              "\t(P) PAYMENT\n" 

              "\t(E) EXIT\n" + 

              "_" * 72) 

 

        input_1 = str(input("Please Select Your Operation: ")).upper()     

        if (len(input_1) == 1):                                            

            if (input_1 == 'O'):                                           

                print("\n" * 10)                                          

                def_order_menu()                                          

                break                                                     

            elif (input_1 == 'P'):                                        

                print("\n" * 10)                                          

                def_payment()                                              

                break                                                      

            elif (input_1 == 'E'):                                         

                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")            

                break                                                      

            else:                                                                                  

                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")      

        else:                                                                                      

            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")          

 

def def_order_menu():                                                                                

    while True:                                              

        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"      

              "\t(F) FOODS\n" 

              "\t(M) MAIN MENU\n" 

              "\t(E) EXIT\n" + 

              "_" * 72) 

 

        input_1 = str(input("Please Select Your Operation: ")).upper()  

        if len(input_1) == 1: 

            if (input_1 == 'F'):   

                print("\n" * 10) 

                def_food_order()  

                break 

            elif (input_1 == 'M'): 

                print("\n" * 10) 

                def_main()  

                break 

            elif (input_1 == 'E'): 

                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 

                break 

            else: 

                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  

        else: 

            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 

 

def connect(): 

    c.execute("select itemname, price, type from items") 

    for i in c: 

      list_foods.append(str(i)) 

connect()     

def def_food_order(): 

    while True: 

            print("*" * 26 + "ORDER FOODS" + "*" * 26) 

            print(" |NO| |FOOD NAME|  |PRICE|   |TYPE|") 

 

            i = 0 

            while i < len(list_foods): 

                var_space = 1 

                if i <= 8:                       

                    var_space = 2 

 

                if i < len(list_foods): 

                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | "  

                else: 

                    food = " " * 36 + "| "  

                print(food) 

                i += 1 

 

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72) 

 

            input_1 = input("Please Select Your Operation: ").upper()  

            if (input_1 == 'M'): 

                print("\n" * 10) 

                def_main()  

                break 

            if (input_1 == 'E'): 

                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  

                break 

            if (input_1 == 'P'): 

                print("\n" * 10) 

                def_payment()  

                break 

            try:         

                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)): 

                     try: 

                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1]))  

                     except: 

                        pass 

                      

                     input_2 = input("How Many do you want to Order?: ").upper()  

                     if int(input_2) > 0: 

                        global amt 

                        e=list_foods[int(input_1)-1] 

                        e=eval(e) 

                        amt=int(amt)+((e[1])*int(input_2)) 

                        print("\n" * 10) 

                        print("Successfully Ordered!") 

                        def_food_order() 

                        break 

                     else: 

                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!") 

            except: 

                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 

 

def def_payment(): 

    print("Your total amount to be paid is", amt) 

    print("Which payment method would you like to use?") 

    print("1.Cash \n2.Credit/Debit Card  \n3.Net Banking  \n4.UPI") 

    p=int(input("Enter your choice:")) 

    if (p==1 or p==2 or p==3 or p==4): 

          print("Order successfully placed") 

    else: 

        print("Invalid Input. Please try again.") 

     

def_main() 
