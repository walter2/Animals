#animals.py
#2014-09-05 22:18 -

import unittest

class Carnivore():
    def __init__(self):
        self.sleeping = False
    
    def feed(self, food):
        return isinstance(food, Meat)

    def go_to_sleep(self):
        if not self.sleeping:
            self.sleeping = True
            return True
        else:
            return False

class Vegitable():
    pass

class Meat():
    pass


class Test(unittest.TestCase):

    def test_sleeping_lion_cannot_go_to_sleep(self):
        lion = Carnivore()
        lion.go_to_sleep()
        expected = False
        actual = lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_play(self):
        lion = Carnivore()
        lion.go_to_sleep()
        expected = False
        actual = lion.eat()
        self.assertEqual(expected, actual)

##    def test_sleeping_lion_cannot_go_to_sleep(self):
##        lion = Carnivore()
##        lion.go_to_sleep()
##        expected = False
##        actual = lion.go_to_sleep()
##        self.assertEqual(expected, actual)

    def test_create_lion_and_sleep(self):
        lion = Carnivore()
        expected = True
        actual = lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_steak(self):
        lion = Carnivore()
        steak = Meat()
        expected = True
        actual = lion.feed(steak)
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_carrot(self):
        lion = Carnivore()
        carrot = Vegitable()
        expected = False
        actual = lion.feed(carrot)
        self.assertEqual(expected, actual)

    def test_create_Carnivore(self):
        lion = Carnivore()
        expected = True
        actual = isinstance(lion, Carnivore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit = False)

