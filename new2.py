from crypt import methods
from flask import Flask , request, jsonify
from pandas import json_normalize
app = Flask(__name__)
task = [
    {
        "id":1,
        "title":"Buy groceries",
        "description":"apple, banana",
        "done":False
    },
    {
        "id":2,
        "title":"learn python",
        "description":"learn python completely",
        "done":False
    },
    {
        "id":1,
        "title":"learn maths",
        "description":"learn maths completely",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data..."
        },400)
        t1 = {
            "id":task[-1]["id"]+1,
            "title":request.json["title"],
            "description":request.json.get("description",""),
            "done":False
        }
        task.append(t1)
        return jsonify({
            "status":"success",
            "message":"task added successfully"
        })

@app.route("/getdata")
def get_task():
    return jsonify({
        "data":task
    })

if (__name__=="__main__"):
    app.run(debug=True)