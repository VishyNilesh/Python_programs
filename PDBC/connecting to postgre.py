import psycopg2
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Nilesh@2022")
crsor = con.cursor()
crsor.execute("CREATE TABLE Employee (emp_id SERIAL PRIMARY KEY,emp_name VARCHAR(255) NOT NULL);")
crsor.close()
con.close()