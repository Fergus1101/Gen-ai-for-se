PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS author (
    Author_id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS book (
    Book_id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Author_id INTEGER NOT NULL,
    Year INTEGER,
    Rating INTEGER CHECK (Rating IS NULL OR Rating BETWEEN 1 AND 5),
    Read_it_or_not BOOLEAN NOT NULL DEFAULT 0 CHECK (Read_it_or_not IN (0, 1)),
    FOREIGN KEY (Author_id) REFERENCES author (Author_id)
);