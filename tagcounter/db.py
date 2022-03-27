import sqlite3
con = sqlite3.connect('tagsCounter.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tags_info (domain text, url text, created_at date, tags_dictionary text)''')

con.commit()
