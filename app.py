from flask import Flask
from datetime import datetime

app = Flask(__name__)

data = {
    "Fruit":[
        {
            "name": "Grape", 
            "description": "Delicious grape fruit drink",
            "date": datetime.now()
        },
        {
            "name": "Lemon", 
            "description": "Undiluted lemon fruit drink",
            "date": datetime.now()
        },
        {
            "name": "Mango", 
            "description": "This is a mango fruit",
            "date": datetime.now()
        }
    ]
}

@app.route("/")
def index():
        return "Welcome! Hello Tushar"

@app.route('/drinks')
def get_drinks():
    # Need datbase connection
    # fire query(select * from xyztable)
    # insert into xyz (id,name,gender) values(1,Tushar, Male)
    # read the data which is returned by query
    # return same data or filtered data
    return data

if __name__ == "__main__":
    app.debug = True
    app.run()