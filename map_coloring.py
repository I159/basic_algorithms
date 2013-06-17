import copy

colors = ('red', 'blue', 'green', 'orange',
          'yellow', 'purple', 'brown', 'black')
countries = {
        'Guyana': {'color': '',
            'relations': ['Venezuella', 'Brazil', 'Suriname']},
        'Suriname': {'color': '',
            'relations': ['Guyana', 'Brazil', 'French Guiana']},
        'Brazil': {'color': '',
            'relations': ['French Guiana', 'Suriname', 'Uruguay',
            'Paraguay', 'Bolivia', 'Peru', 'Columbia',
            'Venezuella', 'Guyana', 'Suriname']},
        'Uruguay': {'color': '',
            'relations': ['Brazil', 'Argentina']},
        'Argentina': {'color': '',
            'relations': ['Uruguay', 'Brazil', 'Paraguay',
                'Bolivia', 'Chile']},
        'Chile': {'color': '',
                'relations': ['Peru', 'Bolivia', 'Argentina']},
        'Paraguay': {'color': '',
            'relations': ['Brazil', 'Bolivia', 'Uruguay', 'Argentina']},
        'Bolivia':{'color': '',
            'relations': ['Peru', 'Brazil', 'Paraguay',
                'Argentina', 'Chile']},
        'Peru': {'color': '',
            'relations': ['Chile', 'Bolivia', 'Brazil', 'Equador', 'Columbia']},
        'Equador': {'color': '',
            'relations': ['Peru', 'Columbia']},
        'Columbia': {'color': '',
            'relations': ['Equador', 'Peru', 'Brazil', 'Venezuella']},
        'Venezuella': {'color': '',
            'relations': ['Columbia', 'Brazil', 'Guyana']},
        'French Guiana': {'color': '',
            'relations': ['Brazil', 'Suriname']},
        'Galapogos Islands': {'color': '', 'relations': []},
        'Falkland Islands': {'color': '', 'relations': []},
        'South Georgia':  {'color': '', 'relations': []}}


class ColoringMap(object):
    """Map coloring algorythm"""
    # TODO: paint the real map
    def __init__(self):
        self.countries = copy.deepcopy(countries)

    def get_relevant_color(self, relations):
        color_index = 0
        for country in relations:
            if self.countries[country]['color'] == colors[color_index]:
                color_index += 1
        return colors[color_index]

    def set_colors(self):
        for country in self.countries.itervalues():
            country['color'] = self.get_relevant_color(country['relations'])
        return self


class TestMapColoringClass(object):
    def __init__(self):
        c = ColoringMap().set_colors()
        self.countries = c.countries

    def test_count_colors(self):
        colors_count = {}
        for v in self.countries.itervalues():
            if v['color'] not in colors_count:
                colors_count[v['color']] = 1
            else:
                colors_count[v['color']] += 1
        print '=================== CLASS COLORS SCHEME ======================'
        print colors_count

    def test_map_cost(self):
        colors_count = {}
        map_cost = 0
        for v in self.countries.itervalues():
            if v['color'] not in colors_count:
                colors_count[v['color']] = 1
            else:
                colors_count[v['color']] += 1
        for k, v in colors_count.iteritems():
            map_cost += (v * colors.index(k) * 100)
        print '===================== CLASS MAP COST ========================='
        print map_cost

    def test_country_coloring(self):
        print '=================== CLASS COUNTRIES AS IS ===================='
        for k, v in self.countries.iteritems():
            print k, ': ', v
