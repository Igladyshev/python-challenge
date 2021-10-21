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
			
	def to_dict(impression):
		if isinstance(impression, ImpressionEvent):
			dictImpression = {
				"id": impression.id,
				"create_datetime_utc": impression.create_datetime_utc,
				"app_id": impression.app_id,
				"country_code": impression.country_code,
				"advertiser_id": impression.advertiser_id
			}
			return dictImpression
		else:
			type_name = impression.__class__.__name__
			raise TypeError("Unexpected type {0}".format(type_name))
			
	def from_dict(dictImpression):
		return ImpressionEvent(dictImpression["id"], dictImpression["app_id"], dictImpression["country_code"], dictImpression["advertiser_id"]) 
		
def main():
	impression = ImpressionEvent(None, 1, "US", 1)
	jsonImpression = json.dumps(impression, default = ImpressionEvent.to_dict)
	print("Json: {0}".format(jsonImpression))
	print("Type of encoded impression {0}".format(type(jsonImpression)))
	dictImpression = json.loads(jsonImpression)
	print("Type of decoded impression {0}".format(type(dictImpression)))
	print("Dictionary {0}".format(dictImpression))
	decodedImpression = ImpressionEvent.from_dict(dictImpression)
	print("Decoded class {0}".format(type(decodedImpression)))
	
if __name__ == "__main__":
	main()