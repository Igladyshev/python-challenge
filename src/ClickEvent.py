from datetime import datetime
from ImpressionEvent import ImpressionEvent
import json

class ClickEvent():
    impression_id = ""
    create_datetime_utc = ""
    revenue = 0.00
    
    def __init__ (self, impression_id, revenue):
        self.impression_id = impression_id
        self.create_datetime_utc = datetime.now().isoformat()
        self.revenue = revenue
    
    def to_dict (click):
        if isinstance(click, ClickEvent):
            return {
                "impression_id": click.impression_id,
                "create_datetime_utc": click.create_datetime_utc,
                "revenue": click.revenue
            }
        else:
            type_name = type(impression)
            raise TypeError("Unexpected type {0}".format(type_name))
    
    
    def from_dict(dictClick):
        if isinstance(dictClick, dict):
            return ClickEvent(dictClick["impression_id"], dictClick["revenue"])
        else:
            type_name = type(impression)
            raise TypeError("Unexpected type {0}".format(type_name))

def main():
    impression = ImpressionEvent(None, 1, "US", 1)
    click = ClickEvent(impression.id, 2.05)
    dictClick = ClickEvent.to_dict(click)
    jsonClick = json.dumps(click, default = ClickEvent.to_dict)
    print("Json: {0}".format(jsonClick))
    print("Type of encoded impression {0}".format(type(jsonClick)))
    dictClcik = json.loads(jsonClick)
    print("Type of decoded impression {0}".format(type(dictClick)))
    print("Dictionary {0}".format(dictClick))
    decodedClick = ClickEvent.from_dict(dictClick)
    print("Decoded class {0}".format(type(decodedClick)))
    
    
	
if __name__ == "__main__":
	main()