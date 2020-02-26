#Χρήση βιβλιοθήκης
from datetime import datetime
print("Write the date like 'day/month/year'")
print("Enter the day:")
d = int(input())
print("Enter the month:")
m = int(input())
print("Enter the year:")
y = int(input())
#Σημερινή ημερομηνία
x = datetime.now()
#Η ημερομηνία του χρήστη
s = datetime(y,m,d)
print(s)
print(x.year)
#Η έξοδος των ασκήσεων γίνεται με την χρήση της μεταβλητής dif
dif = x - s
print(dif.days)
print(dif.total_seconds()/3600)
print(dif.total_seconds())
#Χρήση της βιβλιοθήκης για την εύρεση των ημερών του μήνα
from calendar import monthrange
#Δημιουργία μιας μεταβλητής που μπορεί να χρησιμοποιηθεί και ως λίστα
l = monthrange (y,m)
print("This month has", l[1] , "days!!!!")