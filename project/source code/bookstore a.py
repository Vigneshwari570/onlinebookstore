"""
import platform

import os

def myclear():

   if platform.system()=="Windows": 
print(os.system("cls"))

def intromain():

  myclear()
 print("**BOOKS**MANAGEMENT* SYSTEM***PROJECT******")

print("******************") 

def intro():

print("********BOOKS MANAGEMENT****") 
print("===========================================") 
Print("*****S=Y=S=T=E=M******") 

print("PROJECT:")

print("MADE BY:................... ") 

Print("------------------..................-------------------")

def main():

ch=0

myclear()

intromain()

print("============MAIN MENU=============") 

print("01. BOOKS REPORT GENERATOR")

print("02. ADMINISTRATOR")

print("03. EXIT")

print("==========BOOKS INFO MENU =========") 

ch=int(input("Please Select Your Option (1-3)"))

return ch

def book_menu():

ch=0

intromain()

print("===========BOOKS INFO MENU=========") 

print("01. ADD BOOKS INFORMATION")

print("02. MODIFY BOOKS INFORMATION")

print("03. DELETE BOOKS INFORMATION")

print("04. BACK TO MAIN")
print("=======================================") 

ch-int(input("Please Select Your Option (1-4)")) 
return ch
"""********************
ADMINSTRATOR BOOKS FUNCTION
*******************"""

def admin_menu1():

  ch=0

  myclear()

   intromain()

          print("=============BOOKS ADD MENU============") 

print("1.CREATE BOOKS DETAILS")

print("2.DISPLAY ALL BOOKS DETAILS") 

print("3.SEARCH RECORD BY BOOKID")

print("4,SEARCH RECORD BY BOOK TITLE")

print("5.SEARCH RECORD BY PRICE")

print("6.SEARCH RECORD BY TYPE")

print("7.SEARCH RECORD BY PUBLISHER")

print("8.BACK TO MAIN MENU") 
ch=int(input("Please Enter Your Choice (1-8)"))

return ch
"""*******************
ADMINSTRATOR BOOKS MAIN MENU FUNCTION
********************"""

def BOOKS_menu():

ch=0

myclear()

intromain()

print("===================

ADMIN MENU===========""") 

print("1.BOOK'S MENU")

print("2.BOOKS SALE/PURCHASE")

print("3.BACK TO MAIN MENU")

ch=int(input("Please Enter Your Choice (1-3)"))

return ch
"""********************
MODIFY MENU

********************"""

def modifyBOOKS_menu():

  ch=0

  myclear()

  intromain()

  print("===================MODIFY MENU================""") 

print("1.MODIFY TITLE")

print("2.MODIFY PRICE")

print("3.MODIFY QUANTITY")

print("4.MODIFY ISBN")
print("5.MODIFY PUBLISHER")

print("6.MODIFY CATEGORY") 

print("7.BACK TO MAIN MENU")

ch=int(input("Please Enter Your Choice (1-7)"))

return ch


