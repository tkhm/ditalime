import codecs
from .constants import FieldTypes as FT


class DitaModel:
    """"Data Model for Dita"""

    fields = {
            "contents": {"req": True, "type": FT.long_string}
    }

    def __init__(self, filename):
        self.filename = filename

    def save_record(self, data):
        """Save a dict of data to the file"""

        with codecs.open(self.filename, "w", "utf-8") as f:
            f.write(data["contents"])


class DitaMetaModel:
    """"Meta Data Model for Dita"""

    fields = {
            "topic": {
                "req": True,
                "type": FT.string_list,
                "values": [
                    "concept", "reference", "task"
                ]
            },
    }
