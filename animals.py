#animals.py

import unittest
from datetime import datetime

#ToDo 2014-09-23
#1. DONE refactor tests
#1.1 DONE add class Animal()
#2. sleep duration calculation
#3. DONE food diet type implementation
#4. self.is_hungry
#5. scale for sleep and food
#6. three different game types
#7. separate tests out


#configs
SLEEP_TIME = 2

class Animal():
    '''Base class for different animal types (Omnivore,
       Vegetarian and Carnivore.'''
    def __init__(self):
        self.sleeping = False
        self.needs_sleep = True
    
    def eat(self, food):
        '''The animal takes only meet as food.
           If it is sleeping it cannot eat and
           will complain.'''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        else:
            return self.can_eat(food)

    def can_eat(self, food):
        raise NotImplementedError

    def go_to_sleep(self):
        if not self.sleeping:
            self.sleeping = True
            self.needs_sleep = False
            #self.sleep_release()
            #time.sleep(SLEEP_TIME)
            #self.sleeping = False
            return True
        else:
            return False

    def sleep_release(self):
        '''Does currently not work.
           Should reset self.sleep in the background when
           go_to_sleep was called.'''
        time.sleep(SLEEP_TIME)
        self.sleeping = False

    def play(self):
        if not self.needs_sleep:
            self.needs_sleep = True
            return True
        else:
            return False


class Carnivore(Animal):

    def can_eat(self, food):
        return food.is_meat


class Vegetarian(Animal):

    def can_eat(self, food):
        return food.is_vegetable


class Omnivore(Animal):

    def can_eat(self, food):
        return food.is_vegetable or food.is_meat
    
        
class Vegetable():

    def __init__(self):
        self.is_vegetable = True
        self.is_meat = False


class Meat():

    def __init__(self):
        self.is_vegetable = False
        self.is_meat = True


class Test(unittest.TestCase):

    def setUp(self):
        self.bear = Omnivore()
        self.lion = Carnivore()
        self.goat = Vegetarian()

    def test_a_new_bear_that_slept_can_play(self):
        self.bear.go_to_sleep()
        expected = True
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_can_play_but_not_play_again(self):
        self.bear.go_to_sleep()
        actual = self.bear.play()
        expected = False
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_cannot_play(self):
        expected = False
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_go_to_sleep(self):
        self.bear.go_to_sleep()
        expected = False
        actual = self.bear.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_eat(self):
        self.bear.go_to_sleep()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = self.bear.eat(food)
        self.assertEqual(expected, actual)

    def test_create_bear_and_sleep(self):
        expected = True
        actual = self.bear.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_steak(self):
        steak = Meat()
        expected = True
        actual = self.bear.eat(steak)
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_carrot(self):
        carrot = Vegetable()
        expected = True
        actual = self.bear.eat(carrot)
        self.assertEqual(expected, actual)

    def test_create_Omnivore(self):
        expected = True
        actual = isinstance(self.bear, Omnivore)
        self.assertEqual(expected, actual)


#########

    def test_a_new_goat_that_slept_can_play(self):
        self.goat.go_to_sleep()
        expected = True
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_that_slept_can_play_but_not_play_again(self):
        self.goat.go_to_sleep()
        actual = self.goat.play()
        expected = False
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_cannot_play(self):
        expected = False
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_go_to_sleep(self):
        self.goat.go_to_sleep()
        expected = False
        actual = self.goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_eat(self):
        self.goat.go_to_sleep()
        food = Vegetable()
        expected = 'I am sleeping. Grr.'
        actual = self.goat.eat(food)
        self.assertEqual(expected, actual)

    def test_create_goat_and_sleep(self):
        expected = True
        actual = self.goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_vegies(self):
        carrot = Vegetable()
        expected = True
        actual = self.goat.eat(carrot)
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_steak(self):
        steak = Meat()
        expected = False
        actual = self.goat.eat(steak)
        self.assertEqual(expected, actual)

    def test_create_Vegetarian(self):
        expected = True
        actual = isinstance(self.goat, Vegetarian)
        self.assertEqual(expected, actual)

####

    def test_a_new_lion_that_slept_can_play(self):
        self.lion.go_to_sleep()
        expected = True
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_that_slept_can_play_but_not_play_again(self):
        self.lion.go_to_sleep()
        actual = self.lion.play()
        expected = False
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_cannot_play(self):
        expected = False
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_go_to_sleep(self):
        self.lion.go_to_sleep()
        expected = False
        actual = self.lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_eat(self):
        self.lion.go_to_sleep()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = self.lion.eat(food)
        self.assertEqual(expected, actual)

    def test_create_lion_and_sleep(self):
        expected = True
        actual = self.lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_steak(self):
        steak = Meat()
        expected = True
        actual = self.lion.eat(steak)
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_carrot(self):
        carrot = Vegetable()
        expected = False
        actual = self.lion.eat(carrot)
        self.assertEqual(expected, actual)

    def test_create_Carnivore(self):
        expected = True
        actual = isinstance(self.lion, Carnivore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit = False)

