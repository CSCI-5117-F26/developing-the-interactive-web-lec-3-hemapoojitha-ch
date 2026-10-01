from flask import Flask, request, redirect, render_template

app = Flask(__name__)

names = []

@app.route("/", methods=["GET"]) 
def index():
    return render_template("index.html", names=names)


@app.route("/add", methods=["POST"])
def add_name():
    # global names
    name = request.form.get("name")

    if name:
        names.append(name)

    return redirect("/")

if __name__ == "__main__":
    app.run()
    