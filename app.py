from flask import Flask, request, render_template
import datetime

app = Flask(__name__)


@app.get("/")  # HTTP request:   GET  /
def index():
    return render_template(
        "home.html", title="Welcome to the home page", heading="Tell us about yourself"
    )


@app.route("/personalpage")
def display_personalpage():
    return render_template(
        "personalpage.html",
        the_title="My personal page",
        the_opening_title="Welcome to Terry's Personal page",
    )


@app.route("/cv")
def display_cv():
    return render_template(
        "cv.html", the_title="My CV page", the_opening_title="This is Terry's CV page"
    )


@app.route("/interest")
def display_interest():
    return render_template(
        "interest.html",
        the_title="My interests page",
        the_opening_title="Terry's Interests",
    )


@app.route("/computer")
def display_computer():
    return render_template(
        "computers.html",
        the_title="My computer technology page",
        the_opening_title="Computers",
    )


@app.get("/form")
def display_form():
    """
        Retrieve the form.html file from the hard disk, and send it to the
        browser.
    """
    return render_template(
        "form.html", title="Feedback Form", heading="Please fill in this form"
    )


@app.post("/processform")
def save_date():
    # python-name = html-name:
    Name = request.form["Name"]
    Email = request.form["Email"]
    Comments = request.form["Comments"]
    # So... now, use the python-names in your code:
    with open("Comments.txt", "a") as sf:
        print(f"{Name}, {Email}, {Comments}", file=sf)
    return render_template(
        "Comments.html",
        name=Name,
        heading="we promise not to sell your data to bad guys",
    )


if __name__ == "__main__":
    app.run(debug=True)
