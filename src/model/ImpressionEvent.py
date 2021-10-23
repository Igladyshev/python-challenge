import uuid
from datetime import datetime
import json

class ImpressionEvent():
	id = ""
	create_datetime_utc = ""
	app_id = 1
	country_code = "US"
	advertiser_id = 0

	def __init__(self, id = None, app_id = 1, country_code = "US", advertiser_id = 0):
		if id is None:
			self.id = "{0}".format(uuid.uuid4())
		else:
			self.id = id		
		
		self.create_datetime_utc = datetime.now().isoformat()
		self.app_id = app_id
		self.country_code = country_code
		self.advertiser_id = advertiser_id
			
	def to_dict(self):
		return {
				"id": self.id,
				"create_datetime_utc": self.create_datetime_utc,
				"app_id": self.app_id,
				"country_code": self.country_code,
				"advertiser_id": self.advertiser_id
			}
		
def main():
	impression = ImpressionEvent(None, 1, "US", 1)
	jsonImpression = json.dumps(impression, default = ImpressionEvent.to_dict)
	print("Json: {0}".format(jsonImpression))
	print("Type of encoded impression {0}".format(type(jsonImpression)))
	dictImpression = json.loads(jsonImpression)
	print("Type of decoded impression {0}".format(type(dictImpression)))
	print("Dictionary {0}".format(dictImpression))
	
if __name__ == "__main__":
	main()
