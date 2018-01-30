from unittest import TestCase, main
from fizz_buzz import FizzBuzz


class FizzBuzzTestCase(TestCase):

    def test_int1_to_str1(self):
        # 前準備
        fizz_buzz = FizzBuzz()

        # 実行
        actual = fizz_buzz.convert(1)

        # 検証
        self.assertEqual('1', actual)


if __name__ == '__main__':
    main()