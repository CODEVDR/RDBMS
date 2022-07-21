import mysql.connector as sqlctr

# variables
pw = input("Enter Password : ")


def connect_server():
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pw
        )
    except:
        print("Error")
    return connection, pw


def connect_database(pasword):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pasword,
            database="railways_db"
        )
    except:
        pass
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


q1 = f"create database if not exists railways_db;"
cnecn = connect_server()
execute_query(cnecn[0], q1)
cnecn1 = connect_database(pw)
if __name__=="__main__":
    q0 = """use railways_db;"""
    q1 = """drop table if exists train;"""
    q2 = f"""create table if not exists train (train_name varchar(150)  NOT NULL,train_no int(5) NOT NULL,  total_seats int(255),1stclass_fare int(255),2ndclass_fare int(255),3rdclass_fare int(255));"""
    q3 = """insert into train values("Intercity",120023,2000,3000,2000,1000);"""
    q4 = """insert into train values("Rajdhani",820736,2000,5500,4500,2000);"""
    q5 = """insert into train (train_name,train_no,total_seats,1stclass_fare) values("Shatabdi",360782,800,2500);"""
    q6 = """insert into train values("Garib Rath",481577,2000,3500,2500,1000);"""
    q7 = """insert into train values("Duronto",683088,2000,6500,5400,3500);"""
    execute_query(cnecn1, q0)
    execute_query(cnecn1, q1)
    execute_query(cnecn1, q2)
    execute_query(cnecn1, q3)
    execute_query(cnecn1, q4)
    execute_query(cnecn1, q5)
    execute_query(cnecn1, q6)
    execute_query(cnecn1, q7)
q1 = f"""create table if not exists bookings (name varchar(150)  NOT NULL,train_name varchar(50) NOT NULL,train_no int(50) NOT NULL,age int(12),gender varchar(2),pass_concession varchar(2),class varchar(30));"""
execute_query(cnecn1, q1)
