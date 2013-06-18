colors = ('red', 'blue', 'green', 'orange', 'yellow', 'purple', 'brown',
            'black')
countries = {
        'Guyana': {'color': '',
            'relations': ['Venezuella', 'Brazil', 'Suriname']},
        'Suriname': {'color': '',
            'relations': ['Guyana', 'Brazil', 'French Guiana']},
        'French Guiana': {'color': '',
            'relations': ['Suriname', 'Brazil']},
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
        'Galapogos Islands': {'color': '', 'relations': []},
        'Falkland Islands': {'color': '', 'relations': []},
        'South Georgia':  {'color': '', 'relations': []}}


colored_countries = {}


class ColoringMap(object):
    def __init__(self):
        # TODO: check what is wrong with deepcopy
        self.countries = countries

    def sort_countries(self):
        sorted_keys = self.countries.keys()
        sorted_keys.sort(
                cmp=lambda x, y: len(countries[x]) - len(countries[y]),
                reverse=True)
        return sorted_keys

    def get_relevant_color(self, relations):
        color_index = len(colors) - 1
        for country in relations:
            if self.countries[country]['color'] == colors[color_index]:
                color_index -= 1
        return colors[color_index]

    def set_colors(self):
        sorted_countries = self.sort_countries()
        country_index = 0
        while country_index < len(sorted_countries):
            country = self.countries[sorted_countries[country_index]]
            if not country['color']:
                if country_index == 0:
                    country['color'] = colors[0]
                else:
                    country['color'] = self.get_relevant_color(
                            country['relations'])
            country_index += 1
        return self.countries


#def sort_countries():
#    sorted_keys = countries.keys()
#    sorted_keys.sort(
#            cmp=lambda x, y: len(countries[x]) - len(countries[y]),
#            reverse=True)
#    return sorted_keys
#
#
#def get_relevant_color(relations):
#    color_index = len(colors) - 1
#    for country in relations:
#        if countries[country]['color'] == colors[color_index]:
#            color_index -= 1
#    return colors[color_index]
#
#
#def set_colors():
#    sorted_countries = sort_countries()
#    country_index = 0
#    while country_index < len(sorted_countries):
#        country = countries[sorted_countries[country_index]]
#        if not country['color']:
#            if country_index == 0:
#                country['color'] = colors[0]
#            else:
#                country['color'] = get_relevant_color(country['relations'])
#        country_index += 1


class TestMapColoringClass(object):
    def __init__(self):
        self.countries = ColoringMap().set_colors()

    def test_count_colors(self):
        colors_count = {}
        for v in self.countries.itervalues():
            if v['color'] not in colors_count:
                colors_count[v['color']] = 1
            else:
                colors_count[v['color']] += 1
        print '====================== CLASS COLORS SCHEME ======================== '
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
        print '========================= CLASS MAP COST ==========================='
        print map_cost

    def test_country_coloring(self):
        print '===================== CLASS COUNTRIES AS IS ===================='
        for k, v in self.countries.iteritems():
            print k, ': ', v


#class TestMapColoring(object):
#    def __init__(self):
#        set_colors()
#
#    def test_count_colors(self):
#        colors_count = {}
#        for v in countries.itervalues():
#            if v['color'] not in colors_count:
#                colors_count[v['color']] = 1
#            else:
#                colors_count[v['color']] += 1
#        print '====================== COLOR SCHEME ======================== '
#        print colors_count
#
#    def test_map_cost(self):
#        colors_count = {}
#        map_cost = 0
#        for v in countries.itervalues():
#            if v['color'] not in colors_count:
#                colors_count[v['color']] = 1
#            else:
#                colors_count[v['color']] += 1
#        for k, v in colors_count.iteritems():
#            map_cost += (v * colors.index(k) * 100)
#        print '========================= MAP COST ==========================='
#        print map_cost
#
#    def test_country_coloring(self):
#        print '===================== COUNTRIES AS IS ===================='
#        for k, v in countries.iteritems():
#            print k, ': ', v
