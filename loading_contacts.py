import random 

# giving information that will be used for all the random 200 contacts
def load_initial_contacts(contact_book):
    first_names = ["Grace ", "Lucy", "Eden", "Charlie", "Sam", "Shannon", "Henry", "Tilly", "wendy", "olivia", "Lewis"]

    last_names = ["Smith", "Williams", "Adams", "Baker", "Johnson", "Kent", "Lawrence", "Addyman", "Stevens"]
    
    street_names = ["Desborough Avenue", "High street", "Pretty girl avenue", "Amersham Road", "Parkside Road", "Market Street", "Feathers Way", "Ivy Street"]

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



        # adding the contact to the contact book
        contact_book.add_contact(name)