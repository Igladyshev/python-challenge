import ImpressionEvent

class ImpressionStatisticsKey():
  app_id = 0
  country_code = "US"
  advertiser_id = 0
  
  def __init__ (self, app_id, country_code, advertiser_id):
    self.app_id = app_id
    self.country_code = country_code
    self.advertiser_id = advertiser_id
    
  def toDict(self):
    return {
      "app_id": self.app_id,
      "country_code": self.country_code,
      "advertiser_id": self.advertiser_id
    }
    
  def toString(self):
    return "{0}:{1}:{2}".format(self.app_id, self.country_code, self.advertiser_id)
    
  def getKey(impressionEvent):
    return ImpressionStatisticsKey(impressionEvent.app_id, impressionEvent.country_code, impressionEvent.advertiser_id)
