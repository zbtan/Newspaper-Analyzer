import DatabaseConnector

def addComments():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT COMMENT_ID FROM comments ORDER BY COMMENT_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "M" + str(new_id_number).zfill(9)

    content = input("Content: ")

    while True:
        uid = input("User ID: ")
        if(uid[0]!="U"):
            print("Invalid Input. User ID should start with U.")
        elif(len(uid)!=10):
            print("Invalid Input. User ID should have 1 character and 9 digit.")
        else:
            break
    
    while True:
        nid = input("News ID: ")
        if(nid[0]!="N"):
            print("Invalid Input. News ID should start with n.")
        elif(len(nid)!=10):
            print("Invalid Input. News ID should have 1 character and 9 digit.")
        else:
            break
    
    query = "INSERT INTO comments (COMMENT_ID, CONTENT, USER_ID, NEWS_ID, STATUS) VALUES (%s, %s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, content, uid, nid,))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateComments():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate Comment Info\n\n[1] Content\n[2] User ID\n[3] News ID\n[4] All\n\n")
    while True:
        choice = input("Which field you want to update: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                print("Invalid Input. The number should in the range of 1 to 4.")
            else:
                break
        except:
            print("Invalid Input. Please enter the number between 1 to 4.")
    
    match choice:
        case 1:
            while True:
                id = input("Comment ID: ")
                if(id[0]!="M"):
                    print("Invalid Input. Comment ID should start with M.")
                elif(len(id)!=10):
                    print("Invalid Input. Comment ID should have 1 character and 9 digit.")
                else:
                    break
            
            content = input("Content: ")

            query = "UPDATE comments SET CONTENT = %s WHERE COMMENT_ID = %s"
            val = (content, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 2:
            while True:
                id = input("Comment ID: ")
                if(id[0]!="M"):
                    print("Invalid Input. Comment ID should start with M.")
                elif(len(id)!=10):
                    print("Invalid Input. Comment ID should have 1 character and 9 digit.")
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
            
            query = "UPDATE comments SET USER_ID = %s WHERE COMMENT_ID = %s"
            val = (uid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 3:
            while True:
                id = input("Comment ID: ")
                if(id[0]!="M"):
                    print("Invalid Input. Comment ID should start with M.")
                elif(len(id)!=10):
                    print("Invalid Input. Comment ID should have 1 character and 9 digit.")
                else:
                    break
            
            while True:
                nid = input("News ID: ")
                if(nid[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(nid)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE comments SET USER_ID = %s WHERE COMMENT_ID = %s"
            val = (uid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 4:
            while True:
                id = input("Comment ID: ")
                if(id[0]!="M"):
                    print("Invalid Input. Comment ID should start with M.")
                elif(len(id)!=10):
                    print("Invalid Input. Comment ID should have 1 character and 9 digit.")
                else:
                    break

            content = input("Content: ")

            while True:
                uid = input("User ID: ")
                if(uid[0]!="U"):
                    print("Invalid Input. User ID should start with U.")
                elif(len(uid)!=10):
                    print("Invalid Input. User ID should have 1 character and 9 digit.")
                else:
                    break
            
            while True:
                nid = input("News ID: ")
                if(nid[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(nid)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE comments SET CONTENT = %s, USER_ID = %s, NEWS_ID = %s WHERE COMMENT_ID = %s"
            val = (content, uid, nid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

    cursor.close()
    cnx.close()

def deleteComments():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("Comment ID: ")
        if(id[0]!="M"):
            print("Invalid Input. Comment ID should start with M.")
        elif(len(id)!=10):
            print("Invalid Input. Comment ID should have 1 character and 9 digit.")
        else:
            break

    query = "UPDATE comments SET STATUS = 0 WHERE COMMENT_ID = %s"
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

def printComments():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM comments WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The comment list is empty.")
    cnx.close()

def searchComments():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("Comment ID: ")
        if(id[0]!="M"):
            print("Invalid Input. Comment ID should start with M.")
        elif(len(id)!=10):
            print("Invalid Input. Comment ID should have 1 character and 9 digit.")
        else:
            break

    query = "SELECT * FROM comments WHERE COMMENT_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("Comment not found")
    except:
        print("Comment not found.")
    
    cursor.close()
    cnx.close()