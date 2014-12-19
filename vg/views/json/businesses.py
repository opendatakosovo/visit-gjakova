from flask import Response
from flask.views import View
import simplejson as json
from vg import utils
from urllib2 import urlopen

class Businesses(View):

    def dispatch_request(self, category=None):

        api_url = utils.get_api_url()
        req_url = None

        if category == None:
            req_url = "%s/json/businesses" % api_url
        else:
            req_url = "%s/json/businesses/%s" % (api_url, category.replace(' ', '%20'))

        result = urlopen(req_url).read()

        # Build response object.
        resp = Response(
            response=result,
            mimetype='application/json')

        # Return response.
        return resp
