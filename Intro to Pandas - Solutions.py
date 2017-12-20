-------Άσκηση-------

1. Διαβάστε το αρχείο titanic.csv σε μεταβλητή με όνομα titanic
2. Πόσες σειρές έχει το αρχείο;
3. Αν μια στήλη έχει πάνω από το 50% NaN, διαγράψτε την
4. Όσες έχουν λιγότερο, χρησιμοποιήστε τη fillna με την ανάλογη τιμή. Ποια είναι αυτή για κάθε στήλη;
5. Ποια στήλη έχει τη μεγαλύτερη διακύμανση;
6. Ποια η μέση τιμή του εισιτηρίου;

Λύση :

#Ερώτημα 1
import pandas as pd
titanic = pd.read_csv("titanic.csv")

#Ερώτημα 2
print("Total rows : "+str(titanic.shape[0]))

#Ερώτημα 3

if titanic.shape[0]/2 < titanic["pclass"][pd.isnull(titanic["pclass"])].shape[0] :
    del titanic["pclass"]
if titanic.shape[0]/2 < titanic["survived"][pd.isnull(titanic["survived"])].shape[0] :
    del titanic["survived"]
if titanic.shape[0]/2 < titanic["name"][pd.isnull(titanic["name"])].shape[0] :
    del titanic["name"]
if titanic.shape[0]/2 < titanic["sex"][pd.isnull(titanic["sex"])].shape[0] :
    del titanic["sex"]
if titanic.shape[0]/2 < titanic["age"][pd.isnull(titanic["age"])].shape[0] :
    del titanic["age"]
if titanic.shape[0]/2 < titanic["sibsp"][pd.isnull(titanic["sibsp"])].shape[0] :
    del titanic["sibsp"]
if titanic.shape[0]/2 < titanic["parch"][pd.isnull(titanic["parch"])].shape[0] :
    del titanic["parch"]
if titanic.shape[0]/2 < titanic["ticket"][pd.isnull(titanic["ticket"])].shape[0] :
    del titanic["ticket"]
if titanic.shape[0]/2 < titanic["fare"][pd.isnull(titanic["fare"])].shape[0] :
    del titanic["fare"]
if titanic.shape[0]/2 < titanic["cabin"][pd.isnull(titanic["cabin"])].shape[0] :
    del titanic["cabin"]
if titanic.shape[0]/2 < titanic["embarked"][pd.isnull(titanic["embarked"])].shape[0] :
    del titanic["embarked"]
if titanic.shape[0]/2 < titanic["boat"][pd.isnull(titanic["boat"])].shape[0] :
    del titanic["boat"]
if titanic.shape[0]/2 < titanic["body"][pd.isnull(titanic["body"])].shape[0] :
    del titanic["body"]
if titanic.shape[0]/2 < titanic["home.dest"][pd.isnull(titanic["home.dest"])].shape[0] :
    del titanic["home.dest"]
	
#Ερώτημα 4

titanic['age'] = titanic['age'].fillna(titanic['age'].mean())
titanic['fare'] = titanic['fare'].fillna(titanic['fare'].mean())
titanic['embarked'] = titanic['embarked'].fillna("S")
titanic['home.dest'] = titanic['home.dest'].fillna("UNKNOWN")

titanic.drop(1309, inplace=True)

#Ερώτημα 5

#Η διακύμανση είναι το τετράγωνο της τυπικής απόκλισης, την οποία μπορούμε να δούμε στο describe
titanic.describe() #--> fare

#Ερώτημα 6
titanic.describe() #--> 33.295479



