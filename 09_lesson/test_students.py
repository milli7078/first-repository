import pytest
from db import Session, engine, Base
from models import Student

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_add_student():
    session = Session()
    student = Student(name="Alice", email="alice@example.com")
    session.add(student)
    session.commit()

    saved = session.query(Student).filter_by(email="alice@example.com").first()
    assert saved.name == "Alice"

    session.delete(saved)
    session.commit()
    session.close()

def test_update_student():
    session = Session()
    student = Student(name="Bob", email="bob@example.com")
    session.add(student)
    session.commit()

    student.name = "Bobby"
    session.commit()

    updated = session.query(Student).filter_by(email="bob@example.com").first()
    assert updated.name == "Bobby"

    session.delete(updated)
    session.commit()
    session.close()

def test_delete_student():
    session = Session()
    student = Student(name="Charlie", email="charlie@example.com")
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(Student).filter_by(email="charlie@example.com").first()
    assert deleted is None

    session.close()
