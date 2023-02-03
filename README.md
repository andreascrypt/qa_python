# qa_python

Пояснение работы тестов в файле tests.py

1.test_init_favorites_empty_true
    Проверяет что список избранного пуст

2.test_init_book_rating_empty_true
    Проверяет словарь рейтинг пуст

3.test_add_new_book_one_more_time
    Проверяет что нельзя добавить одну книгу дважды в словарь
    
4.test_set_one_book_with_a_rating_from_1_to_11
    Проверяет возможность добавления рейтинга в диапазоне 1-10
    
5.test_add_one_book_to_books_have_default_rating_true
    Проверяет что при добавлении книга имеет рейтинг "1"
    
6.test_get_books_rating_return_dict_with_book_with_preset_rating
    Можно получить словарь рейтинга
    
7.test_add_books_get_books_with_specific_rating
    Можно получить список книг с заданным рейтингом
    
8.test_add_book_in_favorites_book_not_in_books_rating_cant_be_added_true
    Проверяет что кника не добавляется в список "Избранное" если ее нет в списке книг

9.test_add_book_in_favorites_add_one_book_in_favorites
    Книга добавляется в список "Избранное"
    
10.test_delete_book_from_favorites_delete_book_true
    Книгу можно удалить из списка "Избранное"

11.test_get_list_of_favorites_books_return_list_with_book
    Можно получить список избранных книг
    
12.test_add_new_books_few_books_added
    В словарь books_rating можно добавить несколько разных книг
    
13.test_set_rating_not_added_book
    Нельзя выставить рейтинг книге не из коллекции
