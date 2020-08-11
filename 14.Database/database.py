import sqlite3

connection = sqlite3.connect('pyladies_example_1.db')
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS ROBOT""")

cursor.execute("""CREATE TABLE ROBOT (NAME TEXT, TYPE TEXT)""")

cursor.execute("""
	INSERT INTO ROBOT (NAME, TYPE)
	VALUES ("JIM", "DEFENSIVE"), ("JACK", "OFFENSIVE")
""")

robots = cursor.execute("SELECT * FROM ROBOT")
for robot in robots:
	print(robot)

connection.commit()
connection.close()
