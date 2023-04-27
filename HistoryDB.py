import DatabaseConnector
import datetime

def addHistory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT HISTORY_ID FROM read_history ORDER BY HISTORY_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "H" + str(new_id_number).zfill(9)

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

    cdt = datetime.datetime.now()
    dt = cdt.strftime("%Y-%m-%d %H:%M:%S")

    query = "INSERT INTO read_history (HISTORY_ID, USER_ID, NEWS_ID, DATE_TIME, STATUS) VALUES (%s, %s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, uid, nid, dt,))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")

    cursor.close()
    cnx.close()

def updateHistory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate History Info\n\n[1] User ID\n[2] News ID\n[3] All\n\n")
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
                id = input("History ID: ")
                if(id[0]!="H"):
                    print("Invalid Input. History ID should start with H.")
                elif(len(id)!=10):
                    print("Invalid Input. History ID should have 1 character and 9 digit.")
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

            query = "UPDATE read_history SET USER_ID = %s WHERE HISTORY_ID = %s"
            val = (uid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 2:
            while True:
                id = input("History ID: ")
                if(id[0]!="H"):
                    print("Invalid Input. History ID should start with H.")
                elif(len(id)!=10):
                    print("Invalid Input. History ID should have 1 character and 9 digit.")
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

            query = "UPDATE read_history SET NEWS_ID = %s WHERE HISTORY_ID = %s"
            val = (nid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("History ID: ")
                if(id[0]!="H"):
                    print("Invalid Input. History ID should start with H.")
                elif(len(id)!=10):
                    print("Invalid Input. History ID should have 1 character and 9 digit.")
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

            while True:
                nid = input("News ID: ")
                if(nid[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(nid)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE read_history SET USER_ID = %s, NEWS_ID = %s WHERE HISTORY_ID = %s"
            val = (uid, nid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

    cursor.close()
    cnx.close()

def deleteHistory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    while True:
        id = input("History ID: ")
        if(id[0]!="H"):
            print("Invalid Input. History ID should start with H.")
        elif(len(id)!=10):
            print("Invalid Input. History ID should have 1 character and 9 digit.")
        else:
            break

    query = "UPDATE read_history SET STATUS = 0 WHERE HISTORY_ID = %s"
    
    val = (id,)
    try:
        cursor.execute(query, val)
        cnx.commit()
        print("Delete successful.")
    except:
        print("Delete unsuccessful.")
    
    cursor.close()
    cnx.close()

def printHistory():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM read_history WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The history list is empty.")
    cnx.close()

def searchHistory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("History ID: ")
        if(id[0]!="H"):
            print("Invalid Input. History ID should start with H.")
        elif(len(id)!=10):
            print("Invalid Input. History ID should have 1 character and 9 digit.")
        else:
            break

    query = "SELECT * FROM read_history WHERE HISTORY_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("History not found")
    except:
        print("History not found.")
    
    cursor.close()
    cnx.close()