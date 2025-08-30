from flask import Flask,redirect,render_template


app = Flask(__name__)






        
@app.route("/")
def first_page():
    return render_template("base.html")


@app.route("/Add recipe")
def recipe():
    return render_template("add_recipe.html")

app.run(debug=True)
