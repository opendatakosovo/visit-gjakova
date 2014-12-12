from flask import Response
from flask.views import View
import simplejson as json
from vg import utils
from urllib2 import urlopen

class Places(View):

    def dispatch_request(self):

        api_url = utils.get_api_url()

        req_url = "%s/json/places" % api_url

        result = urlopen(req_url).read()

        # Build response object.
        resp = Response(
            response=result,
            mimetype='application/json')

        # Return response.
        return resp
