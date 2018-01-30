from unittest import TestCase, main
from fizz_buzz import FizzBuzz


class FizzBuzzTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # 前準備
        cls.fizz_buzz = FizzBuzz()

    def test_int1_to_str1(self):
        # 実行 and 検証
        self.assertEqual('1', self.fizz_buzz.convert(1))

    def test_int2_to_str2(self):
        # 実行 and 検証
        self.assertEqual('2', self.fizz_buzz.convert(2))

    def test_int3_to_Fizz(self):
        # 実行 and 検証
        self.assertEqual('Fizz', self.fizz_buzz.convert(3))


if __name__ == '__main__':
    main()
