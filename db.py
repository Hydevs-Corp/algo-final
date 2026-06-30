import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='sentiment_db',
            user='root',
            password='root'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        return None

def fetch_all_tweets():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tweets")
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erreur lors de la récupération des tweets: {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return []
