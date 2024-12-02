from ninja.responses import NinjaJSONEncoder
from ninja.renderers import JSONRenderer
import datetime

class MyJsonEncoder(NinjaJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%d-%m-%Y %H:%M:%S")
        return super().default(obj)


class MyJSONRenderer(JSONRenderer):
    encoder_class = MyJsonEncoder