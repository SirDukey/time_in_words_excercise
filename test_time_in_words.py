from time_in_words import time_in_words

"""python3 -m pytest -v"""

def test_o_clock():
    assert time_in_words(5, 0) == 'five o\' clock'

def test_one_min_past():
    assert time_in_words(5,1) == 'one minute past five'

def test_ten_min_past():
    assert time_in_words(5, 10) == 'ten minutes past five'

def test_quarter_past():
    assert time_in_words(5, 15) == 'quarter past five'

def test_twenty_eight_past():
    assert time_in_words(5, 28) == 'twenty eight minutes past five'

def test_half_past():
    assert time_in_words(5, 30) == 'half past five'

def test_twenty_to():
    assert time_in_words(5, 40) == 'twenty minutes to six'

def test_quarter_to():
    assert time_in_words(5, 45) == 'quarter to six'

def test_thirteen_to():
    assert time_in_words(5, 47) == 'thirteen minutes to six'

def test_sixty_min():
    assert time_in_words(5, 60) == 'six o\' clock'

def test_min_in_contraints():
    assert time_in_words(5, 70) == 'minutes cannot be more than 60'

def test_hour_in_contraints():
    assert time_in_words(13, 0) == 'hours must be in 12 hour format'