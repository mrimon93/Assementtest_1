print('Welcome Muzammil to the Assesment Test ')

import psycopg2
print("Welcome to the phone list, the following commands are available:")
print("LIST, ADD, DELETE, QUIT")
dbconn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="assessmentdb",
    user="postgres",
    password="Monasogsql@12")
def read_contacs(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.contacts;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_contacts(conn, name, lastname):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO public.contacts VALUES ('{name}', '{lastname}');")
    cur.execute("COMMIT;")
    cur.close()
    print(f"{name} added!")
def delete_contacts(conn, name):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM public.contacts WHERE name = '{name}';")
    cur.close()
    print(f"{name} deleted!")
def save_contacts(conn):
    cur = conn.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
while True: ## REPL - Read Execute Print Loop/Read Execute Program Loop
            ##https://codewith.mu/en/tutorials/1.1/repl
    cmd = input("Command: ")
    if cmd == "LIST":
        print(read_contacs(dbconn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_contacts(dbconn, name, lastname)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_contacts(dbconn, name)
    elif cmd == "QUIT":
        save_contacts(dbconn)
        print("Committing all changes to the database and quitting! Good bye!")
        exit()