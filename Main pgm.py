# MAIN PROGRAM
import Functions
while True:                                                 # User Interaction Menu
    print('\nＤＡＹ２ＤＡＹ  ＢＩＬＬ  ＰＯＲＴＡＬ')
    print('▂' * 20 ,end = '\n\n')

    func = input('''
┌────────────────────────────────────┐
│MAIN MENU			     │
├────────────────────────────────────┤
│1. CUSTOMER		             │
│2. INVENTORY                        │
│3. BILLING	                     │
│4. SEARCH	                     │
│5. ADMIN		             │
│6. EXIT		             │
│		                     │
└────────────────────────────────────┘
 ❯ ''')   
    print()
   
    if func == '1':
        while True:
            func1 = input('''
┌────────────────────────────────────┐
│MAIN MENU\CUSTOMER		     │
├────────────────────────────────────┤
│1. ADD A NEW CUSTOMER	             │
│2. MODIFY CUSTOMER DATA             │
│3. DELETE CUSTOMER                  │
│4. GO BACK                          │
│                                    │
└────────────────────────────────────┘
 ❯ ''')                                          # is called from Functions module
            if func1 == '1':
                Functions.customerInfo()                         # function named customerInfo()[To enter customer info] 
                print()

            elif func1 == '2':
                if len(Functions.custInfo) == 0:
                    print('Nothing to change! Please add a new customer first! ')

                else:
                    while True:
                        func2 = input('''
┌────────────────────────────────────┐
│..CUSTOMER\CHANGE CUSTOMER DATA     │
├────────────────────────────────────┤
│1. CHANGE NAME	                     │
│2. CHANGE PHONE NO                  │
│3. CHANGE EMAIL ID                  │
│4. GO BACK                          │
│                                    │
└────────────────────────────────────┘
 ❯ ''') 

            
                        if func2 == '1':
                            Functions.custInfo[1] = input('Enter New Name: ')
                            print('Name changed successfully! ')
                        elif func2 == '2':   
                            Functions.custInfo[2] = input('Enter New Phone No: ')
                            print('Phone No changed successfully! ')
                        elif func2 == '3':
                            Functions.custInfo[3] = input('Enter New Email ID: ')
                            print('Email ID changed successfully! ')
                        elif func2 == '4':
                            break
                        else:
                            print('Invalid Input! ')

            elif func1 == '3':
                Functions.custInfo.clear()
                print('Customer data successfully deleted! ')

            elif func1 == '4':
                break
            else:
                print('Invalid Input! ')
    
        
    elif func == '2':
        while True:
            func3 = input('''
┌────────────────────────────────────┐
│MAIN MENU\INVENTORY		     │
├────────────────────────────────────┤
│1. ADD ITEMS		             │
│2. REMOVE ITEMS	             │
│3. VIEW INVENTORY                   │
│4. CLEAR ALL	                     │
│5. GO BACK		             │
│		                     │
└────────────────────────────────────┘
 ❯ ''')
            if func3 == '1':
                Functions.addItems()                          # function named addItems[to add products] 
                print()
        
            elif func3 =='2':
                if len(Functions.billingData) != 0:                
                    Functions.deleteItems()
                else:
                 print('Nothing to remove. Please add items to inventory first! ' , end = '\n\n')

            elif func3 =='3':
                if len(Functions.billingData) == 0:
                    print('Nothing added to inventory! ')
                else:
                    print('%-20s %-5s %-10s %-10s' % ('ITEM NAME' , 'QTY' , 'PRICE' , 'TOTAL'))
                    for i in Functions.billingData:
                        print('%-20s %-5d %-10d %-10d' % (i[0], i[1] , i[2], i[3]))

            elif func3 =='4':
                Functions.billingData.clear()
                print('Inventory successfully cleared!')

            elif func3 == '5':
                break

            else:
                print('Invalid Input! ')
      
    
    elif func == '3':
        while True:
            func4 = input('''
┌────────────────────────────────────┐
│MAIN MENU\BILLING		     │
├────────────────────────────────────┤
│1. VIEW INVENTORY	             │
│2. GENERATE BILL	             │
│3. GO BACK	                     │
│		                     │
└────────────────────────────────────┘
 ❯ ''')
    
            if func4 == '1':
                if len(Functions.billingData) == 0:
                    print('Nothing added to inventory! ')
                else:
                    print('%-20s %-5s %-10s %-10s' % ('ITEM NAME' , 'QTY' , 'PRICE' , 'TOTAL'))
                    for i in Functions.billingData:
                        print('%-20s %-5d %-10d %-10d' % (i[0], i[1] , i[2], i[3]))

            elif func4 == '2':

                if any(Functions.billingData)  and any(Functions.custInfo):
                    Functions.ModeOfPay = input('Enter the mode of payment: ')
                    inp = input('Confirm to bill?(Enter Y/N):')
                    if inp in 'Yy':
                
                                
                        Functions.addToFile()
                        if len(Functions.billingData) != 0:
                            from billGenerator import *
                            storeData()
                            custData()
                            billingItems()
                        Functions.clear()
            
                    else:
                        pass

                elif len(Functions.custInfo) == 0:
                    print('Customer data not found ! ')
                else:
                    print('Nothing to bill ! ')
                print()

            elif func4 == '3':
                break



    elif func == '4':
        Functions.searchAndDisplay()

    elif func == '5':
        userName = 'Username'
        passWord = '12345678'
        while True:
            uInput = input('Username: ')
            pInput = input('Password: ')
            flag1 = 0

            if uInput == userName and pInput == passWord:
                while True:
                    func5 = input('''
┌────────────────────────────────────┐
│MAIN MENU\ADMIN		     │
├────────────────────────────────────┤
│1. MODIFY SUPERMARKET DATA          │
│2. CHANGE USERNAME	             │
│3. CHANGE PASSWORD                  │
│4. GO BACK                          │
│		                     │
└────────────────────────────────────┘
 ❯ ''')
                    if func5 == '1':
                        Functions.storeInfo()
                        print()

                    elif func5 == '2':
                        userName = input('Enter New Username: ')
                    elif func5 == '3':
                        passWord = input('Enter New Password: ')
                    elif func5 == '4':
                        flag1 = 1
                        break
                        
                    else:
                        print('Invalid Input! ')
                    
            elif uInput != userName or pInput != passWord:
                print('Incorrect Username and/or Password. Please try again! ')
                break

            if flag1 == 1:
                break
        
    elif func == '6':                                     # closing command
        print('Successfully Exited!\n')
        exit()

    else:                                                 # Invalid Input
        print('Invalid Input! \n')
