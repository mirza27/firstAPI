from os import uname_result
from flask import Flask, request
from flask_restful import Resource, Api 
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

identitas = {}



# membuat class untuk resource
class SumberDaya(Resource):
    def get(self):
        respon = {"pesan": "dunia"}
        return identitas    
        
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]

        identitas["nama"] = nama
        identitas["umur"] = umur

        respon = {"pesan": "data diupload"}
        return respon

api.add_resource(SumberDaya, "/buatapi", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005) 