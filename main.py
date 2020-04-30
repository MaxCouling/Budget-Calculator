#Budget Calculator
#sets the user income as zero and once this code is run it will either be true or false
import os
os.system("clear")
def i_or_e():
  global userincome
  userincome = 0
  while userincome == 0:
    userinput = input("Is this income or an expense\n").upper()# .upper used to reduce error of captilisation 

    if userinput == "E" and "EXPENSE":#if the user wants to input an expense this code will come up
      userincome = False#sets userincome as false, so its a expense
      break#breaks out of the while loop
    elif userinput == "I" and "INCOME":
      userincome = True#sets income as true
      break
    else:#if the user didnt input income or expense this code will run forcing the user to type in it again
      print("Please put in either income or expense\n")#if the user didnt type in either income or expense this error code will


useritem = 0
def imt():#imt, item money time does calulations converting the user inputs
  print("epic")
def banana(e):
  global useritem
  
  if e.upper() == "CHANGE" and "C":
    i_or_e()
  elif e.upper() == "XXX":
    imt()
  else:
    useritem = e
  
#name of item
#amount of money assoated
#time period
running = True
while running:#running program
  #NEED INSTRUCTIONS ON HOW TO USE PROGRAM!!!!!!!!!
  #STUCTURE OF PROGRAM
  #TELL USER HOW TO USE
  print("Hello, welcome to Max's Budget Calculator!\n")
  input("type in 'Change' or 'c'to change your inputs from income to an expense and 'xxx' to exit\nPress enter to continue")
  i_or_e()
  userinput = 0

  if userincome:#user lists incomes
    
    banana(input("what is giving you money"))
    usermoney = input("Amount of money that gets you")#needs to me numbers only
    usertime = input("The time period you gain this money")#has to be weeks month quarter year fortnight
    print(useritem)
  else:#user lists expenses
    
    useritem = input("Name of item")
    usermoney = input("amount of money")
    usertime = input("Timeperiod")






print("Through Succefully")#printing so we know that it went through the code
print(userincome)#debug

