import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_success(self, books_collector):
        books_collector.add_new_book('Book1')
        assert 'Book1' in books_collector.books_genre , "Книга не добавлена в books_genre"

    def test_add_new_book_duplicate(self, books_collector):
        # Проверяем, что повторное добавление книги не создает дубликат
        books_collector.add_new_book('Book1')
        books_collector.add_new_book('Book1')
        assert list(books_collector.books_genre.keys()).count('Book1') == 1

    @pytest.mark.parametrize('name', ['Очень длинное название книги, больше 40 символов', ''])
    def test_add_new_book_invalid_name(self, books_collector, name):
        # Проверяем, что книги с некорректными названиями (слишком длинными или пустыми) не добавляются
        books_collector.add_new_book(name)
        assert name not in books_collector.books_genre

    def test_set_book_genre_success(self, books_collector):
        # Проверяем, что жанр книги устанавливается успешно
        books_collector.add_new_book('Book1')
        books_collector.set_book_genre('Book1', 'Фантастика')
        assert books_collector.get_book_genre('Book1') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, books_collector):
        # Проверяем, что установка некорректного жанра не меняет жанр книги
        books_collector.add_new_book('Book1')
        books_collector.set_book_genre('Book1', 'Неизвестный жанр')
        assert books_collector.get_book_genre('Book1') == ''

    def test_get_books_with_specific_genre(self, books_collector):
        # Проверяем получение списка книг определенного жанра
        books_collector.add_new_book('Book1')
        books_collector.set_book_genre('Book1', 'Фантастика')
        books_collector.add_new_book('Book2')
        books_collector.set_book_genre('Book2', 'Ужасы')
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Book1']

    def test_get_books_for_children(self, books_collector):
        # Проверяем получение списка книг для детей (без возрастного рейтинга)
        books_collector.add_new_book('Book1')
        books_collector.set_book_genre('Book1', 'Фантастика')
        books_collector.add_new_book('Book2')
        books_collector.set_book_genre('Book2', 'Ужасы')
        assert books_collector.get_books_for_children() == ['Book1']

    def test_add_book_in_favorites_success(self, books_collector):
        # Проверяем добавление книги в избранное
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        assert 'Book1' in books_collector.favorites

    def test_add_book_in_favorites_not_in_books_genre(self, books_collector):
        # Проверяем, что в избранное нельзя добавить книгу, которой нет в books_genre
        books_collector.add_book_in_favorites('Book1')
        assert 'Book1' not in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):
        # Проверяем удаление книги из избранного
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        books_collector.delete_book_from_favorites('Book1')
        assert 'Book1' not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        assert books_collector.get_list_of_favorites_books() == ['Book1']