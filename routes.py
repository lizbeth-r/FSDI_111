from flask import Flask

app = Flask(__name__)

@app.get("/aboutme")
def get_home():
    me = {
        "first_name": "Lizbeth",
        "last_name": "Ramirez",
        "hobby": "Visit Coffee shops",
        "is_online": True
    }

    return me
    
