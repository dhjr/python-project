# PROGRAM TO GENERATE BILL FOR A CUSTOMER

def storeData():                                                # function to print the store logo & data neatly
    import csv
    with open('logo\logo.txt' , 'r') as g:
        print(g.read())

    with open('storeData.csv' , 'r') as f:
        readerObj = csv.reader(f)
        skipHeader = next(f)
        print()

        for i in readerObj:
            print('STORE EMAIL: ' , i[0] , end = '\t\t')
            print('MANAGER EMAIL: ' , i[1])
            print('PHONE NO   : ' , i[2] , end = '\t\t')
            print('WORKING HOURS: ' , i[3] , 'TO' , i[4] )
            print('GSTIN      : ' , i[5])

    
def custData():                                                 # function to print the customer data neatly
    import Functions
    print()
    print('BILL NO    : ' , Functions.billNo , end = '\t\t\t')
    print('CUSTOMER NAME: ' , Functions.custInfo[1])
    print('DATE       : ' , Functions.dateToday() , end = '\t\t')
    print('PHONE        : ' , Functions.custInfo[2])
    print('TIME       : ' , Functions.timeNow() , end = '\t\t\t')
    print('EMAIL ID     : ' , Functions.custInfo[3])


def billingItems():                                             # function to print the purchased products
    import Functions                                            # and its corresponding data neatly
    print('-' * 80)
    print('%-27s %-4s %-7s %-10s' % ('ITEM CODE', 'QTY', 'PRICE', 'TOTAL'))
    print('-' * 80)
        
    for i in Functions.billingData:
        print('%-27s % -4s % -7s % -10s' % (i[0], i[1] ,i[2] ,i[3]))
    print('-' * 80)
    print('TOTAL QTY      : ' , Functions.totalQty)
    print('GRAND TOTAL    : ' , Functions.grandTotal,'/-')
    print('MODE OF PAYMENT: ' , Functions.ModeOfPay)
    print('-' * 80)
    print('\nThank you for shopping with us.We look forward to serving you again in the future! :) ')
    
