import DBcm

config = {
    "host": "127.0.0.1",
    "database": "visitors",
    "user": "user",
    "password": "visitor",
}

SQL_INSERT = "insert into comments (Name, Email, Comments) values ( %s,%s, %s )"
SQL_GETSCORES = "select Name, Email, Comments from comments order by name desc"


def save_data(Name, Email, Comments):
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_INSERT, (Name, Email, Comments))


def process_data(the_Name, the_Email, the_comment):
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_GETSCORES)
        results = db.fetchall()
    where = results.index((the_Name, the_Email, the_Comments)) + 1
    how_many = len(results)

    return the_Name, the_Email, the_Comments, where, how_many, results
