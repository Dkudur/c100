x = {
    "keyName" : "value",
    "Name" : "abc",
    "id" : 100
}

print(x["id"])

contact = {
    "Number" : 7892536728,
    "Name" : "Sam",
    "Email" : "sam@gmail.com"
}

Grades = {
    "Name" : "Carl",
    "Id" : 786250,
    "Math" : 93,
    "History" : 89,
    "Science" : 92,
    "Writing" : 85,
    "Reading" : 98
}


def average(M, H, S, W, R):
    total = M+H+S+W+R
    average = total/5
    print(average)

average(Grades["Math"], Grades["History"], Grades["Science"], Grades["Writing"], Grades["Reading"])

# -----------------------------------------

class ContactDetails():
    def __init__(self , name , number , email):
        self.Name = name
        self.Number = number
        self.Email = email

        self.person = {
            "NAME" : self.Name,
            "NUMBER" : self.Number,
            "EMAIL" : self.Email
        }

    def showDetails(self):
        print(self.person)


# object name = Class Name()

p1 = ContactDetails("Aniket" , 9019873735 , "ad@gmail.c")

print(p1.Name)

p1.showDetails()







