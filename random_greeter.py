import random

plugins_dict = dict()

def returner1(func1):
	plugins_dict[func1.__name__] = func1
	return func1

@returner1
def hi_func(hi_person):
	return f'Hi {hi_person} !'

@returner1
def salute_func(salute_person):
	return f'Salute {salute_person} !!'

@returner1
def hola_func(hola_person):
	return f'Hola {hola_person} !!!'

def random_greeter(person):
	greet_func_name, greet_func = random.choice(list(plugins_dict.items()))
	return greet_func(person), f'{greet_func_name!r} function is used now'

print(random_greeter('Eddie'))
