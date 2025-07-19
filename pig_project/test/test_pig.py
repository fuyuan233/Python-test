import sys

sys.path.append("../src")
import pig
import unittest


class TestPig(unittest.TestCase):
    def test_init(self):
        pig1 = pig.Pig("123456", name="小猪佩奇", age=1)
        self.assertEqual(pig1.ear_tag, "123456")
        self.assertEqual(pig1.name, "小猪佩奇")
        self.assertEqual(pig1.age, 1)
        self.assertEqual(pig1.treat, {})

    def test_treating(self):
        pig1 = pig.Pig("123456", name="小猪佩奇", age=1)
        pig1.treating("2021-01-01", "青霉素")
        self.assertEqual(pig1.treat, {"2021-01-01": "青霉素"})
