import urllib.request, urllib.parse, urllib.error
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('/home/rohit/Documents/Database/iTune.sqlite')
cur = conn.cursor()

cur.executescript('''
                    DROP TABLE IF EXISTS Artist;
                    DROP TABLE IF EXISTS Genre;
                    DROP TABLE IF EXISTS Album;
                    DROP TABLE IF EXISTS Track;
                    ''')
cur.executescript('''
                    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')

fname = input("Enter The file:")
if len(fname) < 1 :
    fname = '/home/rohit/Documents/tracks/Library.xml'
fh = open(fname)
file = fh.read()

tree = ET.fromstring(file)


stuff = tree.findall('dict/dict/dict')

def lookup(d,key):
    found = False
    for child in d:
        if found:return (child.text)
        if child.tag == 'key' and child.text == key :
            found = True
    return None


for item in stuff:

    if ( lookup(item, 'Track ID') is None ) :
        continue

    name = lookup(item, 'Name')
    genre = lookup(item, 'Genre')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    count = lookup(item, 'Play Count')
    rating = lookup(item, 'Rating')
    length = lookup(item, 'Total Time')

    if name is None or artist is None or album is None or genre is None :
        continue

    cur.execute('INSERT OR IGNORE  INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)', (artist_id , album,))
    cur.execute('SELECT id FROM Album WHERE title = ?' , (album,))
    album_id = cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE INTO Track (title , album_id, genre_id, len , rating , count ) VALUES (?,?,?,?,?,?)', (name,album_id,genre_id,length,rating,count,))
    conn.commit()

sqlstr = ('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')


for row in cur.execute(sqlstr):
    print((row[0],row[1],row[3]))

cur.close()
