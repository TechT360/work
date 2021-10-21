from flask import Flask, render_template, request

from data_utils import save_data, get_data

app = Flask(__name__)


@app.route("/")
def display_home():
    return render_template(
        "home.html",
        the_title="Home page",
        the_opening_title="Welcome to Terry's Webpage",
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


@app.route("/computers")
def display_computer():
    return render_template(
        "computers.html",
        the_title="My computer technology page",
        the_opening_title="Computers",
    )


@app.route("/comments", methods=["POST"])
def display_comments():
    data = request.form
    save_data(data)
    return render_template(
        "thanks.html",
        the_title="Thank you!",
        the_opening_title="Thanks for you data",
        the_name=data["email"],
    )


@app.route("/showdata")
def display_all_visitors():
    data = get_data()
    return render_template(
        "visitors.html",
        the_title="List of Visitors",
        the_opening_title="List of visitors",
        the_data=data,
    )
