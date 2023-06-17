import DatabaseConnector
import ReadFile
import re

def addUser():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT USER_ID FROM users ORDER BY USER_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "U" + str(new_id_number).zfill(9)

    image = ReadFile.readPic()

    name = input("Name: ")

    gender = input("Gender: ")
    if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
        gender = "Male"
    elif (gender == "Female" or gender == "female" or gender == "f" or gender =="F"):
        gender = "Female"
    while (gender != "Female" and gender != "Male"):
        gender = input("Gender: ")
        if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
            gender = "Male"
        elif (gender == "Female" or gender == "female" or gender == "f" or gender == "F"):
            gender = "Female"

    while True:
        age_str = input("Age: ")
        try:
            age = int(age_str)
            if age < 0:
                print("Invalid input. Age cannot be negative.")
            elif age > 120:
                print("Invalid input. Age cannot be greater than 120.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer age.")

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

    query = "INSERT INTO users (USER_ID, PIC, NAME, GENDER, AGE, EMAIL, PASSWORD, STATUS) VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, image, name, gender, age, email, password))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateUser():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate User Info\n\n[1] Profil Pic\n[2] Name\n[3] Gender\n[4] Age\n[5] Email\n[6] Password\n[7] All\n\n")
    while True:
        choice = input("Which field you want to update: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                print("Invalid Input. The number should in the range of 1 to 5.")
            else:
                break
        except:
            print("Invalid Input. Please enter the number between 1 to 5.")
    
    match choice:
        case 1:
            # Main code
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            image = ReadFile.readPic()

            query = "UPDATE users SET PIC = %s WHERE USER_ID = %s"
            val = (image, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        case 2:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break
            name = input("Name: ")
            query = "UPDATE users SET NAME = %s WHERE USER_ID = %s"
            val = (name, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 3:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            gender = input("Gender: ")
            if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
                gender = "Male"
            elif (gender == "Female" or gender == "female" or gender == "f" or gender =="F"):
                gender = "Female"
            while (gender != "Female" and gender != "Male"):
                gender = input("Gender: ")
                if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
                    gender = "Male"
                elif (gender == "Female" or gender == "female" or gender == "f" or gender == "F"):
                    gender = "Female"
            
            query = "UPDATE users SET GENDER = %s WHERE USER_ID = %s"
            val = (gender, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 4:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                age_str = input("Age: ")
                try:
                    age = int(age_str)
                    if age < 0:
                        print("Invalid input. Age cannot be negative.")
                    elif age > 120:
                        print("Invalid input. Age cannot be greater than 120.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer age.")

            query = "UPDATE users SET AGE = %s WHERE USER_ID = %s"
            val = (age, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 5:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
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

            query = "UPDATE users SET EMAIL = %s WHERE USER_ID = %s"
            val = (email, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 6:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                current_password = input("Enter current password: ")
                password = input("Enter password: ")
                password_confirm = input("Confirm password: ")
                
                sql_query = "SELECT PASSWORD FROM users WHERE USER_ID = %s"
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
            
            query = "UPDATE users SET PASSWORD = %s WHERE USER_ID = %s"
            val = (password, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 7:
            while True:
                id = input("User ID: ")
                if(id[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(id)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break
            
            image = ReadFile.readPic()
            
            name = input("Name: ")
            gender = input("Gender: ")
            if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
                gender = "Male"
            elif (gender == "Female" or gender == "female" or gender == "f" or gender =="F"):
                gender = "Female"
            while (gender != "Female" and gender != "Male"):
                gender = input("Gender: ")
                if (gender == "Male" or gender == "male" or gender == "m" or gender == "M"):
                    gender = "Male"
                elif (gender == "Female" or gender == "female" or gender == "f" or gender == "F"):
                    gender = "Female"

            while True:
                age_str = input("Age: ")
                try:
                    age = int(age_str)
                    if age < 0:
                        print("Invalid input. Age cannot be negative.")
                    elif age > 120:
                        print("Invalid input. Age cannot be greater than 120.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer age.")

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
                
            query = "UPDATE users SET PIC = %s, NAME = %s, GENDER = %s, AGE = %s, EMAIL = %s, PASSWORD =%s WHERE USER_ID = %s"
            val = (image, name, gender, age, email, password, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
                
    cursor.close()
    cnx.close()

def deleteUser():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("User ID: ")
        if(id[0]!="U"):
            print("Invalid Input. User ID should start with U.")
        elif(len(id)!=10):
            print("Invalid Input. User ID should have 1 character and 9 digit.")
        else:
            break
    query = "UPDATE users SET STATUS = 0 WHERE USER_ID = %s"
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

def printUser():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM users WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row[:-2])
    else:
        print("The user list is empty.")
    cnx.close()

def searchUser():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("User ID: ")
        if(id[0]!="U"):
            print("Invalid Input. User ID should start with U.")
        elif(len(id)!=10):
            print("Invalid Input. User ID should have 1 character and 9 digit.")
        else:
            break
    query = "SELECT * FROM users WHERE USER_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result[:-2])
        else:
            print("User not found")
    except:
        print("User not found.")
    
    cursor.close()
    cnx.close()