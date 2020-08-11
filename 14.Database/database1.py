import sqlite3

connection = sqlite3.connect('pyladies_example_2.db')
cursor = connection.cursor()
cursor.execute("""DROP TABLE IF EXISTS ROBOT""")
cursor.execute("""DROP TABLE IF EXISTS BATTLE""")


cursor.execute("""
CREATE TABLE ROBOT (
    ROBOT_ID INT PRIMARY KEY,
    NAME TEXT,
    TYPE TEXT)
""")

cursor.execute("""
CREATE TABLE BATTLE (
    BATTLE_ID INT PRIMARY KEY,
    WINNER_ID INT,
    LOSER_ID INT,
    WINNER_POINTS INT,
    LOSER_POINTS INT,
    FOREIGN KEY(WINNER_ID) REFERENCES ROBOT(ROBOT_ID),
    FOREIGN KEY(LOSER_ID) REFERENCES ROBOT(ROBOT_ID)
    )
""")

cursor.execute("""
    INSERT INTO ROBOT (ROBOT_ID, NAME, TYPE) VALUES
    (1, "JIM", "DEFENSIVE"), (2, "JACK", "OFFENSIVE"), (3, "JIMMY", "OFFENSIVE")
""")

cursor.execute("""
    INSERT INTO BATTLE (BATTLE_ID, WINNER_ID, LOSER_ID, WINNER_POINTS, LOSER_POINTS) VALUES
    (1, 1, 2, 10, 8),
    (2, 2, 1, 6, 9),
    (3, 2, 3, 10, 9),
    (4, 1, 3, 5, 4),
    (5, 3, 2, 2, 0),
    (6, 1, 2, 9, 6)
""")

scores = cursor.execute("""
    SELECT BATTLE.WINNER_POINTS, BATTLE.LOSER_POINTS
    FROM BATTLE
    JOIN ROBOT ON ROBOT.ROBOT_ID = BATTLE.WINNER_ID
    WHERE ROBOT.NAME = "JIM"
""")

for score in scores:
    print(score)

connection.commit()
connection.close()
