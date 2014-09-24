#animals.py

import time
import unittest
from datetime import datetime

#ToDo 2014-09-23
#1. DONE refactor tests
#1.1 DONE add class Animal()
#2. DONE sleep duration calculation
#3. DONE food diet type implementation
#4. DONE self.is_hungry
#5. scale for sleep and food
#6. three different game types
#7. separate tests out


#configs
SLEEP_TIME_SECONDS = 1

class Animal():
    '''Base class for different animal types (Omnivore,
       Vegetarian and Carnivore.
    '''
    def __init__(self):
        self.sleeping = False
        self.needs_sleep = True
        self.sleep_start_time = None
        self.is_hungry = True
    
    def eat(self, food):
        '''The animal only can eat food suitable food.
           If it is sleeping it cannot eat and complains.
        '''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        else:
            return self.can_eat(food)

    def can_eat(self, food):
        raise NotImplementedError

    def start_sleeping(self):
        '''Puts the animal to sleep when it requies sleep.'''
        if not self.sleeping:
            self.sleep_start_time = datetime.now()
            self.sleeping = True
            self.needs_sleep = False
            return True
        else:
            return False

    def stop_sleeping(self):
        '''Sets self.sleeping to Flase when the animal slept
           enough and retruns True. Otherwise it returns False.
        '''
        if int(datetime.now().second - self.sleep_start_time.second) > SLEEP_TIME_SECONDS:
            self.sleeping = False
            return True
        else:
            return False

    def play(self):
        if not self.needs_sleep:
            self.needs_sleep = True
            return True
        else:
            return False


class Carnivore(Animal):

    def can_eat(self, food):
        if food.is_meat:
            self.is_hungry = False
            return True
        else:
            return False


class Vegetarian(Animal):

    def can_eat(self, food):
        if food.is_vegetable:
            self.is_hungry = False
            return True
        else:
            return False


class Omnivore(Animal):

    def can_eat(self, food):
        self.is_hungry = False
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

    def test_a_new_bear_is_totally_hungry(self):
        expected = 0
        actual = self.bear.hunger_scale
        self.assertEqual(expected, actual)

    def test_a_new_bear_is_hungry(self):
        expected = True
        actual = self.bear.is_hungry
        self.assertEqual(expected, actual)

    def test_a_new_bear_can_sleep_and_sleeps(self):
        self.bear.start_sleeping()
        expected = True
        actual = self.bear.sleeping
        self.assertEqual(expected, actual)

    def test_a_new_bear_can_sleep_and_stops_sleeping_after_two_seconds(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        expected = False
        actual = self.bear.sleeping
        self.assertEqual(expected, actual)

    def test_a_new_bear_can_sleep_and_cannot_stops_sleeping_after_one_second(self):
        self.bear.start_sleeping()
        time.sleep(1)
        self.bear.stop_sleeping()
        expected = True
        actual = self.bear.sleeping
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_can_play(self):
        self.bear.start_sleeping()
        expected = True
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_can_play_but_not_play_again(self):
        self.bear.start_sleeping()
        actual = self.bear.play()
        expected = False
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_cannot_play(self):
        expected = False
        actual = self.bear.play()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_go_to_sleep(self):
        self.bear.start_sleeping()
        expected = False
        actual = self.bear.start_sleeping()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_eat(self):
        self.bear.start_sleeping()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = self.bear.eat(food)
        self.assertEqual(expected, actual)

    def test_create_bear_and_sleep(self):
        expected = True
        actual = self.bear.start_sleeping()
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_steak(self):
        steak = Meat()
        expected = True
        actual = self.bear.eat(steak)
        self.assertEqual(expected, actual)

    def test_new_fed_bear_is_not_hungry_anymore(self):
        steak = Meat()
        actual = self.bear.eat(steak)
        expected = False
        actual = self.bear.is_hungry
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
        self.goat.start_sleeping()
        expected = True
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_that_slept_can_play_but_not_play_again(self):
        self.goat.start_sleeping()
        actual = self.goat.play()
        expected = False
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_cannot_play(self):
        expected = False
        actual = self.goat.play()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_go_to_sleep(self):
        self.goat.start_sleeping()
        expected = False
        actual = self.goat.start_sleeping()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_eat(self):
        self.goat.start_sleeping()
        food = Vegetable()
        expected = 'I am sleeping. Grr.'
        actual = self.goat.eat(food)
        self.assertEqual(expected, actual)

    def test_create_goat_and_sleep(self):
        expected = True
        actual = self.goat.start_sleeping()
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
        self.lion.start_sleeping()
        expected = True
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_that_slept_can_play_but_not_play_again(self):
        self.lion.start_sleeping()
        actual = self.lion.play()
        expected = False
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_cannot_play(self):
        expected = False
        actual = self.lion.play()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_go_to_sleep(self):
        self.lion.start_sleeping()
        expected = False
        actual = self.lion.start_sleeping()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_eat(self):
        self.lion.start_sleeping()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = self.lion.eat(food)
        self.assertEqual(expected, actual)

    def test_create_lion_and_sleep(self):
        expected = True
        actual = self.lion.start_sleeping()
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

    def test_create_lion_and_feed_carrot(self):
        carrot = Vegetable()
        self.lion.eat(carrot)
        expected = True
        actual = self.lion.is_hungry
        self.assertEqual(expected, actual)

    def test_create_Carnivore(self):
        expected = True
        actual = isinstance(self.lion, Carnivore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit = False)

