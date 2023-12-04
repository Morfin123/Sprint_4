import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Книга фантастики', 'Фантастика'],
            ['Книга ужасов', 'Ужасы'],
            ['Книга расследований', 'Детективы'],
            ['Книга комексов','Мультфильмы'],
            ['Книга комедий','Комедии']
        ]
    )
    def test_set_book_genre_add_book_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(name=book_name, genre=book_genre)
        assert collector.get_book_genre(book_name) != ''

    def test_set_book_genre_get_None_for_book_name_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book(name='Существущая книга')
        collector.set_book_genre(name='Несуществующая книга', genre='Детективы')
        assert collector.get_book_genre(name='Несуществующая книга') is None

    def test_add_new_book_similar_books_not_added(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга 1')
        collector.add_new_book(name='Книга 1')
        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre_book_doesnt_exist_got_genre_is_None(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга 1')
        assert collector.get_book_genre(name='Несуществующая книга') is None

    def test_add_new_book_not_add_long_name(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книжка с каким-то очень длинным названием')
        assert len(collector.get_books_genre()) == 0


    def test_get_books_with_specific_genre_get_not_None_for_book_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга фантастики')
        collector.set_book_genre(name='Книга фантастики', genre='Фантастика')
        assert collector.get_books_with_specific_genre(genre='Фантастика') is not None

    def test_get_books_with_specific_genre_not_return_book_name_with_unexistant_genre(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга фантастики')
        collector.set_book_genre(name='Книга фантастики', genre='Фантастика')
        assert collector.get_books_with_specific_genre(genre='Пустастика') == []

    def test_get_books_for_children_not_get_book_name_in_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга ужасов')
        collector.set_book_genre(name='Книга ужасов', genre='Ужасы')
        assert collector.get_books_for_children() != ['Книга ужасов']

    def test_get_books_for_children_get_book_name_then_book_not_in_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book(name='Детская книга')
        collector.set_book_genre(name='Детская книга', genre='Фантастика')
        assert collector.get_books_for_children() == ['Детская книга']

    def test_add_book_in_favorites_add_one_favorits(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга фаворит 1')
        collector.add_book_in_favorites(name='Книга фаворит 1')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_after_delete_book_from_favorites_get_list_of_favorites_is_clear(self):
        collector = BooksCollector()
        collector.add_new_book(name='Книга фаворит 1')
        collector.add_book_in_favorites(name='Книга фаворит 1')
        collector.delete_book_from_favorites(name='Книга фаворит 1')
        assert collector.get_list_of_favorites_books() == []
