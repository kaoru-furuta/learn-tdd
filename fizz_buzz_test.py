from unittest import TestCase, main
from fizz_buzz import FizzBuzz


class FizzBuzzTestCase(TestCase):

    def test_int1_to_str1(self):
        # 前準備
        fizz_buzz = FizzBuzz()
        # 実行 and 検証
        self.assertEqual('1', fizz_buzz.convert(1))

    def test_int2_to_str2(self):
        # 前準備
        fizz_buzz = FizzBuzz()
        # 実行 and 検証
        self.assertEqual('2', fizz_buzz.convert(2))


if __name__ == '__main__':
    main()
