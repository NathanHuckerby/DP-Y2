import sqlite3
connection = sqlite3.connect("contactDetails.db")
cursor = connection.cursor()

def program():
    #Menu system for the program
    print("\n")
    print("-------    Welcome to the Contact Book    --------")
    print("--- Please choose one of the following options ---")
    print("----------  1) Add new contact record -------------")
    print("----------  2) Search for contacts by name --------")
    print("----------  3) Display all contact records --------")
    print("----------  4) Delete contact records -------------")
    print("----------  5) Modify contact records -------------")
    print("---------------------------------------------------")
    #Assigns the user's input into option
    option = int(input(" "))
    
    #Validates the user's input
    if option > 5 or option < 1:
        print("Invalid input: Please try again")
        program()
    else:
        if option == 1:
            #Allows the user to enter their details
            print("Please enter the following details:")
            Firstname = input("First name: ").capitalize()
            LastName = input("Last name: ").capitalize()
            Housenumber = int(input("House Number: "))
            Streetname = input("Street name: ").capitalize()
            County = input("County: ").capitalize()
            Country = input("Country: ").capitalize()
            Postcode = input("Postcode: ").capitalize()
            Phonenumber = int(input("Phone number: "))
            Email = input("Email address: ")
            #Checks if the table has been created
            #If it hasn't, it creates the table CONTACTDETAILS
            #If it has, the program passes and moved onto the rest of the code
            try:
                cursor.execute("CREATE TABLE CONTACTDETAILS (first_name TEXT, last_name TEXT, house_number INTEGER, street_name TEXT, county TEXT, country TEXT, post_code TEXT, phone_number INTEGER, email TEXT)")
            except: pass
            cursor.execute(f"INSERT INTO contactdetails VALUES ('{Firstname}', '{LastName}', '{Housenumber}', '{Streetname}', '{County}', '{Country}', '{Postcode}', '{Phonenumber}', '{Email}')")
            connection.commit()
            print("Contact details saved.")
            program()
        
        if option == 2:
            searchName = input("Please enter the name: ").capitalize()
            #Select all of the data where the first name is the user's input
            cursor.execute(f"SELECT * FROM CONTACTDETAILS WHERE first_name = '{searchName}';")
            searchResult = cursor.fetchall()
            #Prints results to user
            print(searchResult)
            program()

        
        if option == 3:
            #Fetches all of the data thats inside the database, and outputs the data to the user
            rows = cursor.execute("SELECT first_name, last_name, house_number, street_name, county, country, post_code, phone_number, email FROM contactdetails").fetchall()
            print("\n".join([str(x) for x in rows]))
            program()
        
        if option == 4:
            deleteContact = input("Please enter the name of the contact you would like to delete: ").capitalize()
            cursor.execute(f"DELETE FROM CONTACTDETAILS WHERE first_name = '{deleteContact}';")
            print("Contact details successfully deleted.")
            connection.commit()
            program()
        
        if option == 5:
            contactName = input("Please enter the name of the contact you would like to update: ").capitalize()
            updateChoice = input("What would you like to update (Please enter as row name): ")
            updateConfirm = input("Please enter your updated record: ").capitalize()
            cursor.execute(f"UPDATE CONTACTDETAILS SET {updateChoice} = ? WHERE first_name = ?", (updateConfirm, contactName))
            connection.commit()
            program()



program()
    

