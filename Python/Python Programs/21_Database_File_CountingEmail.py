import sqlite3

conn = sqlite3.connect('/home/rohit/Documents/Database/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input ("Enter the filename: ")
if len(fname) < 1:
    fname = '/home/rohit/Documents/Database/mbox.txt'

fh = open(fname)

for line in fh:

    if not line.startswith('From:'):
        continue
    line = line.split()
    email = line[1]

    cur.execute('SELECT count from Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row == None:
        cur.execute('INSERT INTO Counts (email,count) VALUES (?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE email = ?', (email,))

    conn.commit()

sqlstr = ('SELECT * from Counts ORDER BY count DESC LIMIT 10')

for row in cur.execute(sqlstr):
    print((row[0],row[1]))

cur.close()
