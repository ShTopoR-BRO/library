from flask import Flask, request
from flask import jsonify
import psycopg2

connection = psycopg2.connect(user="postgres",password="190687",host="127.0.0.1",port="5432",database="library")



app = Flask(__name__)

@app.route('/api/books',methods = ["GET", "POST"])
def show_books():
    if request.method == "POST": 
        data = request.get_json()
        try:
            id = data["id"]
            book_name = data["book_name"]
            author = data["author"]
            
            connection = psycopg2.connect(user="postgres",password="190687",host="127.0.0.1",port="5432",database="library")

            cursor = connection.cursor()
            cursor.execute("INSERT INTO books VALUES(%s,%s,%s)", (id, book_name, author))
            connection.commit()
            cursor.close()
            connection.close()
            return {"massenge":"Книга Добавлена в библиотеку"}
        except Exception as e:
            print(e)
            return {"massenge":"oops"}
        
    elif request.method == "GET":
        connection = psycopg2.connect(user="postgres",password="190687",host="127.0.0.1",port="5432",database="library")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        q = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"massenge": q}

    
@app.route('/api/books/<int:post_id>', methods = ["DELETE"])
def delete_book(post_id):
    connection = psycopg2.connect(user="postgres",password="190687",host="127.0.0.1",port="5432",database="library")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s",(post_id,))
    connection.commit()
    cursor.close()
    return {"you want delete books whith id ":post_id}
    
@app.route('/api/books/<int:book_id>', methods = ["GET"])
def show_book(book_id): 
    connection = psycopg2.connect(user="postgres",password="190687",host="127.0.0.1",port="5432",database="library")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id= %s", (book_id,))
    q = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"this your book": q}     

if __name__ == '__main__':
    app.run()