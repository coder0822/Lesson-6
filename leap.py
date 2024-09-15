print(ord('#'))
print(ord('$'))
print(ord('R'))
print(ord('A'))
print(ord('M'))

95 - 112   - "lowercase alphabets"

118 - 126  - "uppercase alphabets"

 
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");    
  else:  
    print ("Given Year is not a leap Year")  
  
Year = int(input("Enter the number: "))    
CheckLeap(Year)  

print("Enter a Character: ",)
print("Enter a Character: ", end="")
c = input()
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>='a' and c<='z':
        print("\n\"" +c+ "\" is an alphabet.")
    elif c>='A' and c<='Z':
        print("\n\"" +c+ "\" is an alphabet.")
    else:
        print("\n\"" +c+ "\" is not an alphabet!")
