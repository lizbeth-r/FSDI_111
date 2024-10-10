from flask import Flask

app = Flask(__name__)

@app.get("/")
def get_home():
    me = {
        "first_name": "Lizbeth",
        "last_name": "Ramirez",
        "hobbies": "Coffee shops",
        "is_online": True
    }

    return me
    
