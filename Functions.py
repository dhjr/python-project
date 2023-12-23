# PROGRAM TO COLLECT USERDATA AND DATA ABOUT ITEMS TO PURCHASE

custInfo = []
billingData = []
grandTotal = 0
totalQty = 0
ModeOfPay = '' 
randomVar = 0
#learning git

def billNo():                                                   # function to generate bill number
    from random import randrange
    global billNo
    billNo = randrange(99999,9999999)
    return billNo

billNo = billNo()

def dateToday():                                                # function to generate the current date
    import datetime
    dt = str(datetime.date.today())
    return dt


def timeNow():                                                  # function to generate the current time
    import datetime
    t = datetime.datetime.now()
    return(str(t.hour)+':'+str(t.minute)+':'+str(t.second))


def addToFile():                                                    # function to add customerdata + product info
                                                                    # to a csv file
    import csv
    global custInfo ,billingData ,grandTotal ,totalQty ,ModeOfPay
    with open('Items.csv' , 'a', newline='') as f:
        csvW = csv.writer(f)
        field1 = ['BILLNO' , 'CUST NAME' , 'PHONE' , 'EMAIL',]
        csvW.writerow(field1)
        csvW.writerow(custInfo)
        field2 = ['ITEM CODE' , 'QTY' , 'PRICE' , 'TOTAL']
        csvW.writerow(field2)
        
        for i in billingData:
            csvW.writerow(i)

        csvW.writerow(['TOTAL QTY' , totalQty])
        csvW.writerow(['GRAND TOTAL',grandTotal])
        csvW.writerow(['MODE OF PAY',ModeOfPay])                


def customerInfo():                                                 # gathers customer data and stores it in a list
    custName = input('Enter the Customer name    : ')
    custPhone = input('Enter the Customer Phone No: ')
    custMail = input('Enter the Customer Mail ID : ')
    global custInfo , billNo
    custInfo =  [billNo , custName , custPhone , custMail]
    print('\nCustomer info successfully entered! \n')


def storeInfo():
    import csv
    with open ('storeData.csv' ,'w+',newline = '') as f:
        fields = ['STORE EMAIL' , 'STORE MANAGER EMAIL' , 'PHONE NO' , 'OPEN FROM' , 'CLOSES' , 'GSTIN']

        storeMail = input('Enter the store email         : ')
        managerMail = input('Enter the store manager mail  : ')
        phone = int(input('Enter the store contact number: '))
        openTime = input('Enter the store opening time  : ')
        closeTime = input('Enter the store closing time  : ')
        GSTIN = input('Enter the GST ID              : ')                         # Supermarket parameters

        global parameterList
        parameterList = [storeMail, managerMail , phone , openTime , closeTime , GSTIN]
    
        w = csv.writer(f)                                                         # Writes to a CSV file for further use
        w.writerow(fields)
        w.writerow(parameterList)

        print('\nStore data has been changed successfully! ')

    
def addItems():                                                             # function to collect and calculate product details
        while True:
            itemCode = input('Enter the item name: ')
            qty = int(input('Enter the quantity : '))
            price = float(input('Enter the price    : '))
            print('\n')
            total = qty * price
            global grandTotal , totalQty
            grandTotal += total
            totalQty += qty
            product = [itemCode , qty , price , total]
            billingData.append(product)

            print('Item successfully added! ')
            userInput = input('Do you want to add more items?(Enter Y/N): ')
            print()
            
            if userInput in['Y','y']:
                pass
            elif userInput in ['N','n']:
                print('Items have successfully been added to bill! ')
                break
            else:
                print('Invalid Input! ')
                break


def deleteItems():                                                  # function to remove items added to inventory
    k = input('Enter the item name to remove from bill: ')
    
    flag = 0
    global totalQty , grandTotal ,billingData
    for i in billingData:
        if k == i[0]:
            n = int(input('Enter the quantity to be removed: '))
            flag = 1
            if n <= int(i[2]):
                i[1] -= n
                totalQty -= n
                i[3] -= (n * float(i[2]))
                grandTotal -= (n * float(i[2]))
                print('Item successfully removed! \n')
                flag = 1
            else:
                print('Quantity to be removed exceeds initally entered value! ')

    if flag == 0:
        print('Item not found! \n')


def clear():                                                        # function to clear all variables                                                                                                                                                      
    global custInfo ,billingData ,grandTotal ,totalQty ,ModeOfPay   # after billing a customer
    custInfo.clear()
    billingData.clear()
    grandTotal = 0
    totalQty = 0
    ModeOfPay = ''


def searchAndDisplay():                                             # function to search and display older entries
    import csv
    clear()
    flag = 0
    searchID = input('Enter the Bill Number: ')    
    with open('Items.csv','r') as f:
        csvRead = csv.reader(f)
        
        for i in csvRead:
            if len(i) == 0:
                print('No entries present!')
                break
            
            if i[0] == searchID:
                custInfo.append(i)
                print('Entry Found!\n ')
                print('BILLNO: ', i[0])
                print('NAME  : ', i[1])
                print('PHONE : ', i[2])
                print('EMAIL : ', i[3])
                print('\n')
                flag = 1
                continue                

            if flag == 1:

                if i[0] == 'TOTAL QTY':
                    print('\nTOTAL QTY  : ', i[1])

                elif i[0] == 'GRAND TOTAL':
                    print('GRAND TOTAL: ' , i[1] , '/-')

                elif i[0] == 'MODE OF PAY':
                    print('MODE OF PAY: ' , i[1])
                    break
                else:
                    print('%-27s % -4s % -7s % -10s' % (i[0], i[1] ,i[2] ,i[3] ))
                    
        else:       
            print('Entry not found! ')

