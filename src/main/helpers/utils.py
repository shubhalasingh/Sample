import json

class DTjsondecoder(json.JSONEncoder):

    """
    This functions encodes objects and return json
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)