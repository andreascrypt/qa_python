import pytest

from main import BooksCollector

@pytest.fixture(scope="function")
#book_dealer fixture

def book_dealer():
    return BooksCollector()