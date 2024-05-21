from colorama import Fore, init
import re # this is imported so we can check specified strings and see if they match

init(autoreset=True)

class Contacts:  # The setup of my class has been called Contacts, we will be using this to establish the details we will hold of the contacts.
    def __init__(self, first_name, last_name, phone_number, email):
        self.first = first_name
        self.last = last_name
        self.phone = phone_number
        self.email = email
    
    def display_info(self):  # Defined a new function to display all the information that we hold of the contacts and added colour for easy readability.
        print(Fore.MAGENTA + "First name: " + Fore.RESET + f"{self.first}." + Fore.MAGENTA + " Last name: " + Fore.RESET + f"{self.last}." + Fore.CYAN + " Phone number: " + Fore.RESET + f"{self.phone}." + Fore.BLUE + f" Email: " + Fore.RESET + f"{self.email}")
        print("____________________________________________________________________________________________________________")  # Print statement were used to display our contact information in a colourful and more appealing way to view the information and broken each contact into separate lines for readability.


class ManageContacts:  # The new class was set up for a way to manage the contact information.
    def __init__(self):
        self.contacts = []  # The changes we make to any of the contacts, or any new contacts will be added into a new list.

    def add_contacts(self):  # A new function within our class, so the user can add any new contacts into our database.
        while True:
            first_name = input(Fore.LIGHTBLACK_EX + "Enter first name: " + Fore.RESET)
            if len(first_name) >=3: # checking that the len of name is equal to or more than 3
                break
            else:
                print(Fore.RED + "Error. First name must be more than 3 characters.")
        while True:
            last_name = input(Fore.LIGHTBLACK_EX + "Enter last name: " + Fore.RESET)
            if len(last_name) >=3: # checking that the len of name is equal to or more than 3
                break
            else:
                print(Fore.RED + "Error. Last name must be more than 3 characters.")

        while True: # while loop used to ensure user adds a phone number that is 11 digits long
            phone_number = input(Fore.LIGHTBLACK_EX + "Enter phone number: " + Fore.RESET)
            if len(phone_number) == 11 and phone_number.isdigit():
                break
            else:
                print(Fore.RED + "Phone number must be 11 digits.")

        while True: # while loop used to ensure email contains @, and ends with .com or co.uk
            email = input(Fore.LIGHTBLACK_EX + "Enter email: " + Fore.RESET)
            if re.match(r'.+@.+\.(com|co\.uk)$', email): # researched on geeksforgeeks how to do this as was unsure, and got chatgpt to help implement
                break # this will break out of the while loop if condition is met
            else:
                print(Fore.RED + "\nEmail must contain '@' and end with .com or .co.uk\n")
        
        if any(contact.phone == phone_number or contact.email == email for contact in self.contacts): # this will be checking if any of the phone numbers and email addreses in contacts are already in our list
            print(Fore.RED + "\nContact already exists with this phone number and/or email.\n")
        else:
            new_contact = Contacts(first_name, last_name, phone_number, email)
            self.contacts.append(new_contact) # this will append our list and add our new contact
            print(Fore.GREEN + "\nContact added.\n")

    def update_contacts(self, contact_position):  # Separate functions used to be able to allow user to update any existing contact that is in our database.
        self.display_all_contacts()  # If option is picked to update the contacts, it will display a list of all contacts so the user can choose which one they would like to amend.

        if 0 <= contact_position < len(self.contacts): # checks if the position is valid against the number of contacts
            print("\nEnter new details or leave blank to keep current details.")  # Print statement used to prompt user to enter the new details or leave blank
            while True:
                new_name = input(Fore.LIGHTBLACK_EX + "Current first name - " + f"{self.contacts[contact_position].first}" + "\nNew first name: " + Fore.RESET).capitalize().strip()
                if not new_name or len(new_name) >= 3: # used a while loop to ensure that all the entered information matches the requirements that we've set.
                    break
                else:
                    print(Fore.RED + "First name must be more than 3 characters.") # error messages displayed so that the user knows what the requirements are
            
            while True:
                new_last_name = input(Fore.LIGHTBLACK_EX + "Current last name - " + f"{self.contacts[contact_position].last}" + "\nNew last name: " + Fore.RESET).capitalize().strip()
                if not new_last_name or len(new_last_name) >= 3:
                    break
                else:
                    print(Fore.RED + "Last name must be more than 3 characters.")

            new_phone = input(Fore.LIGHTBLACK_EX + "Current phone number - " + f"{self.contacts[contact_position].phone}" + "\nNew number: " + Fore.RESET).strip()
            new_email = input(Fore.LIGHTBLACK_EX + "Current email - " + f"{self.contacts[contact_position].email}" + "\nNew email: " + Fore.RESET).strip()

            if new_name: # if it is a new name then it will updated into our list
                self.contacts[contact_position].first = new_name
            if new_last_name:
                self.contacts[contact_position].last = new_last_name # same again for here
            if new_phone:
                while True:
                    if not new_phone or (len(new_phone) == 11 and new_phone.isdigit()):
                        if new_phone:
                            self.contacts[contact_position].phone = new_phone # once new phone number is 11 numbers, it will update our contact in our list
                        break
                    else:
                        print(Fore.RED + "\nInvalid number. Please enter again or leave blank to keep the same.")
                        new_phone = input("Current phone number - " + f"{self.contacts[contact_position].phone}" + "\nNew number: ").strip()
            if new_email:
                while True:
                    if not new_email or re.match(r'.+@.+\.(com|co\.uk)$', new_email): # chatgpt was used to help with this. This will be checking if the email entered contains the strings of, .com or .co.uk using the regular expression library
                        if new_email:
                            self.contacts[contact_position].email = new_email
                        break
                    else:
                        print(Fore.RED + "Please enter again or leave blank to keep the same.")
                        new_email = input(Fore.LIGHTBLACK_EX + "Current email - " + f"{self.contacts[contact_position].email}" + "\nNew email: " + Fore.RESET).strip()

            print(Fore.GREEN + "\nContact updated.")  # Once information is entered, print message will display notifying user that the contact has been updated.
        else:
            print(Fore.RED + "\nInvalid contact position entered")

    def display_all_contacts(self):  # Function created for displaying all our contacts.
        self.sort_contacts()  # we will be sorting the contacts in our list aplhabetically with their first name
        for position, contact in enumerate(self.contacts, start=1):  # For loop used so that it iterates through our contacts attribute in manage contacts
            print(f"\nContact: {position}\n")  # It will display the contact position with a number and we start that from 1 instead of 0 which is why I used start=1
            contact.display_info()
    
    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.first.lower())  # Sorted by first name and is case insensitive

    def delete_contact(self, contact_position):
        if 0 <= contact_position < len(self.contacts):
            self.contacts.pop(contact_position) # pop is used to remove the contact from using the contact position specified
            print(Fore.GREEN + "\nContact deleted.")
        else:
            print(Fore.RED + "\nInvalid contact position entered")

contacts_manager = ManageContacts() # created and instance that we can use to assign difference objects

contacts_manager.contacts.append(Contacts("Sam", "Johnson", "07749397890", "samj@email.com")) # we've added some initial contacts to our list here
contacts_manager.contacts.append(Contacts("Bart", "Stryjek", "07412346543", "bartbob@yolo.com"))
contacts_manager.contacts.append(Contacts("Matt", "Wood", "07343434342", "matt@gmail.com"))

while True:
    print(Fore.YELLOW + "\n --- CONTACT BOOK ---\n \n1. Add: \n2. Update: \n3. Display All: \n4. Search: \n5. Delete:" + Fore.LIGHTWHITE_EX + "\n0. Exit.\n")  # Options will be displayed showing what the user (manager) can do

    managers_option = input("")  # Variable set for the user input so they can enter the option they want
    if managers_option == "1":  # If user types '1' then the add contacts functions will be used to add new contact information
        contacts_manager.add_contacts()
    
    elif managers_option == "2":  # If user types '2' then the display all contacts will show up showing what contact they would like to update/amend/change
        contacts_manager.display_all_contacts()  # Calls our display_all_contacts function
        contact_position = int(input("\nEnter the number of the contact you want to update: ")) - 1  # User will be able to type in the contact number they wish to change, -1 used so that the user can select the correct contact that correlates with that number instead of the index position
        contacts_manager.update_contacts(contact_position)  # Calls our update_contacts function
    
    elif managers_option == "3":  # If user types '3' then it will show a list of all contacts.
        contacts_manager.display_all_contacts()
    
    elif managers_option == "4":  # If user types '4' they will then be able to type the first and/or last name of the contact which will display
        search_name = input("Enter the contact name you want to search: ")
        found_contact = False
        for contact in contacts_manager.contacts:
            if search_name.lower() in (contact.first.lower() + " " + contact.last.lower()): # this will be checking if the name entered in our search matches the names of either first or last in our program
                contact.display_info() # this will display the information that the user has searched for a bring up the related contact
                found_contact = True
        if not found_contact:
            print(Fore.RED + "Contact not found.") # if entered search name does not exist in our contact book, print message will be displayed
    
    elif managers_option == "5":  # If user types '5' they will be able to see all the contacts that they can delete.
        contacts_manager.display_all_contacts()  # This will be calling our display_all_contacts function and displaying our list of contacts
        contact_position = int(input("\nEnter the number of the contact you want to delete: ")) - 1  # Again we have allowed user to type the number of the contact they want to delete that correlates correctly.
        contacts_manager.delete_contact(contact_position) 
        
    elif managers_option == "0": # if option is 0 then program ends
        print("Goodbye.")
        break
    else:
        print(Fore.RED + "Invalid option") # if option is not between 0-5 then print message will display

##END