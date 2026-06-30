import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="portfolio_db"
    )
    return connection

def save_comment(comment):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO comments(comment)
    VALUES(%s)
    """

    cursor.execute(query, (comment,))
    conn.commit()

    cursor.close()
    conn.close()