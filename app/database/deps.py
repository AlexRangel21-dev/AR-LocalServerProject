from database.database import SessionLocal
from database.mysql_database import MySQLSessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_mysql_db():
    db = MySQLSessionLocal()
    try:
        yield db
    finally:
        db.close()