
from astropy.wcs import WCS

from astroquery import log
log.setLevel('ERROR')
from astroquery.astrometry_net import AstrometryNet

from astroquery.simbad import Simbad

class Queries:
    wcs = None
    def initialize(self, path, api_key):
        AstrometryNet.api_key = api_key
        self.wcs = WCS(AstrometryNet.solve_from_image(path))        

    def getCoordinates(self, x, y):
        sky = self.wcs.pixel_to_world(x, y)
        Simbad.add_votable_fields('v*')
        return sky
        
    def querySimbad(self, x, y):
        res = Simbad.query_region(self.getCoordinates(x,y), radius='0d3m0s')
        return res
