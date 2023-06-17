import DatabaseConnector
import re

def addAdmin():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT ADMIN_ID FROM admin ORDER BY ADMIN_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "A" + str(new_id_number).zfill(9)

    name = input("Name: ")

    email = input("Email: ")
    def is_valid_email(email):
        pattern = r"[^@]+@[^@]+\.[^@]+" #Define the pattern of the valid email

        if re.match(pattern, email):
            return True
        else:
            print("Please enter a valid email.")
            return False
    while is_valid_email(email) == False:
        email = input("Email: ")

    while True:
        password = input("Password: ")
        password_confirm = input("Confirm password: ")
        
        if password != password_confirm:
            print("Passwords do not match. Please try again.")
        elif len(password) < 8:
            print("Password is too short. Please enter at least 8 characters.")
        else:
            break

    query = "INSERT INTO admin (ADMIN_ID, NAME, EMAIL, PASSWORD, STATUS) VALUES (%s, %s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, name, email, password))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateAdmin():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate Admin Info\n\n[1] Name\n[2] Email\n[3] Password\n[4] All\n\n")
    while True:
        choice = input("Which field you want to update: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                print("Invalid Input. The number should in the range of 1 to 7.")
            else:
                break
        except:
            print("Invalid Input. Please enter the number between 1 to 7.")
    
    match choice:
        case 1:
            while True:
                id = input("Admin ID: ")
                if(id[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(id)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break
            name = input("Name: ")
            query = "UPDATE admin SET NAME = %s WHERE ADMIN_ID = %s"
            val = (name, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 2:
            while True:
                id = input("Admin ID: ")
                if(id[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(id)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break

            email = input("Email: ")
            def is_valid_email(email):
                pattern = r"[^@]+@[^@]+\.[^@]+" #Define the pattern of the valid email
                if re.match(pattern, email):
                    return True
                else:
                    print("Please enter a valid email.")
                return False
            while is_valid_email(email) == False:
                email = input("Email: ")

            query = "UPDATE admin SET EMAIL = %s WHERE ADMIN_ID = %s"
            val = (email, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("Admin ID: ")
                if(id[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(id)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                current_password = input("Enter current password: ")
                password = input("Enter password: ")
                password_confirm = input("Confirm password: ")
                
                sql_query = "SELECT PASSWORD FROM admin WHERE ADMIN_ID = %s"
                cursor.execute(sql_query, (id,))
                result = cursor.fetchone()

                if current_password != result[0]:
                    print("Incorrect password. Please try again.")
                # Check if new password and confirmation match
                elif password != password_confirm:
                    print("Passwords do not match. Please try again.")
                # Check if new password meets requirements
                elif len(password) < 8:
                    print("Password is too short. Please enter at least 8 characters.")
                # Password is valid, update user password
                else:
                    break
            
            query = "UPDATE admin SET PASSWORD = %s WHERE ADMIN_ID = %s"
            val = (password, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 8:
            while True:
                id = input("Admin ID: ")
                if(id[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(id)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break

            name = input("Name: ")
            email = input("Email: ")
            def is_valid_email(email):
                pattern = r"[^@]+@[^@]+\.[^@]+" #Define the pattern of the valid email

                if re.match(pattern, email):
                    return True
                else:
                    print("Please enter a valid email.")
                    return False
            while is_valid_email(email) == False:
                email = input("Email: ")

            while True:
                current_password = input("Enter current password: ")
                password = input("Enter password: ")
                password_confirm = input("Confirm password: ")
                
                sql_query = "SELECT PASSWORD FROM admin WHERE ADMIN_ID = %s"
                cursor.execute(sql_query, (id,))
                result = cursor.fetchone()

                if current_password != result[0]:
                    print("Incorrect password. Please try again.")
                # Check if new password and confirmation match
                elif password != password_confirm:
                    print("Passwords do not match. Please try again.")
                # Check if new password meets requirements
                elif len(password) < 8:
                    print("Password is too short. Please enter at least 8 characters.")
                # Password is valid, update user password
                else:
                    break
                
            query = "UPDATE admin SET NAME = %s, EMAIL = %s, PASSWORD = %s WHERE ADMIN_ID = %s"
            val = (name, email, password, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
                
    cursor.close()
    cnx.close()

def deleteAdmin():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("Admin ID: ")
        if(id[0]!="A"):
            print("Invalid Input. Admin ID should start with A.")
        elif(len(id)!=10):
            print("Invalid Input. Admin ID should have 1 character and 9 digit.")
        else:
            break
    query = "UPDATE admin SET STATUS = 0 WHERE ADMIN_ID = %s"
    cursor = cnx.cursor()
    
    val = (id,)
    try:
        cursor.execute(query, val)
        cnx.commit()
        print("Delete successful.")
    except:
        print("Delete unsuccessful.")
    
    cursor.close()
    cnx.close()

def printAdmin():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM admin WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row[:-2])
    else:
        print("The admin list is empty.")
    cnx.close()

def searchAdmin():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("Admin ID: ")
        if(id[0]!="A"):
            print("Invalid Input. Admin ID should start with A.")
        elif(len(id)!=10):
            print("Invalid Input. Admin ID should have 1 character and 9 digit.")
        else:
            break
    query = "SELECT * FROM admin WHERE ADMIN_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result[:-2])
        else:
            print("Admin not found")
    except:
        print("Admin not found.")
    
    cursor.close()
    cnx.close()
