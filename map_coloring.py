import copy

colors = ('red', 'blue', 'green', 'orange', 'yellow', 'purple', 'brown',
            'black')
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


class MapColoring(object):
    countries = copy.deepcopy(countries)

    def sort_countries(self):
        sorted_keys = self.countries.keys()
        sorted_keys.sort(
             cmp=lambda x, y: len(self.countries[x]) - len(self.countries[y]),
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
                    country['color'] = self.get_relevant_color(country['relations'])
            country_index += 1
        return self.countries


class NeglectMapColoring(MapColoring):
    def set_colors(self):
        sorted_countries = self.sort_countries()
        for i in sorted_countries:
            country = self.countries[i]
            if not country['color']:
                country['color'] = self.get_relevant_color(
                        country['relations'])
        return self.countries


class MapColoringTestTool(object):
    def __init__(self, algorythm):
        self.countries = algorythm().set_colors()

    def count_colors(self):
        colors_count = {}
        for v in self.countries.itervalues():
            if v['color'] not in colors_count:
                colors_count[v['color']] = 1
            else:
                colors_count[v['color']] += 1
        return colors_count

    def map_cost(self):
        colors_count = {}
        map_cost = 0
        for v in self.countries.itervalues():
            if v['color'] not in colors_count:
                colors_count[v['color']] = 1
            else:
                colors_count[v['color']] += 1
        for k, v in colors_count.iteritems():
            map_cost += (v * colors.index(k) * 100)
        return map_cost

    def map_coloring(self):
        return self.countries


class TestMapColoring(object):
    def __init__(self):
        self.t1 = MapColoringTestTool(MapColoring)

    def test_compare_color_count(self):
        print "\nCOUNT 1: \n", self.t1.count_colors()

    def test_map_coloring(self):
        print '\nCOUNTRIES', countries
        print 'COLORING: \n', self.t1.map_coloring()
