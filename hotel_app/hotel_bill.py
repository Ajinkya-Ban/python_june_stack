import pymysql as pysql
from dotenv import load_dotenv
import os

load_dotenv()
mypassword = os.getenv("db_password")


def connect_db():
    return pysql.connect(host="localhost", user="root", passwd=mypassword, database="hotel_app")


def commit_and_message(cursor, db, message):
    db.commit()
    print(message)


# -----------------------Add category code start here-------------------------------

def add_category(cursor, db):
    while True:
        category_name = input("Enetr the name of the category = ")
        cursor.execute("insert into category(name) values(%s)", (category_name))
        commit_and_message(cursor, db, "Date inserted successfully")
        if input("Do you want to add another category name?yes/no = "):
            break


def update_category(cursor, db):
    category_id = int(input("Enter the category id = "))
    updated_name = input("Enter the name = ")
    cursor.execute("update category set name = %s where id=%s", (updated_name, category_id))
    commit_and_message(cursor, db, "one record updated.")


def delete_category(cursor, db):
    category_id = int(input("Enter the category id = "))
    cursor.execute("delete from category where id = %s", (category_id))
    commit_and_message(cursor, db, "One record deleted.")


def catetgory_menu(cursor, db):
    while True:
        print("\n Category Menu")
        print("1. Add Category")
        print("2. Update Category")
        print("3. Delete Category")
        print("4. Exit to main Menu")
        choice = input("Enter your choice = ")
        if choice == "1":
            add_category(cursor, db)
        elif choice == "2":
            update_category(cursor, db)
        elif choice == "3":
            delete_category(cursor, db)
        elif choice == "4":
            break
        else:
            print("Invalid choice.Please enter option between 1 to 4.")


# -------------------------->Code for main menu------------------------------------>
def main_menu():
    db = connect_db()
    cursor = db.cursor()
    while True:
        print("\n Main Menu")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Orders")
        print("4. Exit from Main menu")
        choice = input("Enter your choice = ")
        if choice == '1':
            catetgory_menu(cursor, db)
        elif choice == '4':
            break
        else:
            print("Select the choce between 1 to 4")
    cursor.close()
    db.close()


if __name__ == "__main__":
    main_menu()
