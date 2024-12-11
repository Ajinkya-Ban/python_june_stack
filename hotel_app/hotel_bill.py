import pymysql as pysql
from dotenv import load_dotenv
import os
from tabulate import tabulate

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
        category_name = input("Enetr the name of the category = ").capitalize().strip()
        cursor.execute("select count(*) from category where name=%s", (category_name))
        if cursor.fetchone()[0] > 0:
            print(f"Category {category_name} already exist")
        else:
            cursor.execute("insert into category(name) values(%s)", (category_name))
            commit_and_message(cursor, db, "Date inserted successfully")
            display_category(cursor, db)
            if input("Do you want to add another category name?yes/no = "):
                break


def update_category(cursor, db):
    category_id = int(input("Enter the category id = "))
    updated_name = input("Enter the new name = ").strip().capitalize()
    cursor.execute("update category set name = %s where id=%s", (updated_name, category_id))
    commit_and_message(cursor, db, "one record updated.")
    display_category(cursor, db)


def delete_category(cursor, db):
    category_id = int(input("Enter the category id = "))
    cursor.execute("delete from category where id = %s", (category_id))
    commit_and_message(cursor, db, "One record deleted.")
    display_category(cursor, db)

def display_category(cursor, db):
    cursor.execute("select * from category")
    result = cursor.fetchall()
    columns = ["Cid", "Category Name"]
    print(tabulate(result, tablefmt="psql", headers=columns, missingval="NA"))

def catetgory_menu(cursor, db):
    while True:
        print("\n Category Menu")
        print("1. Add Category")
        print("2. Update Category")
        print("3. Delete Category")
        print("4. Display Category")
        print("5. Exit to main Menu")
        choice = input("Enter your choice = ")
        if choice == "1":
            add_category(cursor, db)
        elif choice == "2":
            update_category(cursor, db)
        elif choice == "3":
            delete_category(cursor, db)
        elif choice == "4":
            display_category(cursor, db)
        elif choice == "5":
            break
        else:
            print("Invalid choice.Please enter option between 1 to 4.")


# ------------------------> Code for products -------------------------->
def add_product(cursor, db):
    while True:
        pname = input("Enter the product name = ").strip().capitalize()
        cid = int(input("Enter the category id = "))
        price = float(input("Enter the price = "))
        cursor.execute("select count(*) from products where name=%s", (pname))
        if cursor.fetchone()[0] > 0:
            print(f"Product {pname} already exist")
        else:
            cursor.execute("insert into products(name,id,price) values(%s,%s,%s)", (pname, cid, price))
            commit_and_message(cursor, db, "Data inserted successfully")
            display_products(cursor,db)
            if input("Do you want to add another product?yes/no = "):
                break
def update_products(cursor, db):
    p_id = int(input("Enter the product id = "))
    updated_name = input("Enter the product name = ").strip().capitalize()
    updated_cid = int(input("Enter the category id = "))
    updated_price = float(input("Enter the price  = "))
    cursor.execute("update products set name = %s, id=%s, price=%s where pid=%s", (updated_name,updated_cid,updated_price,p_id))
    commit_and_message(cursor, db, "one product updated.")
    display_products(cursor,db)


def delete_products(cursor, db):
    p_id = int(input("Enter the product id = "))
    cursor.execute("delete from products where pid = %s", (p_id))
    commit_and_message(cursor, db, "One record deleted.")
    display_products(cursor, db)

def display_products(cursor,db):
    cursor.execute("select * from products")
    result = cursor.fetchall()
    columns = ["Pid", "Product Name", "Category Id", "Price"]
    print(tabulate(result,tablefmt="psql",headers=columns,missingval="NA"))

def product_menu(cursor, db):
    while True:
        print("\n Product Menu")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Display Products")
        print("5. Exit to main Menu")
        choice = input("Enter your choice = ")
        if choice == "1":
            add_product(cursor, db)
        elif choice == "2":
            update_products(cursor, db)
        elif choice == "3":
            delete_products(cursor, db)
        elif choice == "4":
            display_products(cursor, db)
        elif choice == "5":
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
        elif choice == '2':
            product_menu(cursor,db)

        elif choice == '4':
            break
        else:
            print("Select the choce between 1 to 4")
    cursor.close()
    db.close()


if __name__ == "__main__":
    main_menu()
