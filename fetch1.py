"""fetch1.py"""

import mysql.connector 
from mysql.connector import Error 
 
try: 
    with mysql.connector.connect( 
        host='localhost', 
        user='root', 
        password='rootroot' 
    ) as connection: 
         
        if connection.is_connected(): 
            print("Подключение к MySQL установлено.") 
 
            with connection.cursor() as cursor: 
 
                cursor.execute("CREATE DATABASE IF NOT EXISTS HomeWorkDB") 
                print("База данных HomeWorkDB создана.") 
 
                cursor.execute("USE HomeWorkDB") 
 
                cursor.execute(""" 
                               CREATE TABLE IF NOT EXISTS Salary( 
                               id INT AUTO_INCREMENT PRIMARY KEY, 
                               title VARCHAR(255) NOT NULL
                               );
                               """) 
                print("Таблица Salary создана.") 
 
                insert_query = """ 
                INSERT INTO Salary (title) 
                VALUES (%s) 
                """ 
                records = [ 
                    ('10000$'), 
                    ('15000$'), 
                    ('20000$') 
                ] 
                cursor.executemany(insert_query,records) 
                connection.commit() 
                print(f"Вставлено {cursor.rowcount} записей в таблицу Salary.") 
 
                cursor.execute("SELECT * FROM Salary") 
                rows = cursor.fetchall() 
                print("Данные из таблицы Salary:") 
                for row in rows: 
                    print(row) 
 
except Error as e: 
    print(f"Ошибка при подключнии к MySQL: {e}") 
 
print("Соединение с MySQL закрыто.")