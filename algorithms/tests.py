import unittest

from prime_numbers import prime_numbers
from roman_to_int import roman_numerals_to_int
from text_statistics import text_statistics


class TestPrimeNumbers(unittest.TestCase):
    
    def test_incorrect_values_1(self):
        self.assertEqual(prime_numbers(1, 'строка'), [])
        
    def test_incorrect_values_2(self):
        self.assertEqual(prime_numbers(1, 0), [])

    def test_correct_values_1(self):
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])
        
    def test_correct_values_2(self):
        self.assertEqual(prime_numbers(2.6, 34.8), [3, 5, 7, 11, 13, 17, 19, 23, 29, 31])


class TestRomanNumbers(unittest.TestCase):
    
    def test_incorrect_number_1(self):
        self.assertEqual(roman_numerals_to_int('CCCMMVIIVV'), None)
        
    def test_incorrect_number_2(self):
        self.assertEqual(roman_numerals_to_int('MMMMDMXCIX'), None)

    def test_correct_number_1(self):
        self.assertEqual(roman_numerals_to_int('MMDCCLXXIII'), 2773)
        
    def test_correct_number_2(self):
        self.assertEqual(roman_numerals_to_int('MMMCDXXXIV'), 3434)


class TestTextStat(unittest.TestCase):

    def test_incorrect_file_1(self):
        self.assertEqual(text_statistics(10),
            {'error': 'Аргументом должна быть строка - путь к файлу.'})

    def test_incorrect_file_2(self):
        self.assertEqual(text_statistics('../file.txt'),
            {'error': 'Файла с таким именем не существует.'})

    def test_correct_file(self):
        answer = {'П': (2, 2),
                'р': (50, 42),
                'о': (125, 93),
                'с': (55, 49),
                'т': (72, 60),
                'ы': (21, 20),
                'е': (70, 58),
                'ч': (13, 13),
                'и': (89, 79),
                'л': (46, 44),
                'а': (74, 53),
                'в': (44, 40),
                'з': (25, 25),
                'д': (35, 33),
                'н': (65, 53),
                'м': (31, 30),
                'п': (31, 31),
                'Н': (2, 2),
                'б': (16, 15),
                'х': (10, 9),
                'm': (7, 7),
                'b': (2, 2),
                'ь': (18, 17),
                'ф': (7, 7),
                'у': (23, 22),
                'к': (36, 32),
                'ц': (15, 15),
                'ю': (10, 10),
                'p': (3, 3),
                'r': (6, 6),
                'i': (6, 6),
                'e': (7, 7),
                'n': (11, 10),
                'u': (4, 4),
                's': (4, 4),
                'l': (4, 4),
                'o': (6, 6),
                'w': (2, 2),
                'h': (4, 2),
                'g': (2, 2),
                'г': (6, 6),
                'ж': (6, 6),
                'я': (21, 18),
                'й': (13, 13),
                'э': (3, 3),
                'Ф': (2, 2),
                'щ': (7, 7),
                'a': (4, 4),
                't': (8, 5),
                'Р': (1, 1),
                'ш': (4, 4),
                'N': (1, 1),
                'Д': (2, 2),
                'В': (1, 1),
                'y': (1, 1),
                'Г': (1, 1),
                'Э': (1, 1),
                'word_amount': 176,
                'paragraph_amount': 3,
                'bilingual_word_amount': 4}

        self.assertEqual(text_statistics('../test_data/statistics.txt'), answer)


if __name__ == '__main__':
    unittest.main()
