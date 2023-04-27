import DatabaseConnector

def addUA():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT HISTORY_ID FROM read_history ORDER BY HISTORY_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][2:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "UA" + str(new_id_number).zfill(8)

    while True:
        aid = input("Admin ID: ")
        if(aid[0]!="A"):
            print("Invalid Input. Admin ID should start with A.")
        elif(len(aid)!=10):
            print("Invalid Input. Admin ID should have 1 character and 9 digit.")
        else:
            break

    while True:
        uid = input("User ID: ")
        if(uid[0]!="U"):
            print("Invalid Input. User ID should start with U.")
        elif(len(uid)!=10):
            print("Invalid Input. User ID should have 1 character and 9 digit.")
        else:
            break

    query = "INSERT INTO user_admin (UA_ID, ADMIN_ID, USER_ID, STATUS) VALUES (%s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, aid, uid,))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")

    cursor.close()
    cnx.close()

def updateUA():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate User-Admin Info\n\n[1] Admin ID\n[2] User ID\n[3] All\n\n")
    while True:
        choice = input("Which field you want to update: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 3:
                print("Invalid Input. The number should in the range of 1 to 3.")
            else:
                break
        except:
            print("Invalid Input. Please enter the number between 1 to 3.")

    match choice:
        case 1:
            while True:
                id = input("User-Admin ID: ")
                if(id[:2]!="UA"):
                    print("Invalid Input. User-Admin ID should start with UA.")
                elif(len(id)!=10):
                    print("Invalid Input. User-Admin ID should have 2 character and 8 digit.")
                else:
                    break

            while True:
                aid = input("Admin ID: ")
                if(aid[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(aid)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE user_admin SET ADMIN_ID = %s WHERE UA_ID = %s"
            val = (aid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 2:
            while True:
                id = input("User-Admin ID: ")
                if(id[:2]!="UA"):
                    print("Invalid Input. User-Admin ID should start with UA.")
                elif(len(id)!=10):
                    print("Invalid Input. User-Admin ID should have 2 character and 8 digit.")
                else:
                    break
            
            while True:
                uid = input("User ID: ")
                if(uid[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(uid)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE user_admin SET USER_ID = %s WHERE UA_ID = %s"
            val = (uid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("User-Admin ID: ")
                if(id[:2]!="UA"):
                    print("Invalid Input. User-Admin ID should start with UA.")
                elif(len(id)!=10):
                    print("Invalid Input. User-Admin ID should have 2 character and 8 digit.")
                else:
                    break

            while True:
                aid = input("Admin ID: ")
                if(aid[0]!="A"):
                    print("Invalid Input. Admin ID should start with A.")
                elif(len(aid)!=10):
                    print("Invalid Input. Admin ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                uid = input("User ID: ")
                if(uid[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(uid)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE user_admin SET ADMIN_ID = %s, USER_ID = %s WHERE UA_ID = %s"
            val = (aid, uid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

    cursor.close()
    cnx.close()

def deleteUA():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    while True:
        id = input("User-Admin ID: ")
        if(id[:2]!="UA"):
            print("Invalid Input. User-Admin ID should start with UA.")
        elif(len(id)!=10):
            print("Invalid Input. User-Admin ID should have 2 character and 8 digit.")
        else:
            break

    query = "UPDATE user_admin SET STATUS = 0 WHERE UA_ID = %s"
    
    val = (id,)
    try:
        cursor.execute(query, val)
        cnx.commit()
        print("Delete successful.")
    except:
        print("Delete unsuccessful.")
    
    cursor.close()
    cnx.close()

def printUA():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM user_admin WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The user-admin list is empty.")
    cnx.close()

def searchUA():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("User-Admin ID: ")
        if(id[:2]!="UA"):
            print("Invalid Input. User-Admin ID should start with UA.")
        elif(len(id)!=10):
            print("Invalid Input. User-Admin ID should have 2 character and 8 digit.")
        else:
            break

    query = "SELECT * FROM user_admin WHERE UA_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("User-Admin not found")
    except:
        print("User-Admin not found.")
    
    cursor.close()
    cnx.close()