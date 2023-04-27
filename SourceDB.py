import DatabaseConnector
import re

def addSource():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT SOURCE_ID FROM source ORDER BY SOURCE_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "S" + str(new_id_number).zfill(9)

    name = input("Name: ")

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

    query = "INSERT INTO source (SOURCE_ID, NAME, URL, STATUS) VALUES (%s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, name, url))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateSource():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate Source Info\n\n[1] Name\n[2] URL\n[3] All\n\n")
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
                id = input("Source ID: ")
                if(id[0]!="S"):
                    print("Invalid Input. Source ID should start with S.")
                elif(len(id)!=10):
                    print("Invalid Input. Source ID should have 1 character and 9 digit.")
                else:
                    break
            name = input("Name: ")
            query = "UPDATE source SET NAME = %s WHERE SOURCE_ID = %s"
            val = (name, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 2:
            while True:
                id = input("Source ID: ")
                if(id[0]!="S"):
                    print("Invalid Input. Source ID should start with S.")
                elif(len(id)!=10):
                    print("Invalid Input. Source ID should have 1 character and 9 digit.")
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
            
            query = "UPDATE source SET URL = %s WHERE SOURCE_ID = %s"
            val = (url, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("Source ID: ")
                if(id[0]!="S"):
                    print("Invalid Input. Source ID should start with S.")
                elif(len(id)!=10):
                    print("Invalid Input. Source ID should have 1 character and 9 digit.")
                else:
                    break

            name = input("Name: ")
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

            query = "UPDATE source SET NAME = %s, URL = %s, WHERE SOURCE_ID = %s"
            val = (name, url, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
                
    cursor.close()
    cnx.close()

def deleteSource():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("Source ID: ")
        if(id[0]!="S"):
            print("Invalid Input. Source ID should start with S.")
        elif(len(id)!=10):
            print("Invalid Input. Source ID should have 1 character and 9 digit.")
        else:
            break
    query = "UPDATE source SET STATUS = 0 WHERE SOURCE_ID = %s"
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

def printSource():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM source WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The source list is empty.")
    cnx.close()

def searchSource():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("Source ID: ")
        if(id[0]!="S"):
            print("Invalid Input. Source ID should start with S.")
        elif(len(id)!=10):
            print("Invalid Input. Source ID should have 1 character and 9 digit.")
        else:
            break
    query = "SELECT * FROM source WHERE SOURCE_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("Source not found")
    except:
        print("Source not found.")
    
    cursor.close()
    cnx.close()