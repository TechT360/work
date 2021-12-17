from flask import request


def test_up(client):
    assert client.get("/").status_code == 200


def test_missing(client):
    assert client.get("/missing").status_code == 404


def test_correct_form(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'<form action=" /processform" method="POST">' in response.data
    assert response.data.startswith(b"<!DOCTYPE html>")
