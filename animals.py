#animals.py
#2014-09-05 22:18 -

import unittest
import time


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

    def test_a_new_bear_that_slept_can_play(self):
        bear = Omnivore()
        bear.go_to_sleep()
        expected = True
        actual = bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_can_play_but_not_play_again(self):
        bear = Omnivore()
        bear.go_to_sleep()
        actual = bear.play()
        expected = False
        actual = bear.play()
        self.assertEqual(expected, actual)

    def test_a_new_bear_cannot_play(self):
        bear = Omnivore()        
        expected = False
        actual = bear.play()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_go_to_sleep(self):
        bear = Omnivore()
        bear.go_to_sleep()
        expected = False
        actual = bear.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_bear_cannot_eat(self):
        bear = Omnivore()
        bear.go_to_sleep()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = bear.feed(food)
        self.assertEqual(expected, actual)

    def test_create_bear_and_sleep(self):
        bear = Omnivore()
        expected = True
        actual = bear.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_steak(self):
        bear = Omnivore()
        steak = Meat()
        expected = True
        actual = bear.feed(steak)
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_carrot(self):
        bear = Omnivore()
        carrot = Vegetable()
        expected = True
        actual = bear.feed(carrot)
        self.assertEqual(expected, actual)

    def test_create_Omnivore(self):
        bear = Omnivore()
        expected = True
        actual = isinstance(bear, Omnivore)
        self.assertEqual(expected, actual)


#########

    def test_a_new_goat_that_slept_can_play(self):
        goat = Vegetarian()
        goat.go_to_sleep()
        expected = True
        actual = goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_that_slept_can_play_but_not_play_again(self):
        goat = Vegetarian()
        goat.go_to_sleep()
        actual = goat.play()
        expected = False
        actual = goat.play()
        self.assertEqual(expected, actual)

    def test_a_new_goat_cannot_play(self):
        goat = Vegetarian()        
        expected = False
        actual = goat.play()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_go_to_sleep(self):
        goat = Vegetarian()
        goat.go_to_sleep()
        expected = False
        actual = goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_eat(self):
        goat = Vegetarian()
        goat.go_to_sleep()
        food = Vegetable()
        expected = 'I am sleeping. Grr.'
        actual = goat.feed(food)
        self.assertEqual(expected, actual)

    def test_create_goat_and_sleep(self):
        goat = Vegetarian()
        expected = True
        actual = goat.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_vegies(self):
        goat = Vegetarian()
        carrot = Vegetable()
        expected = True
        actual = goat.feed(carrot)
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_steak(self):
        goat = Vegetarian()
        steak = Meat()
        expected = False
        actual = goat.feed(steak)
        self.assertEqual(expected, actual)

    def test_create_Vegetarian(self):
        goat = Vegetarian()
        expected = True
        actual = isinstance(goat, Vegetarian)
        self.assertEqual(expected, actual)

####

    def test_a_new_lion_that_slept_can_play(self):
        lion = Carnivore()
        lion.go_to_sleep()
        expected = True
        actual = lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_that_slept_can_play_but_not_play_again(self):
        lion = Carnivore()
        lion.go_to_sleep()
        actual = lion.play()
        expected = False
        actual = lion.play()
        self.assertEqual(expected, actual)

    def test_a_new_lion_cannot_play(self):
        lion = Carnivore()        
        expected = False
        actual = lion.play()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_go_to_sleep(self):
        lion = Carnivore()
        lion.go_to_sleep()
        expected = False
        actual = lion.go_to_sleep()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_eat(self):
        lion = Carnivore()
        lion.go_to_sleep()
        food = Meat()
        expected = 'I am sleeping. Grr.'
        actual = lion.feed(food)
        self.assertEqual(expected, actual)

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
        carrot = Vegetable()
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

