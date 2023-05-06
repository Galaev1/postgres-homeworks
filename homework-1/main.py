"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv

customers = []

with open('north_data/customers_data.csv', 'r', encoding='UTF-8') as file:
    file_reader = csv.reader(file,delimiter=",")
    for c in file_reader:
        customers.append(tuple(c))

with psycopg2.connect(host='localhost',database='north',user='postgres',password='1973') as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers[1:])
        cur.execute('SELECT * FROM customers')
        rows = cur.fetchall()
        for row in rows:
            print(row)

cur.close()


employees = []

with open('north_data/employees_data.csv', 'r', encoding='UTF-8') as file:
    file_reader = csv.reader(file,delimiter=",")
    for e in file_reader:
        employees.append(tuple(e))

with psycopg2.connect(host='localhost',database='north',user='postgres',password='1973') as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s,%s, %s)', employees[1:])
        cur.execute('SELECT * FROM employees')
        rows = cur.fetchall()
        for row in rows:
            print(row)

cur.close()



orders = []

with open('north_data/orders_data.csv', 'r', encoding='UTF-8') as file:
    file_reader = csv.reader(file,delimiter=",")
    for o in file_reader:
        orders.append(tuple(o))

with psycopg2.connect(host='localhost',database='north',user='postgres',password='1973') as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s,%s, %s)', orders[1:])
        cur.execute('SELECT * FROM orders')
        rows = cur.fetchall()
        for row in rows:
            print(row)

cur.close()