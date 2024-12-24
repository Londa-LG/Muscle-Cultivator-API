import sqlite3

class Model:
    def __init__(self,database):
        connection = sqlite3.connect(database)
        self.cursor = connection.cursor()

        # Create tables
        self.create_workout()
        self.create_exercise()
        self.create_user()
        self.create_rating()
        self.create_progress()
        self.create_achievement()

    def create_workout(self):
        self.cursor.execute("""
        CREATE TABLE Workout(
            id INT PRIMARY KEY,
            slug VARCHAR,
            type VARCHAR,
            reps VARCHAR,
            sets VARCHAR,
            rest_time DECIMAL,
            day VARCHAR,
            date VARCHAR
            )
        """)
    
    def create_exercise(self):
        self.cursor.execute("""
        CREATE TABLE Exercise(
            id INT PRIMARY KEY,
            slug VARCHAR,
            name VARCHAR,
            technique VARCHAR
            )
        """)

    def create_user(self):
        self.cursor.execute("""
        CREATE TABLE User(
            id INT PRIMARY KEY,
            email VARCHAR,
            username VARCHAR,
            password VARCHAR,
            workouts VARCHAR,
            awards VARCHAR
            )
        """)

    def create_rating(self):
        self.cursor.execute("""
        CREATE TABLE Rating(
            id INT PRIMARY KEY,
            level INT,
            requirements VARCHAR,
            exercise VARCHAR,
            details VARCHAR
            )
        """)

    def create_progress(self):
        self.cursor.execute("""
        CREATE TABLE Progress(
            id INT PRIMARY KEY,
            slug VARCHAR,
            user INT,
            workout VARCHAR
            )
        """)

    def create_achievement(self):
        self.cursor.execute("""
        CREATE TABLE Achievement(
            id INT PRIMARY KEY,
            slug VARCHAR,
            name VARCHAR,
            details VARCHAR,
            requirements VARCHAR
            )
        """)

class Workout_Model:
    def __init__(self):
        connection = sqlite3.connect("app.db")
        self.cursor = connection.cursor()

        
    def create(self,values):
        self.cursor.execute(f"""
           INSERT INTO Workout VALUES(
                {{values[0]}},
                {{values[1]}},
                {{values[2]}},
                {{values[3]}},
                {{values[4]}},
                {{values[5]}},
                {{values[6]}},
                {{values[7]}},
                {{values[8]}}
           )
        """)

    def read_all(self):
        self.cursor.execute(f"""
            SELECT * 
            FROM Workout
        """)

    def read(self,id):
        self.cursor.execute(f"""
            SELECT * 
            FROM Workout
            WHERE id = {{id}}
        """)

    def update(self,id,values):
        self.cursor.execute(f"""
           UPDATE Workout
            SET slug =  {{values[1]}},
            SET type =  {{values[2]}},
            SET split =  {{values[3]}},
            SET reps =  {{values[4]}},
            SET sets =  {{values[5]}},
            SET rest_time =  {{values[6]}},
            SET day =  {{values[7]}},
            SET date =  {{values[8]}},
            WHERE id = {{id}}
        """)

    def delete(self,id):
        self.cursor.execute(f"""
            DELETE FROM Workout
            WHERE id={{id}}
        """)
