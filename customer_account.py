# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:01:39 2023

@author: hp
"""

class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type, interest_rate, overdraft_limit=0):
          self.fname = fname
          self.lname = lname
          self.address = address
          self.account_no = account_no
          self.balance = float(balance)
          self.account_type = account_type
          self.interest_rate = interest_rate
          self.overdraft_limit = 0     # Initialize overdraft limit for non-business accounts
          
          if account_type == 'business':
              self.overdraft_limit = 500  # Set the overdraft limit for business accounts
          elif self.account_type == 'saving':
              self.overdraft_limit = 0    #
              
                  
    def update_first_name(self, fname):
        self.fname = fname
        
    def update_last_name(self, lname):
        self.lname = lname
        
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
    
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
             
    
    def deposit(self, amount):
        self.balance += amount  
        self.add_interest()     # Calculate and add interest after every deposit
        
    def withdraw(self, amount):  #ToDo
        if self.account_type == 'saving':
            if amount > self.balance:
                print("Withdrawal amount exceeds available balance")
            else:
                self.balance -= amount
                self.add_interest()    # Calculate and add interest after every withdrawal
        elif self.account_type == 'business':
            if amount > self.balance + self.overdraft_limit:
                print("Withdrawal amount exceeds overdraft limit")
            else:
                self.balance -= amount
                self.add_interest()
        else:
            print("Invalid account type")
            
    def add_interest(self):
            interest_amount= self.balance * self.interest_rate
            self.balance += interest_amount 
            
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def set_account_type(self, account_type):
        self.account_type = account_type
        
    def calculate_interest_payable(self):
        interest_rate = 0.05   #5%interest rate 
        if self.account_type == 'business':
            interest_rate = 0.06  # Business account interest rate
        elif self.account_type == 'saving':
            interest_rate = 0.04  # Saving account interest rate
        time_period = 1  # Assuming interest is calculated for one year
        interest_payable = self.balance * interest_rate * time_period
        return interest_payable
    
    
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):                               #STEP A.4.3
         print("First name: %s" %self.fname)
         print("Last name: %s" %self.lname)
         print("Account No: %s" %self.account_no)
         print("Address: %s" %self.address[0])
         print(" %s" %self.address[1])
         print(" %s" %self.address[2])
         print(" %s" %self.address[3])
         print("Account Type: %s" % self.account_type)
         print("Balance: %.2f" % self.balance)
         print(" ")
         

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:                                   #STEP A.4.1
               amount = float(input("\n Please enter amount to be deposited: "))
               self.deposit(amount)
               self.print_balance()
               
               
            elif choice == 2:
            #ToDo
             amount = float(input("\n Please enter amount to be withdrawn: "))
             self.withdraw(amount)
             self.print_balance()
             
            elif choice == 3: 
               fname=input("\n Enter customer last name: ")
               self.print_balance()                #STEP A.4.4
               
               
         
            elif choice == 4:                                           #STEP A.4.2
               fname=input("\n Enter new customer first name: ")
               self.update_first_name(fname)
               sname = input("\nEnter new customer last name: \n")  
               self.update_last_name(sname) 
               self.print_details()  
               
                                                    
             
            elif choice == 5:   #ToDo
               address=input("Enter new address: ")
               self.update_address(addr) 
               
           
            elif choice == 6:
               self.print_details()
               
            elif choice == 7:
             loop = 0
        print ("\n Exit account operations")
        
    
