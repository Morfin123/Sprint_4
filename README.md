# qa_python

test_set_book_genre_add_book_genre # Проверка добавления жанра всем книгам

test_set_book_genre_get_None_for_book_name_not_in_books_genre # Жанр не добавляется для несуществующей книги

test_add_new_book_similar_books_not_added # Книги с одинаковым названием не добавляются

test_get_book_genre_book_doesnt_exist_got_genre_is_None # Возвращается значение None по запросу жанра несуществущей книги

test_add_new_book_not_add_long_name # Не добавляются книги с названием длинее 40 символов

test_get_books_with_specific_genre_return_not_None # Возвращаются данные по запросу конкретного жанра добавленной книги

test_get_books_with_specific_genre_not_return_book_name_with_unexistant_genre # Не возвращаются книги с несуществующим жанром

test_get_books_for_children_not_get_book_name_in_genre_age_rating # В книгах для детей нет книг для взролых

test_add_book_in_favorites_add_one_favorits # Добавляется одна книги в список избранных книг

test_delete_book_from_favorites_after_delete_book_from_favorites_get_list_of_favorites_is_clear # Книга удаляется из списка избранных книг