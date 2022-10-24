# pip install flask_restful
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
#flask_restful lib의 Resource 상속
names = {"nick":{"age":20, "gender":"male"}
         , "judy":{"age":25, "gender":"female"}}

class helloworld(Resource):
    def get(self, name):
        return names[name]

api.add_resource(helloworld, "/world/<string:name>")
if __name__ == '__main__':
    app.run(debug=True)