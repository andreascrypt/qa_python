class TestBooksCollector:

# 1.self.favorites = []
    def test_init_favorites_empty_true(self, book_dealer):
        assert len(book_dealer.favorites) == 0

# 2.self.books_rating = {}
    def test_init_book_rating_empty_true(self, book_dealer):
        assert len(book_dealer.books_rating) == 0

# 3.В словарь books_rating нельзя добавить одну книгу дважды
    def test_add_new_book_one_more_time(self, book_dealer):
        book_dealer.add_new_book('Манифест Коммунистической партии')
        book_dealer.add_new_book('Манифест Коммунистической партии')

        assert len(book_dealer.get_books_rating()) == 1

# 4.Для добавленной книги можно установить рейтинг в пределах от 1 до 10
    def test_set_one_book_with_a_rating_from_1_to_11(self, book_dealer):
        book_dealer.add_new_book('Капитал: критика политической экономии')
        book_dealer.set_book_rating('Капитал: критика политической экономии', 9)

        assert book_dealer.books_rating['Капитал: критика политической экономии'] == 9

# 5.При добавлении в словарь books_rating книга имеет рейтинг "1"
    def test_add_one_book_to_books_have_default_rating_true(self, book_dealer):
        book_dealer.add_new_book('Анти-Дюринг. Диалектика природы')

        assert book_dealer.books_rating['Анти-Дюринг. Диалектика природы'] == 1

# 6.Можно получить словарь рейтинга
    def test_get_books_rating_return_dict_with_book_with_preset_rating(self, book_dealer):
        book_dealer.add_new_book('Так говорил Заратустра')
        book_dealer.set_book_rating('Так говорил Заратустра', 2)

        assert type(book_dealer.books_rating) == dict
        assert book_dealer.books_rating['Так говорил Заратустра'] == 2

# 7.Можно получить список книг с заданным рейтингом
    def test_add_books_get_books_with_specific_rating(self, book_dealer):
        book_dealer.add_new_book('Чума')
        book_dealer.add_new_book('Посторонний')
        book_dealer.add_new_book('Два капитана')
        book_dealer.add_new_book('Сын полка')
        book_dealer.add_new_book('Незнайка на Луне')
        book_dealer.add_new_book('Тихий Дон')
        book_dealer.add_new_book('Песня о Буревестнике')

        book_dealer.set_book_rating('Чума', 8)
        book_dealer.set_book_rating('Посторонний', 8)
        book_dealer.set_book_rating('Два капитана', 9)
        book_dealer.set_book_rating('Сын полка', 9)
        book_dealer.set_book_rating('Незнайка на Луне', 9)
        book_dealer.set_book_rating('Тихий Дон', 6)
        book_dealer.set_book_rating('Песня о Буревестнике', 6)

        books_with_rating_eight = book_dealer.get_books_with_specific_rating(8)
        books_with_rating_nine = book_dealer.get_books_with_specific_rating(9)
        books_with_rating_six = book_dealer.get_books_with_specific_rating(6)

        assert len(book_dealer.get_books_with_specific_rating(8)) == 2
        assert ['Чума', 'Посторонний'] == books_with_rating_eight
        assert len(book_dealer.get_books_with_specific_rating(9)) == 3
        assert ['Два капитана', 'Сын полка', 'Незнайка на Луне'] == books_with_rating_nine
        assert len(book_dealer.get_books_with_specific_rating(6)) == 2
        assert ['Тихий Дон', 'Песня о Буревестнике']  == books_with_rating_six

# 8.Книга не добавляется в список "Избранное" если ее нет в списке книг
    def test_add_book_in_favorites_book_not_in_books_rating_cant_be_added_true(self, book_dealer):
        book_dealer.add_book_in_favorites('Сердце тьмы')

        assert 'Сердце тьмы' not in book_dealer.get_list_of_favorites_books()
        assert len(book_dealer.favorites) == 0

# 9.Книга добавляется в список "Избранное"
    def test_add_book_in_favorites_add_one_book_in_favorites(self, book_dealer):
        book_dealer.add_new_book('Бойня номер пять')
        book_dealer.add_book_in_favorites('Бойня номер пять')

        assert 'Бойня номер пять' in book_dealer.get_list_of_favorites_books()
        assert book_dealer.favorites == ['Бойня номер пять']

# 10.Книгу можно удалить из списка "Избранное"
    def test_delete_book_from_favorites_delete_book_true(self, book_dealer):
        book_dealer.add_new_book('Замок')
        book_dealer.add_book_in_favorites('Замок')

        assert 'Замок' in book_dealer.get_list_of_favorites_books()
        assert book_dealer.favorites == ['Замок']

        book_dealer.delete_book_from_favorites('Замок')

        assert 'Замок' not in book_dealer.get_list_of_favorites_books()
        assert len(book_dealer.favorites) == 0

# 11.Можно получить список избранных книг
    def test_get_list_of_favorites_books_return_list_with_book(self, book_dealer):
        book_dealer.add_new_book('Консервный ряд')
        book_dealer.add_book_in_favorites('Консервный ряд')

        assert type(book_dealer.favorites) == list
        assert 'Консервный ряд' in book_dealer.get_list_of_favorites_books()
        assert book_dealer.favorites == ['Консервный ряд']

# 12.В словарь books_rating можно добавить несколько книги с разным названием
    def test_add_new_books_few_books_added(self, book_dealer):
        book_dealer.add_new_book('Капитал: критика политической экономии'),
        book_dealer.add_new_book('Анти-Дюринг. Диалектика природы')

        assert len(book_dealer.get_books_rating()) == 2

# 13.нельзя выставить рейтинг книге не из коллекции
    def test_set_rating_not_added_book(self, book_dealer):
        book_dealer.set_book_rating('Настольная книга атеиста', 9)

        assert len(book_dealer.get_books_rating()) == 0