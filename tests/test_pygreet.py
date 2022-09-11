from pygreet import say_hello


def test_it_should_say_the_given_name():
    assert say_hello('Everybody!') == 'Hello, Everybody!'

def test_it_should_say_the_default_content():
    assert say_hello() == 'Hello, World!'
