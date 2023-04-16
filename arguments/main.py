# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greet_tmplt=f'Hello, <name>!'):
    return greet_tmplt.replace('<name>', name)


def force(mass, body='earth'):
    gravities = {
        'sun' :  274,
        'mercury': 3.7, 
        'venus': 8.9, 
        'earth':9.8, 
        'moon': 1.6, 
        'mars': 3.7, 
        'jupiter':23.1, 
        'saturn': 10.4, 
        'uranus': 8.7, 
        'neptune': 11, 
        'pluto': 0.6
    }
    
    return gravities[body] * mass

print(force(0.013,'pluto'))

def pull(m1, m2, d):
    return 6.674 * (10**-11 * m1 * m2/( d**2))
    