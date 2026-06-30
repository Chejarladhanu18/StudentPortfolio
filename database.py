import mysql.connector

def get_connection():

    connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="root123",

        database="portfolio_db"

    )

    return connection


def save_comment(name,email,comment):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO comments(name,email,comment)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query,(name,email,comment))

    conn.commit()

    cursor.close()

    conn.close()