from typing import Iterable

from sqlalchemy.orm import Session

from plutous.database import engine


def get_session() -> Iterable[Session]:
    conn = engine.connect()
    session = Session(conn)
    try:
        yield session
    finally:
        session.close()
        conn.close()