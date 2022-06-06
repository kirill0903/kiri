import sqlite3
from datetime import datetime

database = sqlite3.Connection(":memory:")

database.execute("""
    CREATE TABLE IF NOT EXISTS
        "articles" (
            "id"            INTEGER PRIMARY KEY AUTOINCREMENT,
            "title"         VARCHAR,
            "text"          VARCHAR,
            "created_at"    DATETIME
        ) 
""")


def get_articles(search: str) -> tuple[int, str, str, datetime]:
    return database.execute("""
        SELECT
            *
        FROM
            "articles"
        WHERE
            INSTR("title", :search) OR INSTR("text", :search)
    """, {"search": search}).fetchall()


def create_article(title: str, text: str) -> None:
    database.execute("""
        INSERT INTO
            "articles" (
                "title", "text", "created_at"
            )
        VALUES (
            ?, ?, ?
        )
    """, (title, text, datetime.now()))


def update_article(id: int, title: str, text: str) -> None:
    database.execute("""
        UPDATE 
            "articles"
        SET
            "title"=?, "text"=?
        WHERE
            "id" = ?
    """, (title, text, id))


def delete_article(id: int) -> None:
    database.execute("""
        DELETE FROM
            "articles"
        WHERE
            "id" = ?
    """, (id,))