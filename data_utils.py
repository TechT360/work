import DBcm

config = {
    'host': '127.0.0.1',
    'database' : 'visitorDB',
    'user' : 'visitors',
    'password': 'visitor',
}

SQL_INSERT = "insert into comments (name, comment) values ( %s, %s )"
SQL_GETSCORES = "select name, comment from comments order by name desc"


def save_data(name, comment):
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_INSERT, (name, comment,))


def process_data(the_name, the_comment):
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_GETSCORES)
        results = db.fetchall()
    where = results.index((the_name, the_comment)) + 1
    how_many = len(results)

    return the_name, the_comment, where, how_many, results