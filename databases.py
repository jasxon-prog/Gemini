import sqlite3
from datetime import date

connection = sqlite3.connect('gemini.db')

cursor = connection.cursor()

def create_databases():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_attemp(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id VARCHAR(100),
        date DATE,
        attemps_count INTEGER DEFAULT 1    
        )
    """)
    connection.commit()
    
def check_user(chat_id):
    today = date.today().strftime('%Y-%m-%d')
    user = cursor.execute(
        'SELECT * FROM user_attemp WHERE chat_id = ? AND date = ?', 
        (chat_id, today)).fetchone()
    if user and user[3] <= 3:
        attemp_count = user[3] + 1
        cursor.execute('''
            UPDATE user_attemp SET attemps_count = ? WHERE chat_id = ?''', (attemp_count, chat_id))
        connection.commit()
        return True
    elif not user:
        cursor.execute("""
            INSERT INTO user_attemp (chat_id, date)
            VALUES (?, ?)           
            """, (chat_id, today))
        connection.commit()
        return True
    return False