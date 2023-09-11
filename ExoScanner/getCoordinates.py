
from astropy.wcs import WCS

from astroquery import log
log.setLevel('ERROR')
from astroquery.astrometry_net import AstrometryNet
from astroquery.exceptions import TimeoutError as AstrometryTimeoutError

from astroquery.simbad import Simbad

class Queries:
    wcs = None
    def initialize(self, path, api_key):
        ast = AstrometryNet()
        ast.api_key = api_key
        try_again = True
        submission_id = None

        while try_again:
            try:
                if not submission_id:
                    print("Submitting first time")
                    wcs_header = ast.solve_from_image(path, force_image_upload=True,submission_id=submission_id)
                else:
                    print("Monitoring submission ",submission_id)
                    wcs_header = ast.monitor_submission(submission_id,solve_timeout=120)
            except AstrometryTimeoutError as e:
                submission_id = e.args[1]
            else:
            # got a result, so terminate
                try_again = False

        if wcs_header:
            # Code to execute when solve succeeds
            self.wcs = WCS(wcs_header)
        else:
            # Code to execute when solve fails
            print("Solving failed")        

    def getCoordinates(self, x, y):
        sky = self.wcs.pixel_to_world(x, y)
        Simbad.add_votable_fields('v*')
        return sky
        
    def querySimbad(self, x, y):
        res = Simbad.query_region(self.getCoordinates(x,y), radius='0d3m0s')
        return res
