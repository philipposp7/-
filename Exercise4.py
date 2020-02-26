output = input("Enter message: ")
print ("String (in ASCII):")
##Συνάρτηση επιστροφής εξόδου
def asc(x):
  return [ ord(x) for x in output ]
  print(asc(output))
#Χαρακτηρισμός μονού αριθμού
def odd(output):
  number = ''.join(str(ord(c)) for c in output)
  num = int(number)
  if  num> 1: 

   for i in range(2, num//2): 
           
       if (num % i) == 0: 
           return num, "is not a odd number" 
           break
   else: 
       return num, "is a odd number" 
  
  else: 
   return num, "is not a odd number"
#Αποτέλεσμα
print (odd(output))