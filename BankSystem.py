"""
Created on Mon Nov 13 21:55:59 2023

@author: hp
"""
import csv
from customer_account import CustomerAccount
from admin import Admin


accounts_list = []
admins_list = []


class BankSystem(object):
    def __init__(self):
        self.accounts_list = []       # list to store customer accounts
        self.admins_list = []    # list to store admin accounts
        self.load_bank_data()
        
    def write_accounts_csv(self):
        filename ='customer_account.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'First Name', 'Last Name', 'Number', 'Street', 'City', 'Postal Code', 'Account Number',
                'Balance', 'Account Type', 'Interest Rate', 'Overdraft Limit'
            ])
            for account in self.accounts_list:
                address = account.address                      # Get the address list
                writer.writerow([ 
                    account.fname, account.lname,
                    address[0], address[1], address[2], address[3],
                    account.get_account_no(), account.get_balance(), account.account_type,
                    account.interest_rate, account.overdraft_limit
                ])
            print("CSV file 'customer_account.csv' has been created successfully with customer account data.")
    
    def write_admins_csv(self):
        filename ='admins.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'First Name', 'Last Name', 'Number', 'Street', 'City', 'Postal Code', 'Username', 'Password', 'Full Admin Rights'
            ])
            for admin in self.admins_list:
                address = admin.address                                # Get the address list
                writer.writerow([
                    admin.fname, admin.lname,
                    address[0], address[1], address[2], address[3],
                    admin.get_username(), admin.get_password(), admin.has_full_admin_right()
                ])
            print("CSV file 'admins.csv' has been created successfully with admin account data.")
    
    def load_bank_data(self):
        #Crete Customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, 'business', 0, 500)
        self.accounts_list.append(customer_1)
        
        account_no += 1
        savings_customer = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 600.00, 'saving', 0.05, 0)
        self.accounts_list.append(savings_customer)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Via-duct", "London", "EC1A 2FD"], account_no, 3200.00, 'saving', 0.05, 0)
        self.accounts_list.append(customer_2)
        
        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "CardiganStreet", "Birmingham", "B4 7BD"], account_no, 18000.00, 'saving', 0.05, 0)
        self.accounts_list.append(customer_3)
        
        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "ChurchillWay West", "Basingstoke", "RG21 6YR"], account_no, 40.00, 'business', 0, 500)
        self.accounts_list.append(customer_4)
        
        account_no += 1
        savings_customer = CustomerAccount("Ali", "Abdallah",["44", "ChurchillWay West", "Basingstoke", "RG21 6YR"], account_no, 600.00, 'saving', 0.05, 0)
        self.accounts_list.append(savings_customer)
        
        #CREATE ADMINS
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)
        
        admin_2 = Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)
        
    def search_admins_by_name(self, admin_username):                   #A.2
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
        return found_admin

              
    def search_customers_by_name(self, customer_lname):            #A.3
        found_accounts = [a for a in self.accounts_list if a.get_last_name().lower() == customer_lname.lower()]
        if not found_accounts:
            print("\n No customers with the last name %s found! Try again...\n" % customer_lname)
        return found_accounts
    
    
    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")
    
    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):  #ToDo
        sender_account = None
        receiver_account = None 
        
        for account in self.accounts_list:
            if account.get_last_name().lower() == sender_lname.lower():
                sender_account = account
                break                      #exit the loop when sender is find
                        
        for account in self.accounts_list:
            if account.get_last_name().lower() == receiver_lname.lower():
                if account.get_account_no() == int(receiver_account_no):
                    receiver_account = account
                    break                  # exit the loop when reciver account is find
                
        if sender_account == None:
            print("Sender is not found")
            return
        if receiver_account == None:
            print("Receiver account not found")
            return
        if sender_account.get_balance() < amount:    #to check receiver balance 
            print("Insufficient balance")
            return
        if receiver_account.get_account_no() != int(receiver_account_no):
            print("Reciver account not found")
            return
        sender_account.withdraw(amount)                          #withdraw from sender account
        receiver_account.deposit(amount)                         #deposit into reciver account
        sender_account.add_interest()
        receiver_account.add_interest()                          # Calculate and add interest after the transaction
        print(f"Transfer of {amount} from {sender_account.get_first_name()} {sender_account.get_last_name()} "f"to {receiver_account.get_first_name()} {receiver_account.get_last_name()} is successful")                          
                                                           #successfull transfer
        
    def admin_login(self, username, password):             #A.1
        found_admin = self.search_admins_by_name(username)
        msg = "\nLogin failed"
        if found_admin != None:
           if found_admin.get_password() == password:
              msg = "\n Login successful"
        return msg, found_admin
    
    def calculate_total_interest_payable(self):
        total_interest = sum(account.calculate_interest_payable() for account in self.accounts_list)
        return total_interest
   
    def managment_report(self):
        total_customers = len(self.accounts_list)
        total_money_in_accounts = sum(account.get_balance() for account in self.accounts_list)
        total_interest_payable = sum(account.calculate_interest_payable() for account in self.accounts_list)
        total_overdrafts = sum(account.overdraft_limit for account in self.accounts_list if account.overdraft_limit > 0)
        print("Management Report:")
        print(f"Total number of customers in the system: {total_customers}")
        print(f"Total money in customers' accounts: {total_money_in_accounts}")
        print(f"Total interest payable to all accounts for one year: {total_interest_payable}")
        print(f"Total amount of overdrafts currently taken by all customers: {total_overdrafts}")
    
    
    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Admin account profile setting")
         print ("6) Managment Report")
         print ("7) Sign Out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option
    
    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount) 
                   
            elif choice == 2:                       #A.4
               customer_name = input("\n Please input customer surname : ")
               customer_accounts = self.search_customers_by_name(customer_name)  
               if customer_accounts:
                   for customer_account in customer_accounts:
                       customer_account.run_account_options()
                       self.write_accounts_csv()  # Update CSV file after 
               else:
                   print("\nNo customers with the provided surname found.")
            
            elif choice == 3:   #Todo # Remove customer account
                if admin_obj.has_full_admin_right():
                    account_number = input("\n Please input account number to delete: ")
                    account_to_delete = None
                    for account in self.accounts_list:
                        if str(account.get_account_no()) == account_number:
                            account_to_delete = account
                            break
                    if account_to_delete:
                        self.accounts_list.remove(account_to_delete)
                        print(f"\nAccount with account number '{account_number}' deleted successfully.")
                        self.write_accounts_csv()  # Update CSV file
                    else:
                        print("\nNo account found with the provided account number.")
                else:
                    print("\nInsufficient rights to delete customer accounts.")
                    
                         
            elif choice == 4:           #Todo
                self.print_all_accounts_details()
                
            elif choice == 5:
                admin_username = input("\n Please input admin username:\n")
                found_admin = self.search_admins_by_name(admin_username)
                if found_admin:
                    new_fname = input("Enter new first name: ")
                    new_lname = input("Enter new last name: ")
                    new_address = input("Enter new address:")
        
                    found_admin.update_first_name(new_fname)
                    found_admin.update_last_name(new_lname)
                    found_admin.update_address_name(new_address)
                    print("Admin profile updated successfully.")
                else:
                    print("Admin not found.")
                    
            elif choice == 6:
                self.managment_report()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")
        
    def print_all_accounts_details(self):
                # list related operation - move to main.py
                i = 0
                for c in self.accounts_list:
                    i+=1
                    print('\n %d. ' %i, end = ' ')
                    c.print_details()
                    print("------------------------")
                    
app = BankSystem()
app.write_accounts_csv()  # Generate the CSV file for accounts
app.write_admins_csv()  # Generate the CSV file for admins
app.run_main_options()        
            



    
