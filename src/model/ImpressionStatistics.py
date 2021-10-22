from datetime import datetime
from datetime import date
import random
import json
from pathlib import Path

from ImpressionEvent import ImpressionEvent
from ClickEvent import ClickEvent

class ImpressionStatistics():
  app_id = 1
  country_code = "US"
  impressions = 0
  clicks = 0
  revenue = 0.00
  period_start = "1970-01-01"
  period_end = "2022-01-01"
  
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
    #if isinstance(revenue, double):
    statistics.revenue += revenue
    
    return statistics
    
  def calculateRevenue(clicks):
    totalRevenue = 0.00
    for click in clicks:
      if click.revenue is not None:
        totalRevenue += click.revenue
    return totalRevenue 
    
  def to_dict (stats):
    if isinstance(stats, ImpressionStatistics):
      return {
        "app_id": stats.app_id,
        "country_code": stats.country_code,
        "period_start": stats.period_start,
        "period_end": stats.period_end,
        "impressions": stats.impressions,
        "clicks": stats.clicks,
        "revenue": stats.revenue
      }
    else:
      type_name = type(stats)
      raise TypeError("Unexpected type {0}".format(type_name))    
  
DATETIME_FORMAT = "%Y%m%dT%H%M%S"

def main():
  "The main function is to generate test data"
  impressionEvents = []
  for i in range(123456):
    impressionEvents.append(ImpressionEvent(id = None, app_id = 1, country_code = "US", advertiser_id = random.randint(1234567890, 9876543210)))
    
  clicks = []
  for impression in impressionEvents :
    if random.randint(1,10) >= 7:
      clicks.append(ClickEvent(impression.id, random.randrange(0,2)))
  homeDir = Path(__file__).parents[2]
  dataDir = "{0}/{1}".format(homeDir, "resources/data")
  
  fileImpressions = open("{1}/impressions-{0}.json".format(datetime.now().strftime(DATETIME_FORMAT), dataDir), "a")

  fileImpressions.write(json.dumps(impressionEvents, default = ImpressionEvent.to_dict))
  
  fileImpressions.flush()
  fileImpressions.close()

  fileClicks = open("{1}/clicks-{0}.json".format(datetime.now().strftime(DATETIME_FORMAT), dataDir), "a")

  fileClicks.write(json.dumps(clicks, default = ClickEvent.to_dict))
  
  fileClicks.flush()
  fileClicks.close()

  
  
if __name__ == "__main__":
	main()
