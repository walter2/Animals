#animals.py
#2014-09-05 22:18 -

import unittest
import time

#ToDo 2014-09-23
#1. refactor tests
#1.1 add class Animal()
#2. sleep duration calculation
#3. food diet type implementation
#4. self.is_hungry
#5. scale for sleep and food
#6. three different game types

#configs
SLEEP_TIME = 2


class Carnivore():
    def __init__(self):
        self.sleeping = False
        self.needs_sleep = True
    
    def feed(self, food):
        '''The animal takes only meet as food.
           If it is sleeping it cannot eat and
           will complain.'''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        else:
            return isinstance(food, Meat)

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

class Vegetarian():
    def __init__(self):
        self.sleeping = False
        self.needs_sleep = True
    
    def feed(self, food):
        '''The animal takes only meet as food.
           If it is sleeping it cannot eat and
           will complain.'''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        else:
            return isinstance(food, Vegetable)

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

class Omnivore():
    def __init__(self):
        self.sleeping = False
        self.needs_sleep = True
    
    def feed(self, food):
        '''The animal takes only meet as food.
           If it is sleeping it cannot eat and
           will complain.'''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        else:
            return isinstance(food, (Meat, Vegetable))

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

        
class Vegetable():
    pass

class Meat():
    pass


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
        actual = self.bear.feed(food)
        self.assertEqual(expected, actual)

    def test_create_bear_and_sleep(self):
        expected = True
        actual = self.bear.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_steak(self):
        steak = Meat()
        expected = True
        actual = self.bear.feed(steak)
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_carrot(self):
        carrot = Vegetable()
        expected = True
        actual = self.bear.feed(carrot)
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

##    def test_a_new_goat_cannot_play(self):
##        expected = False
##        actual = self.goat.play()
##        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_go_to_sleep(self):
        self.goat.go_to_sleep()
        expected = False
        actual = self.goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_eat(self):
        self.goat.go_to_sleep()
        food = Vegetable()
        expected = 'I am sleeping. Grr.'
        actual = self.goat.feed(food)
        self.assertEqual(expected, actual)

    def test_create_goat_and_sleep(self):
        expected = True
        actual = self.goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_vegies(self):
        carrot = Vegetable()
        expected = True
        actual = self.goat.feed(carrot)
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_steak(self):
        steak = Meat()
        expected = False
        actual = self.goat.feed(steak)
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

##    def test_a_new_lion_cannot_play(self):
##        expected = False
##        actual = self.lion.play()
##        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_go_to_sleep(self):
        self.lion.go_to_sleep()
        expected = False
        actual = self.lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_eat(self):
        self.lion.go_to_sleep()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = self.lion.feed(food)
        self.assertEqual(expected, actual)

    def test_create_lion_and_sleep(self):
        expected = True
        actual = self.lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_steak(self):
        steak = Meat()
        expected = True
        actual = self.lion.feed(steak)
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_carrot(self):
        carrot = Vegetable()
        expected = False
        actual = self.lion.feed(carrot)
        self.assertEqual(expected, actual)

    def test_create_Carnivore(self):
        expected = True
        actual = isinstance(self.lion, Carnivore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit = False)

