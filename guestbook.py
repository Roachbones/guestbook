import json
import datetime
from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
import wtforms.validators as validators

app = Flask(__name__)
with open("secret_key") as file:
    app.config["SECRET_KEY"] = file.read()

@app.route("/home")
def root():
    return redirect("https://rose.systems", code=303)

@app.route("/", methods=["GET","POST"])
def guestbook():
    form = GuestbookForm()
    with open("signatures.json") as file:
        signatures = json.load(file)
    if form.validate_on_submit():
        print("valid submission received. :3")
        signature = {
            "name": request.form["name"],
            "message": request.form["message"],
            # time in ISO 8601 rounded to nearest minute
            "time": datetime.datetime.now().isoformat()[:16]
        }
        print(signature)
        signatures.insert(0, signature)
        with open("signatures.json", "w") as file:
            json.dump(signatures, file, indent=4)
        return redirect("/")
    else: # either a GET request or invalid submission
        return render_template(
            "guestbook.html",
            form=form,
            signatures=signatures
        )

class GuestbookForm(FlaskForm):
    name = StringField('name',
        validators=[
            validators.InputRequired(),
            validators.Length(max=255)
        ],
        render_kw = {"maxlength": 255}
    )
    message = TextAreaField('message',
        validators=[
            validators.InputRequired(),
            validators.Length(max=1000)
        ],
        render_kw = {
            "maxlength": 1000,
            "cols": 40,
            "rows": 6
        }
    )
    sentience = StringField(
        validators=[
            validators.InputRequired(),
            validators.Length(max=64),
            validators.AnyOf(
                ("cicada", "Cicada", "CICADA"),
                message="failed sentience check. type CICADA in the third box"
            )
        ],
        render_kw = {"maxlength": 64}
    )



    
    
