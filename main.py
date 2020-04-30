#Budget Calculator
userincome = 0 #sets the user income as zero and once this code is run it will either be true or false


while userincome == 0:
  userinput = input("Is this income or an expense\n").upper()# .upper used to reduce error of captilisation 

  if userinput == "E" and "EXPENSE":#if the user wants to input an expense this code will come up
    userincome = False#sets userincome as false, so its a expense
    break#breaks out of the while loop
  elif userinput == "I" and "INCOME":
    userincome = True#sets as 
    break
  else:#if the user didnt input income or expense this code will run forcing the user to type in it again
    print("Please put in either income or expense\n")#if the user didnt type in either income or expense this error code will

print("Through Succefully")#printing so we know that it went through the code
print(userincome)#debug
print(userinput)#debug
