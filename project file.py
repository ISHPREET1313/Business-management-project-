# Importint Required libraries
import pandas as pd
import matplotlib.pyplot as plt

#Creation of Required Dataframe
Storage=pd.DataFrame(columns=['Invoice No.','Customer_Name','Detailed invoice','total amount'])
customer=pd.DataFrame(columns=['Cust_Id',"Cust_Name","Phone_No"])
products=pd.DataFrame(columns=['Product_Id','Product_Name','Price','Inventory'])
YourDetails=pd.DataFrame(columns=['Name',"GST No",'MIN_Inventory'])

#Sample Data
dataC={'Cust_Id':['1','2','3','4','5'],'Cust_Name':['Sanjay Batra','Arjun Mehta','Amit Sood','Karan Sharma','Radhika Desai'],
      'Phone_No':['+91 98765 43210','+91 99876 54321','+91 98765 67890','+91 99887 65432','+91 98765 12345']}
dataP={'Product_Id':['1','2'],'Product_Name':['Cycle','Scooter'],'Price':[7000,3500],'Inventory':[15,25]}
dataY={'Name':['Ishpreet'],'GST No.':['27ABCDE1234F1Z5'],'MIN_Inventory':[7]}

#Putting Sample data in datframes
customer=pd.DataFrame(dataC)
products=pd.DataFrame(dataP)
YourDetails=pd.DataFrame(dataY)

# Main loop in while loop which runs infinitely unless exited
while True:
    print()
    print('\t\t\t Management System')
    print()
    print('What can I help YOU with:')
    print("1. Customers")
    print("2. Products and Inventory")
    print("3. Invoice")
    print("4. Trends")
    print("5. Your Details")
    print("6. Exit")

    #Giving alert for Low Inventory
    for x in products['Product_Name']:
        if int(products.loc[products['Product_Name']==x,'Inventory'].values[0])<int(YourDetails['MIN_Inventory'].values[0]):
            print()
            print('Low Inventory of : ', x)
            print()

    print()
    choice=input("Enter your Choice(1-6):")
    print()

    if choice=='1':
        print("(a) Add customer")
        print("(b) View customers")
        print("(c) Update customer details")
        print("(d) delete customer")
        print("(e) Exit")
        print()
        choice1=input("Enter your Choice(a-e):")
        print()
        if choice1=='a':
           rows=len(customer)
           print("Add your "+str(rows+1)+"th Customer")
           Id=int(input('Enter Cust_Id:'))
           Name=input('Enter Cust_Name:')
           phoneNo=input('Enter Phone_No:')
           customer.loc[rows]=[Id,Name,phoneNo]
           print()
           print('New customer added')
           print()
           print(customer)
           
        elif choice1=='b':
            print(customer)
            
        elif choice1=='c':
            NameUpdate=input('Enter Name of customer whose details you want to update:')
            print()
            print("(a) Customer Id")
            print("(b) Customer Name")
            print("(c) Phone Number")
            print()
            choice2=input('Enter your choice(a-c):')
            print()
            if choice2=='a':
                new_Detail=input('What you want it to be:')
                customer.loc[customer['Cust_Name'] == NameUpdate,'Cust_Id']= new_Detail
                print()
                print('Updated')
                print()
                print(customer)
                
            elif choice2=='b':
                new_Detail=input('What you want it to be:')
                customer.loc[customer['Cust_Name'] == NameUpdate,'Cust_Name']= new_Detail
                print()
                print('Updated')
                print()
                print(customer)
                
            elif choice2=='c':
                new_Detail=input('What you want it to be:')
                customer.loc[customer['Cust_Name'] == NameUpdate,'Phone_No']= new_Detail
                print()
                print('Updated')
                print()
                print(customer)
            else:
                print('Wrong Input')
                print()
                print('Back to main menu')
                
        elif choice1=='d':
            NameUpdate1=input('Enter Name of customer whose details you want to delete:')
            print()
            if NameUpdate1 in customer['Cust_Name'].values:
                index1=customer[customer['Cust_Name']==NameUpdate1].index
                customer.drop(index1,inplace=True)
                print('Deleted')
                print()
                print(customer)
            else:
                print('Customer not found')
                print()
                print(customer)
            
        elif choice1=='e':
            print('back to main menu')

        else:
            print('not correct input')
            print()
            print('back to main menu')
    
    elif choice=='2':

        # Data Related To Products

        print("(a) View Products and Inventory")
        print('(b) Update Products and Inventory')
        print('(c) Add Product')
        print('(d) Delete Product')
        print("(e) Exit")
        print()
        choice3=input("Enter your Choice(a-e):")
        print()

        if choice3=='a':

            # View Products

            print()
            print(products)

        elif choice3=='b':

            # Update Products Details

            NameUpdate=input('Enter Name of Product whose details you want to update:')
            print()
            print("(a) Product Id")
            print("(b) Product Name")
            print("(c) Price")
            print("(d) Inventory")
            print()
            choice4=input('Enter your choice(a-d):')
            print()
            if choice4=='a':
                new_Detail=input('What you want it to be:')
                products.loc[products['Product_Name'] == NameUpdate,'Product_Id']= new_Detail
                print()
                print('Updated')
                print()
                print(products)
                
            elif choice4=='b':
                new_Detail=input('What you want it to be:')
                products.loc[products['Product_Name'] == NameUpdate,'Product_Name']= new_Detail
                print()
                print('Updated')
                print()
                print(products)
                
            elif choice4=='c':
                new_Detail=input('What you want it to be:')
                products.loc[products['Product_Name'] == NameUpdate,'Price']= new_Detail
                print()
                print('Updated')
                print()
                print(products)
            
            elif choice4=='d':
                new_Detail=input('What you want it to be:')
                products.loc[products['Product_Name'] == NameUpdate,'Price']= new_Detail
                print()
                print('Updated')
                print()
                print(products)
            
            else:
                print('Wrong Input')
                print()
                print('Back to main menu')
        
        elif choice3=='c':

            # adding Products

            rows1=len(products)
            print("Add your "+str(rows1+1)+"th Customer")
            Id=int(input('Enter Product_Id:'))
            Name=input('Enter Product_Name:')
            price=input('Enter Price:')
            inventory=input('Enter Inventory:')
            products.loc[rows1]=[Id,Name,price,inventory]
            print()
            print('New product added')
            print()
            print(products)
        
        elif choice3=='d':

            # Deleting Products

            NameUpdate2=input('Enter Name of Product whose you want to delete:')
            print()
            if NameUpdate2 in products['Product_Name'].values:
                index3=products[products['Product_Name']==NameUpdate2].index
                products.drop(index3,inplace=True)
                print('Deleted')
                print()
                print(products)
            else:
                print('Product not found')
                print()
                print(products)
        
        elif choice3=='e':
            print('back to main menu')
        
        else:
            print('Wrong Input')
            print()
            print('Back to main menu')

    elif choice=='3':
        
        # here Generating and viewing Previous Invoices

        print('(a) Generate')
        print('(b) Records')
        print()
        choice8=input('Enter your choice(a-b):')
        print()

        if choice8=='a':

            # Generating Invoice

            CustomerName=input(('Enter Customer Name:'))
            choice5=int(input("How many products want to add (GIVE NO. of UNIQUE products):"))
            if CustomerName in customer['Cust_Name'].values:
                invoice =pd.DataFrame(columns=['Product Name','Price','Qty','Total Price'])
                for x in range(choice5):
                    print('Add your '+str(x+1)+'th Product')
                    Pro_Name=input('Enter Product Name:')
                    if Pro_Name in products['Product_Name'].values:
                        index2=products[products['Product_Name']==Pro_Name].index[0]
                        Pro_Qty=int(input('Enter Product Quantity:'))
                        Pro_Price = products.loc[index2,'Price']
                        Pro_Total=Pro_Price*Pro_Qty
                        invoice.loc[x]=[Pro_Name,Pro_Price,Pro_Qty,Pro_Total]
                    else:
                        print('Prouct Not FOUND')
                        break
                invoice.index=range(1,choice5+1)
                df_str = invoice.to_string(index=True)
                print()
                print()
                print("\t\t\t\t\t INVOICE")
                print()
                your_gst_no=YourDetails.loc[0,'GST No.']
                print("\t\t\tGST NO. :",your_gst_no)
                print("\t\t\t_____________________________________")
                print()
                print('\t\t\tCustomer Name : ',CustomerName)
                print()
                for line in df_str.split('\n'):
                    print("\t\t\t" + line)
                print('\t\t\t')
                print()
                total_amount=invoice['Total Price'].sum()
                print('\t\t\t\tYour Total amount is :',total_amount)
                print()

                # Saving invoice For further use

                index4=len(Storage)
                print('Add your '+str(index4+1)+"th Invoice as record")
                Id=input('Enter Invoice Id(like I00001):')
                directory = 'C://Users//INTEL//Desktop//storage'
                file_name = str(Id) + '.csv'
                file_path = directory + '//' + file_name 
                invoice.to_csv(file_path, sep=',', index=True)
                Storage.loc[index4]=[Id,CustomerName,file_path,total_amount]

                
                # Removing Products from Inventory
                for x in invoice['Product Name'].values:
                    UsedP=int(invoice.loc[invoice['Product Name']==x,'Qty'].values[0])
                    products.loc[products['Product_Name']==x,'Inventory'] -= UsedP
                print()
                print('Inventory Decreased')
                print()
                invoice=pd.DataFrame()

            else:
                print('Customer Not FOUND')
        
        elif choice8=='b':

            # Viewing Previous Records

            print('(a) View Total invoices')
            print('(b) Detailed invoice also')
            print()
            choice9=input('Enter Choice(a-b):')
            print()
            if choice9=='a':
                print(Storage)
            elif choice9=='b':
                print(Storage)
                print()
                InvoiceNo=input('Enter Invoice No. whose you want detailed invoice:')
                file_url = Storage.loc[Storage['Invoice No.']==InvoiceNo, 'Detailed invoice'].values[0]
                df_from_url = pd.read_csv(file_url)
                print(df_from_url)
            else:
                print('Wrong Input')
                print()
                print('Back to main menu')

        else:
           print('Wrong Input')
           print()
           print('Back to main menu')
    
    elif choice=='4':

        # Making Graphs to visualize

        print('(a) Customer Trends')
        print('(b) Product Sales (Bar graph)')

        print()
        choice10=input('Enter Your Choice(a-b):')
        print()

        if choice10=='a':
            print('(a) Customer Frequency(Bar Graph)')
            print('(b) Customer total amount trend (Bar Grap)')
            print()
            choice11=input('Enter Your Choice(a-b):')
            print()
            df2 = []
            df3 = []
            for x in Storage['Invoice No.'].values:
                Custname = Storage.loc[Storage['Invoice No.'] == x, 'Customer_Name'].values[0]
                Custamount = int(Storage.loc[Storage['Invoice No.'] == x, 'total amount'].values[0])
                df2.append(Custname)
                df3.append(Custamount)
            Cust_Sales = pd.DataFrame({'Customer_Name': df2, 'total amount': df3})
            result = Cust_Sales.groupby('Customer_Name').agg(count=('Customer_Name', 'size'),total_amount=('total amount', 'sum')).reset_index()
            if choice11=='a':
                plt.bar(result['Customer_Name'],result['count'],color='blue')
                plt.title('Customer Frequency Count')
                plt.xlabel('Customers')
                plt.ylabel('Count')
                plt.yticks(result['count'])
                plt.show()
            elif choice11=='b':
                plt.bar(result['Customer_Name'],result['total_amount'],color='blue')
                plt.title('Customer V/S Total Amount ')
                plt.xlabel('Customers')
                plt.ylabel('Total Amount')
                plt.yticks(result['total_amount'])
                plt.show()
            else:
                print('not correct input')
                print()
                print('back to main menu')


        elif choice10=='b':
            Pro_Sales=pd.DataFrame(columns=['Product Name','Qty'])
            df1=[]
            df4=[]
            for x in Storage['Invoice No.'].values:
                file_url = Storage.loc[Storage['Invoice No.']==x, 'Detailed invoice'].values[0]
                df_from_url = pd.read_csv(file_url)
                df1.extend(df_from_url["Product Name"].values)
                df4.extend(df_from_url['Qty'].values)
            Pro_Sales = pd.DataFrame({'Product Name': df1, 'Qty': df4})
            result1 = Pro_Sales.groupby('Product Name').agg(total_qty=('Qty', 'sum')).reset_index()
            plt.bar(result1['Product Name'],result1['total_qty'],color='green')
            plt.title('Product Frequency Count')
            plt.xlabel('Products')
            plt.ylabel('Count')
            plt.yticks(result1['total_qty'])
            plt.show()

        else:
            print('not correct input')
            print()
            print('back to main menu')

    elif choice=='5':
       
        #Here User details
       
        print("(a) Add")
        print("(b) View")
        print('(c) Update')
        print("(d) Exit")
        
        print()
        choice6=input('Enter your choice(a-d):')
        print()

        if choice6=='a':
            
            #Add User details (for First time)
            
            Name=input('Enter Name:')
            gstNo=input('Enter Gst No.:')
            minInventory=input('Enter Minimum Inventory limit at which you want alert:')
            YourDetails.loc[0]=[Name,gstNo,minInventory]
            print()
            print('Details added')
            print()
            print(YourDetails)

        elif choice6=='b':
           
            # View Your Details
            
            print(YourDetails)

        elif choice6=='c':
            
            # Updating Your details

            print('Enter details which you want to update:')
            print()
            print("(a) Name")
            print("(b) GST No.")
            print('(c) Minimum Inventory')
            print()
            choice7=input('Enter your choice(a-c):')
            print()

            if choice7=='a':
                new_Detail1=input('What you want it to be:')
                YourDetails.loc[0,'Name']= new_Detail1
                print()
                print('Updated')
                print()
                print(YourDetails)
                
            elif choice7=='b':
                new_Detail1=input('What you want it to be:')
                YourDetails.loc[0,'GST No.']= new_Detail1
                print()
                print('Updated')
                print()
                print(YourDetails)

            elif choice7=='c':
                new_Detail1=input('What you want it to be:')
                YourDetails.loc[0,'MIN_Inventory']= new_Detail1
                print()
                print('Updated')
                print()
                print(YourDetails)
                   
            else:
                print('Wrong Input')
                print()
                print('Back to main menu')
        
        elif choice6=='d':
            print('back to main menu')

        else:
            print('Wrong Input')
            print()
            print('Back to main menu')

    elif choice=='6':
        
        #Using this to exit so breaking the loop
        
        print('\t\t\t Exiting the System')
        print()
        break

    else:
       
        #if anything else typed then this give ouput and takes back to main interface
        
        print('Wrong Input')
        print()
        print('Please write b/w 1-6')
        print()
        print('back to main menu')
        print()