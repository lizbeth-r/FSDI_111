from flask import Flask

app = Flask(__name__)

@app.get("/aboutme")
def get_home():
    me = {
        "first_name": "LIZBETH",
        "last_name": "RAMIREZ",
        "hobby": "VISIT_COFFEE_SHOPS",
        # "is_online": True
    }

    return me
    
