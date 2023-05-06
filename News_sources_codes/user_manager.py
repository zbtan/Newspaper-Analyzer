import mysql.connector


def findLargestID():

    #establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # create a cursor object
    cursor = connection.cursor()

    # execute a SQL query to find the largest id value
    query = "SELECT MAX(USER_ID) FROM users"
    cursor.execute(query)

    # fetch the result and extract the largest id value
    result = cursor.fetchone()

    try:
        max_id = result[0]
    except TypeError:
        # if no id value is found, assign a default value of "A0001"
        max_id = "U000000001"

    

    # close the cursor and database connection
    cursor.close()
    connection.close()

    return max_id

class User:
    def __init__(self, USER_ID, NAME, GENDER, AGE, EMAIL, STATUS, USERNAME, PASSWORD):
        self.USER_ID = USER_ID
        self.NAME = NAME
        self.GENDER = GENDER
        self.AGE = AGE
        self.EMAIL = EMAIL
        self.STATUS = STATUS
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD


def insert(user):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        cursor = connection.cursor()
        # Preparing SQL query to INSERT a record into the database. 
        sql = ("INSERT INTO users (USER_ID, NAME, GENDER, AGE, EMAIL, STATUS, USERNAME, PASSWORD)" 
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        user.USER_ID = findLargestID()
        data = (user.USER_ID, user.NAME, user.GENDER, user.AGE, user.EMAIL, user.STATUS, user.USERNAME, user.PASSWORD)


        # Executing the SQL command
        cursor.execute(sql, data)
        
        # Commit your changes in the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()


    except:
        # Rolling back in case of error
        connection.rollback()

        print("Data inserted")

        # Closing the connection
        connection.close()

def update(user):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to update the admin object with the given adminID
        query = "UPDATE users SET NAME = %s, GENDER = %s, AGE = %s, EMAIL = %s, STATUS = %s, USERNAME = %s, PASSWORD = %s WHERE USER_ID = %s"
        values = (user.NAME, user.GENDER, user.AGE, user.EMAIL, user.STATUS, user.USERNAME, user.PASSWORD, user.USER_ID)

        cursor.execute(query, values)

        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print(f"Error: {error}")


def delete(user):
    try:
        #establishing the connection
        connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
        # create a cursor object
        cursor = connection.cursor()

        # execute a SQL query to update the user object with the given userID
        query = "UPDATE users SET STATUS = 0 WHERE USER_ID = %s"
        values = (user.USER_ID,)
        cursor.execute(query, values)


        # commit the changes to the database
        connection.commit()

        # close the cursor and database connection
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")

def get(username, password):
    #establishing the connection
    connection = mysql.connector.connect(host="localhost", user="root", passwd="password123", database="newspaper_analyzer")
    # create a cursor object
    cursor = connection.cursor()

    # execute a SQL query to find the admin object with the given adminID
    query = "SELECT * FROM users WHERE USERNAME = %s AND PASSWORD = %s"
    values = (username, password)
    cursor.execute(query, values)

    # fetch the result and create an Admin object
    result = cursor.fetchone()

    if result is None:
        return None

    USER_ID, NAME, GENDER, AGE, EMAIL, STATUS, USERNAME, PASSWORD = result
    user = User(USER_ID, NAME, GENDER, AGE, EMAIL, STATUS, USERNAME, PASSWORD)

    # close the cursor and database connection
    cursor.close()
    connection.close()

    return user

