colors = ('red', 'blue', 'green', 'orange', 'yellow', 'purple', 'brown',
            'black')
countries = {
        'Guyana': ['Venezuella', 'Brazil', 'Suriname'],
        'Suriname': ['Guyana', 'Brazil', 'French Guiana'],
        'French Guiana': ['Suriname', 'Brazil'],
        'Brazil': ['French Guiana', 'Suriname', 'Uruguay',
            'Paraguay', 'Bolivia', 'Peru', 'Columbia',
            'Venezuella', 'Guyana', 'Suriname'],
        'Uruguay': ['Brazil', 'Argentina'],
        'Argentina': ['Uruguay', 'Brazil', 'Paraguay', 'Bolivia', 'Chile'],
        'Chile': ['Peru', 'Bolivia', 'Argentina'],
        'Paraguay': ['Brazil', 'Bolivia', 'Uruguay', 'Argentina'],
        'Bolivia':['Peru', 'Brazil', 'Paraguay', 'Argentina', 'Chile'],
        'Peru': ['Chile', 'Bolivia', 'Brazil', 'Equador', 'Columbia'],
        'Equador': ['Peru', 'Columbia'],
        'Columbia': ['Equador', 'Peru', 'Brazil', 'Venezuella'],
        'Venezuella': ['Columbia', 'Brazil', 'Guyana'],
        'Guyana': ['Venezuella', 'Brazil', 'Suriname'],
        'Suriname': ['Guyana', 'Brazil', 'French Guiana'],
        'French Guiana': ['Brazil', 'Suriname'],
        'Galapogos Islands': [],
        'Falkland Islands': [],
        'South Georgia': []}

# Get empty nodes
# Get richest nodes
# Appoint the most expensive color to the vertice with the highest number of relations

def get_richest():
    sorted_keys = countries.keys()
    sorted_keys.sort(
            cmp=lambda x, y: len(countries[x]) - len(countries[y]),
            reverse=True)
    return sorted_keys


def set_color():
# Coloring algorithm
    raise NotImplementedError
