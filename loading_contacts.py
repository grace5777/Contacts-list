import random 

# giving information that will be used for all the random 200 contacts
def load_initial_contacts(contact_book):
    first_names = ["Grace ", "Lucy", "Eden", "Charlie", "Sam", "Shannon", "Henry", "Tilly", "wendy", "olivia", "Lewis", "Maddie", "Rachel", "Susan", "Duncan", "Ana", "Michelle", "Jennifer", "Miranda"]

    last_names = ["Smith", "Williams", "Adams", "Baker", "Johnson", "Kent", "Lawrence", "Addyman", "Stevens", "Rivers", "Cassidy", "Jennings", "Pierce", "Stone", "Sinclair", "Parker", "Knight", "Francis", "Wilson", "Anderson"]
    
    street_names = ["Desborough Avenue", "High Street", "Pretty girl Avenue", "Amersham Road", "Parkside Road", "Market Street", "Feathers Way", "Ivy Street"]

    # making sets will prevent duplication
    used_names = set()
    used_phones = set()
    used_addresses = set()

    # will loop until 200 contacts have been made
    while len(used_names) < 200:
        # creating a full name
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        # if the name has been used already it will find a new one
        if name in used_names:
            continue 

        # creating a uk phone number
        # the 07 is because all uk numbers start with 07
        # random.randit(100, 999) will create 3 random digits
        # random.randit(100, 999999) will create 6 random digits
        # this allows the phone number to be spaced like an actual phone number
        phone = f"07{random.randint(100, 999)} {random.randint(100000, 999999)}"
        # making sure theres no duplication
        if phone in used_phones:
            continue

        # creating an address
        # getting a random house number 
        house_number = random.randint(1, 200)
        # combines the number and one of the street names
        address = f"{house_number} {random.choice(street_names)}"
        # making sure theres no duplication
        if address in used_addresses:
            continue

        # adding the contact to the contact book
        contact_book.add_contact(name, phone, address, silent = True)
        used_names.add(name, silent = True)
        used_phones.add(phone, silent = True)
        used_addresses.add(address, silent = True)