#from flask import Flask
from flask import Flask, request, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  
    #

   # def get(self):
   #     return {"data":"Hello World"}

    def get(self,name,test):
        return {"name":name, "test": test}

#    def get(self,age,name,country,language,medical_history,details):
#        return {"age":age, "name":name, "country": country, "language": language, "medical_history": medical_history, "details": details}

#api.add_resource(HelloWorld, "/helloworld")

api.add_resource(HelloWorld, "/<string:name>/<int:test>")

#api.add_resource(HelloWorld, "/<string:age>/<string:name>/<string:country>/<string:language>/<string:medical_history>/<string:details>/")


#class AskADoctor():


@app.route("/question", methods=["GET", "POST"])
def question():
    d = {}

    if request.method == "POST":
        age = request.form["age"]
        name = request.form["name"]
        country = request.form["country"]
        language = request.form["language"]
        medical_history = request.form["medical_history"]
        details = request.form["details"]

        print(age)
        print(name)
        print(country)
        print(language)
        print(medical_history)
        print(details)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
