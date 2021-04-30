from flask import Flask
from flask_cors import CORS, cross_origin
from news import News
import json

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content_Type"


@app.route("/")
@cross_origin()
def get_data():
    content = News().nationsAppearance()
    print(content)
    return json.dumps(content, ensure_ascii=False)
