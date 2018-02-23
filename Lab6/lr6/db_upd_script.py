import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        # открытие соединения
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        # закрытие соединения
        if self._connection:
            self._connection.close()


class lr6_horse:
    def __init__(self, db_connection, horse_name, horse_owner, horse_club):
        self.db_connection = db_connection.connection
        self.horse_name = horse_name
        self.horse_owner = horse_owner
        self.horse_club = horse_club

    @staticmethod
    def getall(con):
        c = con.connection.cursor()
        c.execute('SET NAMES utf8;')
        c.execute('SET CHARACTER SET utf8;')
        c.execute('SET character_set_connection=utf8;')
        c.execute("SELECT * FROM lr6_horse")
        entries = c.fetchall()
        horses = []
        for entry in entries:
            id, name, owner, club = entry
            object = lr6_horse(con, name, owner, club)
            horses.append(object)
        return horses



    def save(self):
        c = self.db_connection.cursor()

        self.db_connection.set_character_set('utf8')
        c.execute('SET NAMES utf8;')
        c.execute('SET CHARACTER SET utf8;')
        c.execute('SET character_set_connection=utf8;')

        c.execute("INSERT INTO lr6_horse (horse_name, horse_owner, horse_club) VALUES (%s, %s, %s);",
                  (self.horse_name, self.horse_owner, self.horse_club))
        self.db_connection.commit()
        c.close()


con = Connection("dbuser", "123", "first_db")

with con:
    print(lr6_horse.getall(con))
    horse = lr6_horse(con, "Звездочка", "Галкин", "МГТУ им. Баумана")
    horse.save()

    horse = lr6_horse(con, "Радуга", "Ужбанов", "Чистое небо")
    horse.save()

    horse = lr6_horse(con, "Маргарита", "Ихимов", "Шустрые ангелы")
    horse.save()