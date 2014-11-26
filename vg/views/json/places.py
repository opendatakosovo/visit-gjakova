from flask import Response
from flask.views import View
import simplejson as json

places_json = {
    "historic-sites":[
        {
            "name": "The Hadum Mosque",
            "description": "A nice mosque.",
            "coordinates":{
                "lat": 42.379197046703354,
                "lon": 20.42738065123558
            }
        }
    ],
    "museums":[
        {
            "name": "Ethnographic museum of Gjakova",
            "description": "A nice museum.",
            "coordinates":{
                "lat": 42.37946650946881,
                "lon": 20.430760234594345
            }
        }
    ],
    "parks":[
        {
            "name": "Parku i qytetit",
            "description": "A nice park.",
            "coordinates":{
                "lat": 42.384055124338275,
                "lon": 20.430073589086533
            }
        },
        {
            "name": "Parku i Lirise",
            "description": "A nice park.",
            "coordinates":{
                "lat": 42.37429103713273,
                "lon":  20.431983321905136
            }
        }
    ],
    "cafes":[
        {
            "name": "Caffe Bar Corbusier",
            "description": "A nice cafe.",
            "coordinates":{
                "lat": 42.38006883382208,
                "lon": 20.430438369512558
            }
        },
        {
            "name": "Cafe Bar 1 2 3",
            "description": "A nice cafe.",
            "coordinates":{
                "lat": 42.37743374595815, 
                "lon": 20.43169230222702
            }
        },
        {
            "name": "Lord's",
            "description": "A nice cafe.",
            "coordinates":{
                "lat": 42.38068892219377,
                "lon": 20.427054092288017
            }
        },
        {
            "name": "Amici",
            "description": "A nice cafe.",
            "coordinates":{
                "lat": 42.38084346348469,
                "lon": 20.427080914378166
            }
        },
        {
            "name": "1595",
            "description": "A nice cafe.",
            "coordinates":{
                "lat": 42.38143388696538, 
                "lon": 20.427086278796196
            }
        }
    ],
    "restaurants":[
        {
            "name": "Fast Food Dea Food",
            "description": "A nice restaurant.",
            "coordinates":{
                "lat": 42.38384115493345,
                "lon": 20.43259486556053
            }
        },
        {
            "name": "Hani i Haracise",
            "description": "A nice restaurant.",
            "coordinates":{
                "lat": 42.37868598064419,
                "lon": 20.427894294261932
            }
        }
    ],
    "bars":[
        {
            "name": "Shpija e Vjeter",
            "description": "A nice bar.",
            "coordinates":{
                "lat": 42.38094060883706,
                "lon": 20.42412981390953
            }
        },
        {
            "name": "Deep Bar",
            "description": "A nice bar.",
            "coordinates":{
                "lat": 42.38144973718364,
                "lon": 20.427107736468315
            }
        },
        {
            "name": "Hapesira Bashkepunuese",
            "description": "A nice bar.",
            "coordinates":{
                "lat": 42.38088308939546,
                "lon": 20.427070185542107
            }
        }
    ],
    "accomodations":[
        {
            "name": "Hotel Pashtriku",
            "description": "A nice hotel",
            "coordinates":{
                "lat": 42.3831913174557,
                "lon": 20.42914018034935
            }
        },
        {
            "name": "Hotel Carshia e Jupave",
            "description": "A nice hotel",
            "coordinates":{
                "lat": 42.3816439020326,
                "lon": 20.427611991763115
            }
        }
    ]
}

class Places(View):

    def dispatch_request(self, category):

        # Build response object.
        resp = Response(
            response=json.dumps(places_json[category]),
            mimetype='application/json')

        # Return response.
        return resp
