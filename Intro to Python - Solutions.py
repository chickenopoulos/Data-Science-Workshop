#####
DAY 1
#####

-------Άσκηση-------

1. Δημιουργήστε 2 κενές λίστες. Η πρώτη να λέγεται cities και η δεύτερη populations
2. Με χρήση της append προσθέστε 5 πόλεις της Ελλάδας
3. Αφού βρείτε τον πληθυσμό των πόλεων από τη Wikipedia, συμπληρώστε και τη δεύτερη λίστα με την ίδια σειρά
4. Τυπώστε τη δεύτερη πόλη μαζί με τον πληθυσμό της στη μορφή "Καβάλα: 80000"

Λύση :

#δημιουργία κενών λιστών
cities = []
populations = []

#Χρήση της append για προσθήκη 5 πόλεων και πληθυσμών
cities.append("Καβάλα")
cities.append("Θεσσαλονίκη")
cities.append("Αθήνα")
cities.append("Ξάνθη")
cities.append("Πάτρα")

populations.append(124.917)
populations.append(315.196)
populations.append(664.046)
populations.append(70.873)
populations.append(167.446)

#Τύπωση της δεύτερης πόλης μαζι με τον πληθυσμό της
print(cities[1]+": "+str(populations[1]))

-------Άσκηση-------

Να βρεθεί η πόλη με την μεγαλύτερη εγκληματικότητα. 

Λύση :

maxCrime = -1
city = ""

for row in rows :
    temp = row.split(',')
    if(int(temp[1]) > maxCrime) :
        maxCrime = int(temp[1])
        city = temp[0]
print(city)  

-------Άσκηση-------    

1. Να βρεθεί dataset με όλες τις πόλεις και τον πληθυσμό τους
2. Να βρεθεί η πόλη με τον μικρότερο πληθυσμό

Λύση :

data = open("populations.csv", "r", encoding="utf8").read().split('\n')

smallest_city = ''
smallest_pop = 9999999999999999

for row in data[1:-2]:
    city = row.split(',')
    if float(city[4]) < smallest_pop:
        smallest_pop = float(city[4])
        smallest_city = city[0]

print(smallest_city)

-------Άσκηση-------   

Να γραφτεί συνάρτηση που θα δέχεται λίστα και θα επιστρέφει το μέγιστο. 
Για ευκολία, θεωρούμε ότι η λίστα θα περιέχει μόνο αριθμούς.

Λύση :

def maxItem(x):
    max_item = -9999
    for i in x:
        if(int(i) > max_item):
            max_item = int(i)
    return max_item
	
	
-------Επαναληπτική Άσκηση-------   

1. Διαβάζουμε το αρχείο births.csv
2. Το φέρνουμε σε μορφή list of lists
3. Ποια ήταν η χρονιά με τις περισσότερες γέννες;
4. Ποια είναι η κατανομή γεννών ανά μήνα;

Για το 4, το επιθυμητό αποτέλεσμα είναι:

January: 15%
February: 8%
March: 7%
...
...

Λύση :

#Διαβάζουμε το αρχείο births.csv
data = open("births.csv", "r", encoding="utf8").read().split("\n")

#Το φέρνουμε σε μορφή list of lists
births = []
flag = True #δείχνει αν είναι η πρώτη σειρά (True = ναι)
for row in data:
    if flag :
        flag = False
    else :
        births.append( row.split(","))

#Η χρονιά με τις περισσότερες γέννες
flag = True #δείχνει αν είναι η πρώτη σειρά (True = ναι)
max_births = -99999
max_year = ""
count = 0 #μετράει το άθροισμα των γεννήσεων κάθε έτους
index_row = "" #αποθηκεύει το έτος του προηγούμενου row

for row in births:
    if flag :
        flag = False
        count += int(row[-1])
    else :
        if row[0] == index_row :  #αν το έτος είναι ίδιο με του προηγούμενου row
            count += int(row[-1]) #τότε πρόσθεσε την τιμή στο count
        else :
            if(row[0] != ""):  #Check αν η γραμμή είναι άδεια
                if count > max_births:  #κλασικός έλεγχος max
                    max_births = count  
                    max_year = index_row
                index_row = row[0] #αλλαγή του έτους
                count = int(row[-1]) #επαναφορά του count
print("Year with most births :", max_year, "\n" + "Births :",max_births, "\n")

#Κατανομή των γεννών ανά μήνα
flag = True #δείχνει αν είναι η πρώτη σειρά (True = ναι)
months = [0,0,0,0,0,0,0,0,0,0,0,0]
max_year = ""
count = 0 #μετράει το άθροισμα των γεννήσεων κάθε μήνα
years_passed = 0 #μετράει το πόσες χρονιές έχει το dataset
index_row = "" #αποθηκεύει το μήνα του προηγούμενου row

for row in births:

        if(row[0] != ""):  #Check αν η γραμμή δεν είναι άδεια
            if row[1] == index_row :  #αν το έτος είναι ίδιο με του προηγούμενου row
                count += int(row[-1]) #τότε πρόσθεσε την τιμή στο count
            else :	#αν το έτος δεν είναι ίδιο
                if(row[0] != ""):  #Check αν η γραμμή δεν είναι άδεια
                    years_passed += 1 
                    months[int(row[1])-1] = count #προσθήκη του αθροίσματος των γεννήσεων αυτού του μήνα στον months
                    index_row = row[1] #αλλαγή του μήνα
                    count = int(row[-1]) #επαναφορά του count

pososta = []  #πίνακας αποθήκευσης ποσοστών γεννήσεων ανά μήνα
for row in months :
    temp = int(row)*100/4080627 #το 4080627 είναι το άθροισμα όλων των γεννήσεων
    pososta.append(temp)                

print("January : "+"%.2f" % float(pososta[0])+"%")
print("February : "+"%.2f" % float(pososta[1])+"%")
print("March : "+"%.2f" % float(pososta[2])+"%")
print("April : "+"%.2f" % float(pososta[3])+"%")
print("May : "+"%.2f" % float(pososta[4])+"%")
print("June : "+"%.2f" % float(pososta[5])+"%")
print("July : "+"%.2f" % float(pososta[6])+"%")
print("August : "+"%.2f" % float(pososta[7])+"%")
print("September : "+"%.2f" % float(pososta[8])+"%")
print("October : "+"%.2f" % float(pososta[9])+"%")
print("November : "+"%.2f" % float(pososta[10])+"%")
print("December : "+"%.2f" % float(pososta[11])+"%")





























