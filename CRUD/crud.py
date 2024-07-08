import pymysql
from pymysql import *
from tabulate import tabulate


def db_connect():
    return connect(host="localhost", user="root", passwd="admin123", db="python_fullstack")


def check_id_exists(empid):
    con = db_connect()
    try:
        cur = con.cursor()
        check_id = "select sid from student where sid=%s";
        cur.execute(check_id, (empid,))
        result = cur.fetchone()
        return result is not None

    except pymysql.Error as err:
        print(err)
    finally:
        cur.close()
        con.close()


def check_email_exists(email):
    con = db_connect()
    try:
        cur = con.cursor()
        check_email = "select email from student where email=%s";
        cur.execute(check_email, (email,))
        result = cur.fetchone()
        return result is not None

    except pymysql.Error as err:
        print(err)
    finally:
        cur.close()
        con.close()


def check_mobile_exists(mobile):
    con = db_connect()
    try:
        cur = con.cursor()
        check_email = "select mob from student where mob=%s";
        cur.execute(check_email, (mobile,))
        result = cur.fetchone()
        return result is not None

    except pymysql.Error as err:
        print(err)
    finally:
        cur.close()
        con.close()


def is_valid_mobile_number(mobile):
    return len(mobile) == 10 and mobile.isdigit() and mobile[0] in '6789'


def insert_data():
    con = db_connect()
    try:
        cur = con.cursor()

        # sid = int(input("Enter student ID = "))
        sname = input("Enter student Name = ")
        age = int(input("Enter the age = "))
        sadd = input("Enter the address = ")
        semail = input("Enter the email address = ")
        smob = input("Enter the mobile = ")
        if check_email_exists(semail):
            print("This email id is already exists.Please try another one")
            return
        elif check_mobile_exists(smob):
            print("This mobile number is already exists in database")
            return
        elif not is_valid_mobile_number(smob):
            print("Invalid mobile number. Please enter a 10-digit number starting with 6, 7, 8, or 9.")
            return
        else:
            insert_query = "insert into student(sname,age,sadd,email,mob) values(%s,%s,%s,%s,%s)"
            cur.execute(insert_query, (sname, age, sadd, semail, smob))
            con.commit()
            print("Data inserted successfully.")

    except pymysql.Error as err:
        print(err)
    finally:
        cur.close()
        con.close()


def update_data():
        connection = db_connect()
        try:
            cur = connection.cursor()
            stud_id = int(input("Enter Student ID to update: "))
            if not check_id_exists(stud_id):
                print("Student ID does not exist. Please try again.")
                return

            column = input("Enter the column to update (sname,age,sadd,email,mob): ")
            new_value = input(f"Enter the new value for {column}: ")

            if column == 'email' and check_email_exists(new_value):
                print("Email already exists. Please try again.")
                return

            if column == 'mob':
                if not is_valid_mobile_number(new_value):
                    print("Invalid mobile number. Please enter a 10-digit number starting with 6, 7, 8, or 9.")
                    return

            query = f"UPDATE student SET {column} = %s WHERE id = %s"
            cur.execute(query, (new_value, stud_id))
            connection.commit()
            print("Data updated successfully.")
        except pymysql.MySQLError as err:
            print(err)
        finally:
            cur.close()
            connection.close()


def delete_data():
    con = db_connect()
    try:
        cur = con.cursor()
        sid = int(input("Enter student id = "))
        if not check_id_exists(sid):
            print("This id does not exists. Please check id")
            return
        else:
            del_query = "delete from student where sid = %s"
            cur.execute(del_query, (sid,))
            con.commit()
            print("data deleted successfully")
    except pymysql.Error as err:
        print(err)
    finally:
        cur.close()
        con.close()


def search_data():
    con = db_connect()
    try:
        cur = con.cursor()
        searchRec = int(input("Enter student id = "))
        query = "select * from student where sid=%s"
        cur.execute(query, (searchRec,))
        result = cur.fetchall()
        headers = ["ID", "Name", "age", "Address"]
        print(tabulate(result, headers=headers, tablefmt="psql"))

    except MySQLError as err:
        print(err)

    finally:
        cur.close()
        con.close()


def getAllData():
    con = db_connect()
    try:
        cur = con.cursor()
        query = "select * from student where sid=%s"
        cur.execute(query)
        result = cur.fetchall()
        headers = ["ID", "Name", "age", "Address"]
        print(tabulate(result, headers=headers, tablefmt="psql"))

    except MySQLError as err:
        print(err)

    finally:
        cur.close()
        con.close()


def main_menu():
    while True:
        print("Please select your choice = ")
        print("1. Insert the record.")
        print("2. Update the record")
        print("3. Delete the record")
        print("4. Search the record")
        print("5. Get All Data")
        print("6. Exit")

        choice = input("Enter your choice = ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            update_data()
        elif choice == '3':
            delete_data()
        elif choice == '4':
            search_data()
        elif choice == '5':
            getAllData()
        elif choice == '6':
            confirm = input("Do you want to continue?yes or y or no or n = ")
            if confirm.lower() in ['yes', 'y']:
                pass
            else:
                break
        else:
            print("Invalid input")


main_menu()
