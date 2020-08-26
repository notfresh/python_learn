import pymysql.cursors
import pymysql



def fake_data():
    _fake_data = []
    from faker import Faker
    fake = Faker()
    for i in range(10000):
        email = fake.email()
        while len(email) > 16:
            email = fake.email()
        _fake_data.append((email, fake.password(length=12)))
    return _fake_data


# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.executemany(sql, fake_data())
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()
