import os

where = os.uname().release.find("aws")

if where == -1:
    # Not on PA.
    config = {
        "host": "127.0.0.1",
        "database": "visitors",
        "user": "user",
        "password": "visitor",
    }
else:
    # Local.
    config = {
        "host": "c00241029.mysql.pythonanywhere-services.com",
        "database": "c00241029$visitors",
        "user": "c00241029",
        "password": "visitors",
    }
