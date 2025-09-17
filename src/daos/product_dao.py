"""
Product DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
import mysql.connector
from models.product import Product

class ProductDAO:
    def __init__(self):
        try:
            load_dotenv()
            db_host = os.getenv("MYSQL_HOST")
            db_name = os.getenv("MYSQL_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")     
            self.conn = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)   
            self.cursor = self.conn.cursor()
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        self.cursor.execute("SELECT id, name, brand, price FROM products")
        rows = self.cursor.fetchall()
        return [Product(*row) for row in rows]
    
    def update(self, product: Product):
        self.cursor.execute(
            "UPDATE products SET name=%s, brand=%s, price=%s WHERE id=%s",
            (product.name, product.brand, product.price, product.id)
        )
        self.conn.commit()

    def insert(self, product):
        self.cursor.execute(
            "INSERT INTO products (name, brand, price) VALUES (%s, %s, %s)",
            (product.name, product.brand, product.price)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def delete(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
        self.conn.commit()

    def delete_all(self): #optional
        """ Empty products table in MySQL """
        sql = "DELETE FROM products"
        self.cursor.execute(sql)
        self.conn.commit()

        pass
        
    def close(self):
        self.cursor.close()
        self.conn.close()
