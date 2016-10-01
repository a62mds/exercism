
class SpaceAge(object):

    def __init__(self, seconds):
        self._seconds = seconds
        self._e_years = seconds * self.years_per_sec

    @property
    def secs_per_year(self):
        return 31557600

    @property
    def years_per_sec(self):
        return 1.0 / self.secs_per_year

    @property
    def seconds(self):
        return self._seconds

    def age_on(self, planet):
        years_on = {'Mercury' : 0.2408467,
                    'Venus'   : 0.61519726,
                    'Earth'   : 1.0,
                    'Mars'    : 1.8808158,
                    'Jupiter' : 11.86261,
                    'Saturn'  : 29.447498,
                    'Uranus'  : 84.016846,
                    'Neptune' : 164.79132}
        return float('{0:.2f}'.format(self._e_years / years_on[planet]))

    def on_mercury(self):
        return self.age_on('Mercury')

    def on_venus(self):
        return self.age_on('Venus')

    def on_earth(self):
        return self.age_on('Earth')

    def on_mars(self):
        return self.age_on('Mars')

    def on_jupiter(self):
        return self.age_on('Jupiter')

    def on_saturn(self):
        return self.age_on('Saturn')

    def on_uranus(self):
        return self.age_on('Uranus')

    def on_neptune(self):
        return self.age_on('Neptune')
