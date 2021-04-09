import json
from ..default.renderer.base import Author
from ..default.renderer.paidmessage import Colors
from ..default.renderer.paidsticker import Colors2


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author) or isinstance(obj, Colors) or isinstance(obj, Colors2):
            return vars(obj)
        return json.JSONEncoder.default(self, obj)
