import sqlite3
con = sqlite3.connect(':memory:')
cursor = con.cursor()

cursor.execute('''CREATE TABLE tags_info (domain text, url text, created_at date, tags_dictionary text)''')

con.commit()
