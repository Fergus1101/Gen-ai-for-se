"""Example client for books_api.py."""

import books_api


def main() -> None:
    books_api.init_db()

    author_id = books_api.add_author("Ursula K. Le Guin")
    book_id = books_api.add_book(
        title="A Wizard of Earthsea",
        author_id=author_id,
        year=1968,
        rating=5,
        read_it_or_not=True,
    )

    print("Author:", books_api.get_author(author_id))
    print("Book:", books_api.get_book(book_id))

    books_api.update_book(
        book_id,
        title="A Wizard of Earthsea",
        author_id=author_id,
        year=1968,
        rating=5,
        read_it_or_not=False,
    )

    print("All authors:", books_api.list_authors())
    print("All books:", books_api.list_books())


if __name__ == "__main__":
    main()