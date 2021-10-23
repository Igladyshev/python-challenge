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
    
    def to_dict (self):
    	return {
    		"impression_id": self.impression_id,
				"create_datetime_utc": self.create_datetime_utc,
        "revenue": self.revenue
      }
    
def main():
    impression = ImpressionEvent(None, 1, "US", 1)
    click = ClickEvent(impression.id, 2.05)
    dictClick = click.to_dict()
    jsonClick = json.dumps(click, default = ClickEvent.to_dict)
    print("Json: {0}".format(jsonClick))
    print("Type of encoded impression {0}".format(type(jsonClick)))
    dictClcik = json.loads(jsonClick)
    print("Type of decoded impression {0}".format(type(dictClick)))
    print("Dictionary {0}".format(dictClick))
    print("Decoded class {0}".format(type(decodedClick)))
    
    
	
if __name__ == "__main__":
	main()
