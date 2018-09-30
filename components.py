# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age
       # self.status = ""

    def __str__(self):
        # your code goes here!
        return " Name: %s , Age: %d , Bio: %s " % (self.name, self.age, self.bio)


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []


    def assign_president(self, person):
        # your code goes here!
        self.president = person


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!

        s = 0.0

        print ("\nMembers: ")

        #if self.president != "":
            #print (" Name: %s , Age: %d , Status: President , Bio: %s " % (self.name, self.age, self.bio))

        for m in self.members:
            if m.name.lower() == self.president.name.lower():
                print (" Name: %s , Age: %d , Status: president , Bio: %s " % (m.name, m.age, m.bio))
            else:
                print (m)

        for cm in self.members:
            s += cm.age

        avg = s/len(self.members)

        print ("\nThe average age in this club is %.2f yr" % avg)

    def __str__(self):
        # your code goes here!
        return " Name: %s \n Description: %s \n Num Of Members: %d " % (self.name, self.description, len(self.members))
