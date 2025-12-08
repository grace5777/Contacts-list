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

