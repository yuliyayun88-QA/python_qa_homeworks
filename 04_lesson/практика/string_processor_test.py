# import pytest
# from string_processor import StringProcessor


# @pytest.mark.parametrize('input_text, expected_text', [
#     ('Hello.', 'Hello.'),
#     ('Мышь', 'Мышь.'),
#     ('  ', '  .'),
#     ('---', '---.'),
#     (',.', ',.')])
# def text_verific(input_text, expected_text):
#     res = StringProcessor.process(input_text)
#     assert res == expected_text

# Нужно задать значение по умолчанию для параметра expected_text в кортеже —
# чтобы оно автоматически бралось из выходного значения функции класса
# StringProcessor, а не прописывалось вручную.

# Вариант 1. Использование функции-обёртки
# Создаём вспомогательную функцию, которая автоматически получает значение от
# StringProcessor:

# python
# class StringProcessor:
#     @staticmethod
#     def process(text):
#         return text.upper()  # пример обработки

# def create_test_case(input_text, expected_text=None):
#     if expected_text is None:
#         expected_text = StringProcessor.process(input_text)
#     return (input_text, expected_text)

# # Использование
# test_cases = [
#     create_test_case("hello"),
#     create_test_case("world"),
#     create_test_case("custom", "CUSTOM")  # можно переопределить
# ]
# Вариант 2. Фабрика кортежей с методом класса
# Добавляем в класс метод, генерирующий кортежи с предустановленными
#  значениями:

# python
# class StringProcessor:
#     @staticmethod
#     def process(text):
#         return text.upper()

#     @classmethod
#     def create_test_case(cls, input_text):
#         expected = cls.process(input_text)
#         return (input_text, expected)

# # Использование
# test_cases = [
#     StringProcessor.create_test_case("hello"),
#     StringProcessor.create_test_case("world")
# ]
# # Результат: [('hello', 'HELLO'), ('world', 'WORLD')]
# Вариант 3. Использование dataclass
# Более структурированный подход с dataclass:

# python
# from dataclasses import dataclass

# @dataclass
# class TestCase:
#     input_text: str
#     expected_text: str = None

#     def __post_init__(self):
#         if self.expected_text is None:
#             self.expected_text = StringProcessor.process(self.input_text)

#     def as_tuple(self):
#         return (self.input_text, self.expected_text)

# # Использование
# test_cases = [
#     TestCase("hello").as_tuple(),
#     TestCase("world").as_tuple()
# ]
# Вариант 4. Декоратор для автоматической генерации
# Создаём декоратор, который дополняет кортежи ожидаемыми значениями:

# python
# def auto_expected(test_cases):
#     result = []
#     for case in test_cases:
#         if len(case) == 1:
#             input_text = case[0]
#             expected = StringProcessor.process(input_text)
#             result.append((input_text, expected))
#         else:
#             result.append(case)
#     return result

# # Использование
# raw_cases = [("hello",), ("world",), ("custom", "CUSTOM")]
# test_cases = auto_expected(raw_cases)
