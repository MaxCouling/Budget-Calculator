#Budget Calculator
#sets the user income as zero and once this code is run it will either be true or false
import os
os.system("clear")
def i_or_e():
  global userincome
  userincome = 0
  while userincome == 0:
    userinput = input("Is this income or an expense\n").upper()# .upper used to reduce error of captilisation 

    if userinput == "E" or "EXPENSE":#if the user wants to input an expense this code will come up
      userincome = False#sets userincome as false, so its a expense
      break#breaks out of the while loop
    elif userinput == "I" or "INCOME":
      userincome = True#sets income as true
      break
    else:#if the user didnt input income or expense this code will run forcing the user to type in it again
      print("Please put in either income or expense\n")#if the user didnt type in either income or expense this error code will

  
#name of item
#amount of money assoated
#time period
running = True
while running:#running program
  #NEED INSTRUCTIONS ON HOW TO USE PROGRAM!!!!!!!!!
  #STUCTURE OF PROGRAM
  #TELL USER HOW TO USE
  print("Hello, welcome to Max's Budget Calculator!\n")
  input("'xxx' to exit\nPress enter to continue")
  items = False
  money = False
  time = False
  useritems = []
  while not items:
    os.system("clear")
    
    for x in range(len(useritems)): 
      print (x+1,useritems[x])#lists what user has allready put in
    iteminput = input("What items cause income to your budget?\n")
    
    if iteminput.upper() == "XXX":
      items = True
      break
      break
      
    useritems.append(iteminput)#adds user input to the useritems list

    
    
  break
    
  
  





print("Through Successfully")#printing so we know that it went through the code


