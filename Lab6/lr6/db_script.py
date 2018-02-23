import MySQLdb

db = MySQLdb.connect(
	host="localhost",
	user="dbuser",
	passwd="123",
	db="first_db"
)

c = db.cursor()

db.set_character_set('utf8')
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')

c.execute("INSERT INTO lr6_horse (horse_name, horse_owner, horse_club) VALUES (%s, %s, %s);", ('Вьюга', 'Толстой', 'Грива и копыта'))
c.execute("UPDATE lr6_horse SET horse_owner = 'Пушкин' WHERE horse_owner = 'Толстой';")
db.commit()

c.execute("SELECT * FROM lr6_horse;")

entries = c.fetchall()

for entry in entries:
	print(entry)

c.close()
db.close()
