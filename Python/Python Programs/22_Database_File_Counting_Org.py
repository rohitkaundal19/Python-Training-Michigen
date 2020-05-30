import sqlite3

conn = sqlite3.connect('/home/rohit/Documents/Database/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input ("Enter the filename: ")
if len(fname) < 1:
    fname = '/home/rohit/Documents/Database/mbox.txt'

fh = open(fname)

for line in fh:

    if not line.startswith('From:'):
        continue
    line = line.split()
    email = line[1]
    email = email.split('@')
    domain  = email[1]

    #print (email)

    cur.execute('SELECT count from Counts WHERE org = ?', (domain,))
    row = cur.fetchone()

    if row == None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (domain,))

    conn.commit()

sqlstr = ('SELECT * from Counts ORDER BY count DESC LIMIT 10')

for row in cur.execute(sqlstr):
    print((row[0],row[1]))

cur.close()
