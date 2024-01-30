from flask import Flask , render_template, request
import pickle
app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("index.html")

@app.route("/predict", methods=["post"])
def fun2():
    nm=request.form['name']
    age = int(request.form['age'])
    Gender = request.form['Gender']
    bmi = float(request.form['bmi'])
    number_child = int(request.form['number_child'])
    smoker = request.form['smoker']

    Gender=0 if Gender.lower()=='male' else 1
    smoker=0 if smoker.lower()=='yes' else 1

    q = [[age, Gender, bmi, number_child, smoker]]

    mymodel = pickle.load(open("final_model1.pkl", "rb"))
    premium = round(mymodel.predict(q)[0], 2)

    return render_template("second.html",name=nm, premium=premium)

if __name__ == '__main__':
    app.run(debug=True)

