print("Enter a number:")
number=int(input())
#Έναρξη διδαδικασίας
def prob(number):
    global sum 
    sum = 0
    number = number * 3
    number = number + 1
    #Επαναληπτική διαδικασία
    while number > 0:
        rem = number % 10
        sum = sum + rem
        number = int(number/10)
    print(sum)
prob(number)
while sum >=10 :
    prob(sum)
