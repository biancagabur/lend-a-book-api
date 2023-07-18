import unittest

from models.book import Book


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.book = Book(id=1,
                         title="unit_test",
                         author="Bianca",
                         publication_date="18/07/2023",
                         isbn="11111")

    def test_to_dict(self):
        self.assertIsInstance(self.book.to_dict(), dict)

    def test_contains_id(self):
        self.assertIsNotNone(self.book.id)


if __name__ == '__main__':
    unittest.main()
