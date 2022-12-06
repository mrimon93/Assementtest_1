print('Welcome Muzammil to the Assesment Test ')
#This is from the branch
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
def add_contacts(conn,id, first_name, last_name,title,organization):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO public.contacts VALUES ('{id}','{first_name}', '{last_name}','{title}','{organization}');")
    cur.execute("COMMIT;")
    cur.close()
def delete_contacts(conn, id):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM public.contacts WHERE id = '{id}';")
    cur.execute("COMMIT;")
    cur.close()
def save_contacts(conn):
    cur = conn.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()



while True:
    cmd = input("Command: ")
    if cmd == "LIST":
        print(read_contacs(dbconn))
    elif cmd == "ADD":
        id= input('Enter Id number after 7 ')
        first_name = input("  Name: ")
        last_name = input("  Lastname: ")
        title = input('Your Title? ')
        organization = input('Where do your work? ')
        add_contacts(dbconn,id, first_name, last_name,title,organization)
    elif cmd == "DELETE":
        id = input("  id: ")
        delete_contacts(dbconn, id)
    elif cmd == "QUIT":
        save_contacts(dbconn)
        print("Committing all changes to the database and quitting! Good bye!")
        exit()