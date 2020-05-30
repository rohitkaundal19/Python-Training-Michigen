import sqlite3
import json

conn = sqlite3.connect('/home/rohit/Documents/Database/Many_to_Many_JSON.sqlite')
cur = conn.cursor()

cur.executescript('''
                    DROP TABLE IF EXISTS User;
                    DROP TABLE IF EXISTS Course;
                    DROP TABLE IF EXISTS Member;
                    ''')

cur.executescript('''
                    CREATE TABLE User (
    id      INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT        UNIQUE
    );

CREATE TABLE Course (
    id       INTEGER    NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT       UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id , course_id)
    )
''')

fname = input("Enter The file:")
if len(fname) < 1 :
    fname = '/home/rohit/Documents/Sample Folder/roster_data.json'
fh = open(fname)
file = fh.read()

tree = json.loads(file)

for item in tree:

    name = item[0]
    course = item[1]
    role = item[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (course,))
    course_id = cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE INTO Member (user_id , course_id, role) VALUES (?,?,?)', (user_id , course_id , role))
    conn.commit()

sqlstr = ('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X''')


for row in cur.execute(sqlstr):
    print(row[0])

cur.close()
