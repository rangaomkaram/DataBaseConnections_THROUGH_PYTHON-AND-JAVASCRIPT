import psycopg2 as psql

try:
    conn = psql.connect(host='localhost',
                        dbname = 'BIKE',
                        user = 'postgres',
                        password = 'Ranga@1993!',
                        port =5432)
    
    cur1 = conn.cursor()
    
    create_script = '''CREATE TABLE IF NOT EXISTS STORES (
                        id int PRIMARY KEY,
                        name varchar(40) NOT NULL,
                        Rental_Cost int,
                        dept_id varchar(30)
                        )'''

    cur1.execute(create_script)

    cur2 = conn.cursor()
    
    #cur2.execute('SELECT * FROM public."Sales_Store" LIMIT 100')



    #for record in cur2.fetchall():
        #print(record)

    #cur2.execute('SELECT DISTINCT "Age_Group" FROM public."Sales_Store"')

    cur2.execute("select COLUMN_NAME from information_schema.columns\
            where table_name='Sales_Store'")

    


    for rec in cur2.fetchall():
        print(rec)

except Exception as error:
    print(error)

finally:
    if cur1 is not None:
        cur1.close()
    if cur2 is not None:
        cur2.close()
    if conn is not None:
        conn.close()

