"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import csv
import psycopg2

ORDERS = os.path.join('north_data', 'orders_data.csv')
EMPLOYEES = os.path.join('north_data', 'employees_data.csv')
CUSTOMERS = os.path.join('north_data', 'customers_data.csv')

with psycopg2.connect(host="localhost", database="north", user="postgres", password="12345") as conn:
    with conn.cursor() as cur:
        with open(EMPLOYEES) as csvfile:
            list_employees = csv.DictReader(csvfile, delimiter=',')
            for i in list_employees:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                            (i["employee_id"], i["first_name"], i["last_name"], i["title"], i["birth_date"], i["notes"])
                             )
        with open(CUSTOMERS) as csvfile:
            list_customers = csv.DictReader(csvfile, delimiter=',')
            for i in list_customers:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                            (i['customer_id'], i['company_name'], i['contact_name'])
                            )
        with open(ORDERS) as csvfile:
            list_orders = csv.DictReader(csvfile, delimiter=',')
            for i in list_orders:
                pass
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                            (i["order_id"], i["customer_id"], i["employee_id"], i["order_date"], i["ship_city"])
                            )


conn.close()
