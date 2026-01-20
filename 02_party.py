class Party:

    def __init__(self):
        self.people = []

    def fill_in_names(self):
        name = input()
        while name != "End":
            self.people.append(name)
            name = input()

    def __repr__(self):
        people = ", ".join(self.people)
        returning_string = f"Going: {people}"
        total_people = len(self.people)
        returning_string += f"\nTotal: {total_people}"
        return returning_string

my_party = Party()
my_party.fill_in_names()
print(my_party)







