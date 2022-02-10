from flask import request
from werkzeug.wrappers import response


def test_home(client):
    assert client.get("/").status_code == 200


def test_correct_form(client):
    response = client.get("/form")
    assert response.status_code == 200
    # response.data is a binary text version of the html page.
    assert b'<form action="/processform" method="POST">' in response.data

def test_form_operation(client):
    response = client.get("/form")
    form_data = {
        "Name": "john",
        "Email": "john@gmail.com",
        "Comments": "work",

    }
    response = client.post("/processform", data=form_data)
    assert response.status_code == 200
    resp = response.data
    assert bytes(form_data["Name"], encoding="utf-8") in resp
    assert bytes(form_data["Email"], encoding="utf-8") in resp
    assert bytes(form_data["Comments"], encoding="utf-8") in resp


def test_computers(client):
    assert client.get("/computer").status_code == 200


def test_cv(client):
    assert client.get("/cv").status_code == 200


def test_form(client):
    assert client.get("/form").status_code == 200


def test_interest(client):
    assert client.get("/interest").status_code == 200


def test_personalpage(client):
    assert client.get("/personalpage").status_code == 200


def test_visitors(client):
    # these are the visitors
    assert client.get("/visitors").status_code == 200


def test_comments(client):
    # the comments made by the visitors
    assert client.get("/Comments").status_code == 200
