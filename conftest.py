import pytest
from main import BooksCollector

@pytest.fixture(scope="function")
def books_collector():
    return BooksCollector()
