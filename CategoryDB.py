import DatabaseConnector

def addCategory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    sql_query = "SELECT CATEGORY_ID FROM category ORDER BY CATEGORY_ID DESC LIMIT 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    if result is not None:
        last_id_number = int(result[0][1:])   # Extract the numeric portion of the last ID number
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1
    new_id = "C" + str(new_id_number).zfill(9)

    name = input("Name: ")

    desc = input("Description: ")

    query = "INSERT INTO category (CATEGORY_ID, NAME, DESCRIPTION, STATUS) VALUES (%s, %s, %s, 1)"
    try:
        cursor.execute(query, (new_id, name, desc))
        cnx.commit()
        print("Insert successful.")
    except:
        print("Insert unsuccessful.")
    cursor.close()
    cnx.close()

def updateCategory():

    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()

    print("Upadate Category Info\n\n[1] Name\n[2] Description\n[3] All\n\n")
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
                id = input("Category ID: ")
                if(id[0]!="C"):
                    print("Invalid Input. Category ID should start with C.")
                elif(len(id)!=10):
                    print("Invalid Input. Category ID should have 1 character and 9 digit.")
                else:
                    break
            name = input("Name: ")
            query = "UPDATE category SET NAME = %s WHERE CATEGORY_ID = %s"
            val = (name, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
        
        case 2:
            while True:
                id = input("Category ID: ")
                if(id[0]!="C"):
                    print("Invalid Input. Category ID should start with C.")
                elif(len(id)!=10):
                    print("Invalid Input. Category ID should have 1 character and 9 digit.")
                else:
                    break

            desc = input("Description: ")
            
            query = "UPDATE category SET DESCRIPTION = %s WHERE CATEGORY_ID = %s"
            val = (desc, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")

        case 3:
            while True:
                id = input("Category ID: ")
                if(id[0]!="C"):
                    print("Invalid Input. Category ID should start with C.")
                elif(len(id)!=10):
                    print("Invalid Input. Category ID should have 1 character and 9 digit.")
                else:
                    break

            name = input("Name: ")
            desc = input("Description: ")

            query = "UPDATE category SET NAME = %s, DESCRIPTION = %s, WHERE CATEGORY_ID = %s"
            val = (name, desc, id,)
            try:
                cursor.execute(query, val)
                cnx.commit()
                print("Update successful.")
            except:
                print("Update unsuccessful.")
                
    cursor.close()
    cnx.close()

def deleteCategory():
    cnx = DatabaseConnector.connect()
    while True:
        id = input("Category ID: ")
        if(id[0]!="C"):
            print("Invalid Input. Category ID should start with C.")
        elif(len(id)!=10):
            print("Invalid Input. Category ID should have 1 character and 9 digit.")
        else:
            break
    query = "UPDATE category SET STATUS = 0 WHERE CATEGORY_ID = %s"
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

def printCategory():
    cnx = DatabaseConnector.connect()
    query = "SELECT * FROM category WHERE STATUS = 1"
    results = DatabaseConnector.query(cnx, query)
    if results:
        for row in results:
            print(row)
    else:
        print("The category list is empty.")
    cnx.close()

def searchCategory():
    cnx = DatabaseConnector.connect()
    cursor = cnx.cursor()
    while True:
        id = input("Category ID: ")
        if(id[0]!="C"):
            print("Invalid Input. Category ID should start with C.")
        elif(len(id)!=10):
            print("Invalid Input. Category ID should have 1 character and 9 digit.")
        else:
            break
    query = "SELECT * FROM category WHERE CATEGORY_ID = %s"
    val = (id,)
    cursor.execute(query, val)
    try:
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result)
        else:
            print("Category not found")
    except:
        print("Category not found.")
    
    cursor.close()
    cnx.close()