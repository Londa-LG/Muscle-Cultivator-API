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
            id INT,
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
            id INT,
            slug VARCHAR,
            name VARCHAR,
            technique VARCHAR
            )
        """)

    def create_user(self):
        self.cursor.execute("""
        CREATE TABLE User(
            id INT,
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
            id INT,
            level INT,
            requirements VARCHAR,
            exercise VARCHAR,
            details VARCHAR
            )
        """)

    def create_progress(self):
        self.cursor.execute("""
        CREATE TABLE Progress(
            id INT,
            slug VARCHAR,
            user INT,
            workout VARCHAR
            )
        """)

    def create_achievement(self):
        self.cursor.execute("""
        CREATE TABLE Progress(
            id INT,
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
        
    def create(self):
        passs

    def read_all(self):
        pass

    def read(self,id):
        pass

    def update(self,id):
        pass

    def delete(self,id):
        pass
