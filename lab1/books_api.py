"""Small SQLite API for the book collection database."""

from pathlib import Path
import sqlite3
from typing import Any, Dict, List, Optional


DATABASE_PATH = Path(__file__).with_name("books.db")
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db() -> None:
    """Create the database tables if they do not already exist."""
    with _connect() as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def add_author(name: str) -> int:
    """Create an author and return the generated Author_id."""
    if not name.strip():
        raise ValueError("Name must not be empty")

    with _connect() as connection:
        cursor = connection.execute("INSERT INTO author (Name) VALUES (?)", (name,))
        return int(cursor.lastrowid)


def get_author(author_id: int) -> Optional[Dict[str, Any]]:
    """Return one author by Author_id, or None when it does not exist."""
    with _connect() as connection:
        row = connection.execute(
            "SELECT Author_id, Name FROM author WHERE Author_id = ?", (author_id,)
        ).fetchone()
    return dict(row) if row else None


def list_authors() -> List[Dict[str, Any]]:
    """Return all authors ordered by Author_id."""
    with _connect() as connection:
        rows = connection.execute(
            "SELECT Author_id, Name FROM author ORDER BY Author_id"
        ).fetchall()
    return [dict(row) for row in rows]


def update_author(author_id: int, name: str) -> bool:
    """Update an author and return whether a record was changed."""
    if not name.strip():
        raise ValueError("Name must not be empty")

    with _connect() as connection:
        cursor = connection.execute(
            "UPDATE author SET Name = ? WHERE Author_id = ?", (name, author_id)
        )
    return cursor.rowcount > 0


def add_book(
    title: str,
    author_id: int,
    year: Optional[int] = None,
    rating: Optional[int] = None,
    read_it_or_not: bool = False,
) -> int:
    """Create a book and return the generated Book_id."""
    if not title.strip():
        raise ValueError("Title must not be empty")
    if rating is not None and rating not in range(1, 6):
        raise ValueError("Rating must be between 1 and 5")

    with _connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO book (Title, Author_id, Year, Rating, Read_it_or_not)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, author_id, year, rating, int(read_it_or_not)),
        )
        return int(cursor.lastrowid)


def get_book(book_id: int) -> Optional[Dict[str, Any]]:
    """Return one book by Book_id, or None when it does not exist."""
    with _connect() as connection:
        row = connection.execute(
            """
            SELECT Book_id, Title, Author_id, Year, Rating, Read_it_or_not
            FROM book WHERE Book_id = ?
            """,
            (book_id,),
        ).fetchone()
    return dict(row) if row else None


def list_books() -> List[Dict[str, Any]]:
    """Return all books ordered by Book_id."""
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT Book_id, Title, Author_id, Year, Rating, Read_it_or_not
            FROM book ORDER BY Book_id
            """
        ).fetchall()
    return [dict(row) for row in rows]


def update_book(
    book_id: int,
    title: str,
    author_id: int,
    year: Optional[int] = None,
    rating: Optional[int] = None,
    read_it_or_not: bool = False,
) -> bool:
    """Update a book and return whether a record was changed."""
    if not title.strip():
        raise ValueError("Title must not be empty")
    if rating is not None and rating not in range(1, 6):
        raise ValueError("Rating must be between 1 and 5")

    with _connect() as connection:
        cursor = connection.execute(
            """
            UPDATE book
            SET Title = ?, Author_id = ?, Year = ?, Rating = ?, Read_it_or_not = ?
            WHERE Book_id = ?
            """,
            (title, author_id, year, rating, int(read_it_or_not), book_id),
        )
    return cursor.rowcount > 0