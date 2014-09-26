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
#5. DONE scale for sleep and food
# DONE CONTINUE: from email, remove double referece to sleep (needs_sleep)
#          and hunger (is_hungry), fullness_scale, etc
#          then do more on animal_short_before_play_implentation.txt
#6. DONE three basic game types, only reduce awake_energy
#6.1 DONE awake and fullness constants
#7. separate tests out


#configs
SLEEP_TIME_SECONDS = 1
MAX_AWAKENESS = 10
MAX_FULLNESS = 10

class Animal():
    '''Base class for different animal types (Omnivore,
       Vegetarian and Carnivore.
    '''
    def __init__(self):
        '''Default attributes of the animal:
           sleeping ... default: False; if the animal is currently sleeping or not
           sleep_start_time ... default: None; time (datetime) when animal
                                starts sleeping           
           fullness_scale ... default: 0; 0 means completely hungry,
                            10 means animal cannot eat more
           awake_scale ... default: 0; 0 means the animal is completely tired,
                           10 means the animal is fully awake
        '''
        self.sleeping = False
        self.sleep_start_time = None        
        self.awake_scale = 0
        self.fullness_scale = 0
    
    def eat(self, food):
        '''The animal only can eat food suitable food.
           It uses the child class can_eat() function to
           determine if it can eat a certain type of food.
           If the animal is full it cannot eat.
           If it is sleeping it cannot eat and complains.
        '''
        if self.sleeping:
            return 'I am sleeping. Grr.'
        elif self.fullness_scale == MAX_FULLNESS:
            return 'I am so full ... I cannot eat anymore.'
        else:
            if self.can_eat(food):
                self.fullness_scale = MAX_FULLNESS
                return True
            else:
                return False

    def can_eat(self, food):
        raise NotImplementedError

    def start_sleeping(self):
        '''Puts the animal to sleep when it requies sleep.'''
        if not self.sleeping:
            self.sleep_start_time = datetime.now()
            self.sleeping = True
            return True
        else:
            return False

    def stop_sleeping(self):
        '''Sets self.sleeping to Flase and self.awake_scale to 10
           when the animal slept enough and retruns True.
           Otherwise it returns False.
        '''
        if int(datetime.now().second - self.sleep_start_time.second) > SLEEP_TIME_SECONDS:
            self.sleeping = False
            self.awake_scale = MAX_AWAKENESS
            return True
        else:
            return False

    def play(self, game):
        '''play() takes a game as argument and
           reduces the awake_scale minus two points.
        '''
        if (self.awake_scale - game.awake_energy_used) >= 2:
            self.awake_scale -= game.awake_energy_used
            self.needs_sleep = True
            return True
        else:
            return False


class Carnivore(Animal):
    '''Carnivore class that only eats meat.'''
    def can_eat(self, food):
        if food.is_meat:
            return food.is_meat
        else:
            return False


class Vegetarian(Animal):
    '''Vegetarian class that only eats vegetables.'''
    def can_eat(self, food):
        if food.is_vegetable:            
            return food.is_vegetable
        else:
            return False


class Omnivore(Animal):
    '''Omnivore class that eats meat and vegetables.'''
    def can_eat(self, food):
        self.fullness_scale = 10
        return food.is_vegetable or food.is_meat
    

class Food():
    '''Base class for food types.'''
    pass


class Vegetable(Food):
    '''Vegetable food.'''
    def __init__(self):
        self.is_vegetable = True
        self.is_meat = False


class Meat(Food):
    '''Meat food.'''
    def __init__(self):
        self.is_vegetable = False
        self.is_meat = True


class Game():
    '''Game is the base class for all games the animals
       can play.
    '''
    def __str__(self):
        return self.name


class HideAndSeek(Game):
    '''Hide and seek game. It deducts two points of the awake_scale.'''
    def __init__(self):
        self.name = 'hide and seek'
        self.awake_energy_used = 2


class CatchFrisbee(Game):
    '''Catch a frisbee game. It deducts one points of the awake_scale.'''
    def __init__(self):
        self.name = 'catch frisbee'
        self.awake_energy_used = 1


class JumpOverHedges(Game):
    '''Jump over hedges game. It deducts three points of the awake_scale.'''
    def __init__(self):
        self.name = 'jump over hedges'
        self.awake_energy_used = 3


class Test(unittest.TestCase):
    '''Unittests for all classes'''

    def setUp(self):
        self.bear = Omnivore()
        self.lion = Carnivore()
        self.goat = Vegetarian()
        self.steak = Meat()
        self.carrot = Vegetable()
        self.hide_and_seek = HideAndSeek()
        self.catch_frisbee = CatchFrisbee()
        self.jump_over_hedges = JumpOverHedges()

    def test_new_bear_that_slept_can_play_one_hide_and_seek_games(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        expected = True
        actual = self.bear.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_new_bear_that_slept_cannot_play_five_hide_and_seek_games(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        self.bear.play(self.hide_and_seek)
        self.bear.play(self.hide_and_seek)
        self.bear.play(self.hide_and_seek)
        self.bear.play(self.hide_and_seek)
        expected = False
        actual = self.bear.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_new_bear_that_slept_can_play_eight_times_catch_frisbee(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        expected = True
        actual = self.bear.play(self.catch_frisbee)
        self.assertEqual(expected, actual)

    def test_new_bear_that_slept_cannot_play_nine_times_catch_frisbee(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        self.bear.play(self.catch_frisbee)
        expected = False
        actual = self.bear.play(self.catch_frisbee)
        self.assertEqual(expected, actual)

    def test_new_bear_that_slept_cannot_play_two_hide_and_seek__and__two_jump_over_hedges(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        self.bear.play(self.hide_and_seek)
        self.bear.play(self.hide_and_seek)
        self.bear.play(self.jump_over_hedges)
        expected = False
        actual = self.bear.play(self.jump_over_hedges)
        self.assertEqual(expected, actual)

    def test_hide_and_seek_is_a_game(self):
        expected = True
        actual = isinstance(self.hide_and_seek, Game)
        self.assertEqual(expected, actual)

    def test_catch_frisbee_is_a_game(self):
        expected = True
        actual = isinstance(self.catch_frisbee, Game)
        self.assertEqual(expected, actual)
        
    def test_jump_over_hedges_is_a_game(self):
        expected = True
        actual = isinstance(self.jump_over_hedges, Game)
        self.assertEqual(expected, actual)
        
    def test_new_bear_that_eat_cannot_eat_again(self):
        self.bear.eat(self.steak)
        expected = 'I am so full ... I cannot eat anymore.'
        actual = self.bear.eat(self.steak)
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_is_totally_awake(self):
        self.bear.start_sleeping()
        time.sleep(2)
        self.bear.stop_sleeping()
        expected = 10
        actual = self.bear.awake_scale
        self.assertEqual(expected, actual)

    def test_a_new_bear_is_totally_tried(self):
        expected = 0
        actual = self.bear.awake_scale
        self.assertEqual(expected, actual)

    def test_new_bear_eats_steak_and_is_full(self):
        self.bear.eat(self.steak)
        expected = 10
        actual = self.bear.fullness_scale
        self.assertEqual(expected, actual)

    def test_a_new_bear_is_hungry(self):
        expected = 0
        actual = self.bear.fullness_scale
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
        time.sleep(2)
        self.bear.stop_sleeping()
        expected = True
        actual = self.bear.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_a_new_bear_that_slept_can_play_but_not_play_again(self):
        self.bear.start_sleeping()
        actual = self.bear.play(self.hide_and_seek)
        expected = False
        actual = self.bear.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_a_new_bear_cannot_play(self):
        expected = False
        actual = self.bear.play(self.hide_and_seek)
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
        actual = self.bear.eat(self.steak)
        expected = 10
        actual = self.bear.fullness_scale
        self.assertEqual(expected, actual)

    def test_create_bear_and_feed_carrot(self):
        expected = True
        actual = self.bear.eat(self.carrot)
        self.assertEqual(expected, actual)

    def test_create_Omnivore(self):
        expected = True
        actual = isinstance(self.bear, Omnivore)
        self.assertEqual(expected, actual)


#########

    def test_new_goat_eats_carrots_and_is_full(self):
        self.goat.eat(self.carrot)
        expected = 10
        actual = self.goat.fullness_scale
        self.assertEqual(expected, actual)

    def test_a_new_goat_that_slept_can_play_but_not_play_again(self):
        self.goat.start_sleeping()
        actual = self.goat.play(self.hide_and_seek)
        expected = False
        actual = self.goat.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_a_new_goat_cannot_play(self):
        expected = False
        actual = self.goat.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_go_to_sleep(self):
        self.goat.start_sleeping()
        expected = False
        actual = self.goat.start_sleeping()
        self.assertEqual(expected, actual)

    def test_sleeping_goat_cannot_eat(self):
        self.goat.start_sleeping()
        expected = 'I am sleeping. Grr.'
        actual = self.goat.eat(self.carrot)
        self.assertEqual(expected, actual)

    def test_create_goat_and_sleep(self):
        expected = True
        actual = self.goat.start_sleeping()
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_vegies(self):
        expected = True
        actual = self.goat.eat(self.carrot)
        self.assertEqual(expected, actual)

    def test_create_goat_and_feed_steak(self):
        expected = False
        actual = self.goat.eat(self.steak)
        self.assertEqual(expected, actual)

    def test_create_Vegetarian(self):
        expected = True
        actual = isinstance(self.goat, Vegetarian)
        self.assertEqual(expected, actual)

####

    def test_new_lion_eats_steak_and_is_full(self):
        self.lion.eat(self.steak)
        expected = 10
        actual = self.lion.fullness_scale
        self.assertEqual(expected, actual)

    def test_a_new_lion_that_slept_can_play_but_not_play_again(self):
        self.lion.start_sleeping()
        actual = self.lion.play(self.hide_and_seek)
        expected = False
        actual = self.lion.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_a_new_lion_cannot_play(self):
        expected = False
        actual = self.lion.play(self.hide_and_seek)
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_go_to_sleep(self):
        self.lion.start_sleeping()
        expected = False
        actual = self.lion.start_sleeping()
        self.assertEqual(expected, actual)

    def test_sleeping_lion_cannot_eat(self):
        self.lion.start_sleeping()
        expected = 'I am sleeping. Grr.'
        actual = self.lion.eat(self.steak)
        self.assertEqual(expected, actual)

    def test_create_lion_and_sleep(self):
        expected = True
        actual = self.lion.start_sleeping()
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_steak(self):
        expected = True
        actual = self.lion.eat(self.steak)
        self.assertEqual(expected, actual)

    def test_create_lion_and_feed_carrot(self):
        expected = False
        actual = self.lion.eat(self.carrot)
        self.assertEqual(expected, actual)

    def test_new_create_lion_that_got_a_carrot_is_still_hungry(self):
        self.lion.eat(self.carrot)
        expected = 0
        actual = self.lion.fullness_scale
        self.assertEqual(expected, actual)

    def test_create_Carnivore(self):
        expected = True
        actual = isinstance(self.lion, Carnivore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit = False)

