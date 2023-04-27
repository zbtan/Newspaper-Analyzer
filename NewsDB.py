import DatabaseConnector
import re

def addNews():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT NEWS_ID FROM news ORDER BY NEWS_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "N" + str(new_id_number).zfill(9)

    title = input("Title: ")

    while True:
        try:
            url_pattern = re.compile(r'https?://(www\.)?\w+\.\w{2,3}')
            url = input("URL: ")
            
            if url_pattern.match(url) == True:
                url = url_pattern.match(url)
                break
            else:
                print("Invalid URL.")
        except:
            print("Invalid URL.")

    while True:
        sid = input("Source ID: ")
        if(sid[0]!="S"):
            print("Invalid Input. Source ID should start with S.")
        elif(len(sid)!=10):
            print("Invalid Input. Source ID should have 1 character and 9 digit.")
        else:
            break

    while True:
        cid = input("Category ID: ")
        if(cid[0]!="C"):
            print("Invalid Input. Category ID should start with C.")
        elif(len(cid)!=10):
            print("Invalid Input. Category ID should have 1 character and 9 digit.")
        else:
            break

    query = "INSERT INTO news (NEWS_ID, TITLE, URL, SOURCE_ID, CATEGORY_ID, STATUS) VALUES (%s, %s, %s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, title, url, sid, cid))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateNews():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate News Info\n\n[1] Title\n[2] URL\n[3] Source ID\n[4] Category ID\n[5] All\n\n")
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
                id = input("News ID: ")
                if(id[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(id)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            title = input("Title: ")

            query = "UPDATE news SET TITLE = %s WHERE NEWS_ID = %s"
            val = (title, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 2:
            while True:
                id = input("News ID: ")
                if(id[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(id)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break
            
            while True:
                try:
                    url_pattern = re.compile(r'https?://(www\.)?\w+\.\w{2,3}')
                    url = input("URL: ")
                    
                    if url_pattern.match(url) == True:
                        url = url_pattern.match(url)
                        break
                    else:
                        print("Invalid URL.")
                except:
                    print("Invalid URL.")
            
            query = "UPDATE news SET URL = %s WHERE NEWS_ID = %s"
            val = (url, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("News ID: ")
                if(id[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(id)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                sid = input("Source ID: ")
                if(sid[0]!="S"):
                    print("Invalid Input. Source ID should start with S.")
                elif(len(sid)!=10):
                    print("Invalid Input. Source ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE news SET SOURCE_ID = %s WHERE NEWS_ID = %s"
            val = (sid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 4:
            while True:
                id = input("News ID: ")
                if(id[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(id)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                cid = input("Category ID: ")
                if(cid[0]!="C"):
                    print("Invalid Input. Category ID should start with C.")
                elif(len(cid)!=10):
                    print("Invalid Input. Category ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE news SET CATEGORY_ID = %s WHERE NEWS_ID = %s"
            val = (cid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 5:
            while True:
                id = input("News ID: ")
                if(id[0]!="N"):
                    print("Invalid Input. News ID should start with n.")
                elif(len(id)!=10):
                    print("Invalid Input. News ID should have 1 character and 9 digit.")
                else:
                    break

            title = input("Title: ")

            while True:
                try:
                    url_pattern = re.compile(r'https?://(www\.)?\w+\.\w{2,3}')
                    url = input("URL: ")
                    
                    if url_pattern.match(url) == True:
                        url = url_pattern.match(url)
                        break
                    else:
                        print("Invalid URL.")
                except:
                    print("Invalid URL.")

            while True:
                sid = input("Source ID: ")
                if(sid[0]!="S"):
                    print("Invalid Input. Source ID should start with S.")
                elif(len(sid)!=10):
                    print("Invalid Input. Source ID should have 1 character and 9 digit.")
                else:
                    break

            while True:
                cid = input("Category ID: ")
                if(cid[0]!="C"):
                    print("Invalid Input. Category ID should start with C.")
                elif(len(cid)!=10):
                    print("Invalid Input. Category ID should have 1 character and 9 digit.")
                else:
                    break

            query = "UPDATE news SET TITLE = %s, URL = %s, SOURCE_ID = %s, CATEGORY_ID = %s WHERE NEWS_ID = %s"
            val = (title, url, sid, cid, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

    cursor.close()
    cnx.close()

def deleteNews():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("News ID: ")
        if(id[0]!="N"):
            print("Invalid Input. News ID should start with N.")
        elif(len(id)!=10):
            print("Invalid Input. News ID should have 1 character and 9 digit.")
        else:
            break
    query = "UPDATE news SET STATUS = 0 WHERE NEWS_ID = %s"
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

def printNews():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM news WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The news list is empty.")
    cnx.close()

def searchNews():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("News ID: ")
        if(id[0]!="N"):
            print("Invalid Input. News ID should start with N.")
        elif(len(id)!=10):
            print("Invalid Input. News ID should have 1 character and 9 digit.")
        else:
            break
    query = "SELECT * FROM news WHERE NEWS_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("News not found")
    except:
        print("News not found.")
    
    cursor.close()
    cnx.close()