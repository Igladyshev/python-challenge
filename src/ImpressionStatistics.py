import datetime
import random
import json

from ImpressionEvent import ImpressionEvent
from ClickEvent import ClickEvent

class ImpressionStatistics():
  app_id = 1
  country_code = "US"
  impressions = 0
  clicks = 0
  revenue = 0.00
  period_start = datetime.datetime(1970, 1, 1)
  period_end = datetime.datetime(2200, 1, 1)
  
  def __init__ (self, app_id, country_code, period_start, period_end):
    self.app_id = app_id
    self.country_code = country_code
    self.period_start = period_start
    self.period_end = period_end
    self.impressions = 0
    self.clicks = 0
    self.revenue = 0.00
    
  def addImpressions(statistics, impressions):
    if isinstance(impressions, int):
      statistics.impressions += impressions
    elif isinstance(impressions, ImpressionEvent):
      statistics.impressions += 1
    
    return statistics
    
  
  def addClicks(statistics, clicks):
    if isinstance(clicks, int):
      statistics.clicks += clicks
    elif isinstance(clicks, ClickEvent):
      statistics.impressions += 1
    
    return statistics
   
  
  def addRevenue (statistics, revenue):
    if isinstance(clicks, double):
      statistics.revenue += revenue
    
    return statistics
    
  def calculateRevenue(clicks):
    totalRevenue = 0.00
    for click in clicks:
      if click.revenue is not None:
        totalRevenue += click.revenue
    return totalRevenue 

def main():
  impressionEvents = []
  for i in range(10):
    impressionEvents.append(ImpressionEvent(id = None, app_id = 1, country_code = "US", advertiser_id = random.randint(1234567890, 9876543210)))
    
  clicks = []
  for impression in impressionEvents :
    if random.randint(1,10) >= 7:
      clicks.append(ClickEvent(impression.id, random.randrange(0,2)))
    
  print("Impressions {0}, clicks {1}".format(len(impressionEvents), len(clicks)))
  
  #for impression in impressionEvents:
  print(json.dumps(impressionEvents, default = ImpressionEvent.to_dict))

  
  
if __name__ == "__main__":
	main()