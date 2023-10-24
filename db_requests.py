import requests

class Req:
    def __init__(self, connect):
        self.connect = connect
        self.cur = connect.cursor()
        
    def show_for_author(self):
        self.cur.execute("""SELECT * FROM books WHERE author=%""", (author,))
        result = self.cur.fetchall()
        return result    