import sqlite3

class Workout_Model:
    def __init__(self,database):
        self.connection = sqlit3.connect(database)
        self.cursor = connection.cursor()
        
    def create(self):
        pass

    def read_all(self):
        pass

    def read(self,id):
        pass

    def update(self,id):
        pass

    def delete(self,id):
        pass
