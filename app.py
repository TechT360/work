from flask import Flask, request, render_template
import datetime

app = Flask(__name__)


@app.get("/")  # HTTP request:   GET  /
def index():
    return render_template("index.html",
                           title="Welcome!",
                           heading="Tell us about yourself",)


@app.get("/showform")
def display_form():
    """
        Retrieve the form.html file from the hard disk, and send it to the
        browser.
    """
    return render_template("form.html",
                           title="Welcome Form",
                           heading="Please fill in this form",)


@app.post("/processform")
def save_data():
    """
        Receive the data from the HTML form, then save it to a disk file, then respond
        with a nice friendly message to the awaiting browser.

        The following inputs are expected: first, last, and dob.
    """
    # python-name = html-name:
    the_first = request.form["first"]
    the_last = request.form["last"] 
    the_dob = request.form["dob"] 
    # So... now, use the python-names in your code:
    with open("suckers.txt", "a") as sf:
        print(f"{the_first}, {the_last}, {the_dob}", file=sf)
    return f"Thanks, {the_first}, we promise not to sell your data to the bad guys."    


if __name__ == "__main__":
    app.run(debug=True)
