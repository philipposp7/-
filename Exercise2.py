#Άνοιγμα αρχείουd
d = open("c:/Users/kostas/Desktop/Εισαγωγή Στην Επιστήμη των Η_Y/Main.txt", "r")
#Χωρίζω τις λέξεις
s=0
#Εμφάνιση γραμμών
for line in d :
    print(line)
#Διαχωρισμός λέξεων με βάση τα σύμφωνα τους 
    for word in line.split():
        print(word)
        countb = 0
        countg = 0 
        for letter in word:
            if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
            or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
                pass
            else:
                if (letter == 'f' or letter == 'F' or letter == 'c' or letter == 'C' or letter == 'k'
                or letter == 'K' or letter == 'r' or letter == 'R') :
                    countb = countb + 1
                else:
                    countg = countg + 1
#Χαρακτηρισμός των λέξεων
        if countb > countg : 
            print ("The word is bad.")
        else:
            print ("The word is good.")