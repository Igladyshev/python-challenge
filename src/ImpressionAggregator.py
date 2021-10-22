from datetime import datetime, date, timedelta
import json
from pathlib import Path
import os
import sys

homeDir = Path(__file__).parents[1]
dataDir = "{0}/resources/data".format(homeDir)
modelDir = "{0}/src/model".format(homeDir)
sys.path.insert(1, modelDir)

from ImpressionEvent import ImpressionEvent 
from ClickEvent import ClickEvent
from ImpressionStatistics import ImpressionStatistics
 
def main():
  impressionFiles = [f for f in Path(dataDir).iterdir() if f.match("impressions-*.json")]
  clickFiles = [f for f in Path(dataDir).iterdir() if f.match("clicks-*.json")]
  
  
  stats = ImpressionStatistics(app_id = 1, country_code = "US", period_start = "{0}".format(date.today() - timedelta(1)), period_end = "{0}".format(date.today()))
  
  for impressionFilePath in impressionFiles:   
    print("Impressions file name={0}, size={1}\n".format(impressionFilePath, os.path.getsize(impressionFilePath)))
  
    with open(impressionFilePath, 'r') as impressionFile:
      data = impressionFile.read()
    impressionFile.close()
    impressionsJson = json.loads(data)
    impressions = len(impressionsJson)

    print("Number of impressions={0}".format(impressions))

    ImpressionStatistics.addImpressions(stats, impressions)
  
  for clicksFilePath in clickFiles:
    print("Clicks file name={0}, size={1}\n".format(clicksFilePath, os.path.getsize(clicksFilePath)))
    
    with open(clicksFilePath, 'r') as clicksFile:
      data = clicksFile.read()
    
    clicksFile.close()
    
    clicksJson = json.loads(data)
    clicks = len(clicksJson)
    
    print("Number of clicks={0}".format(clicks))
    
    ImpressionStatistics.addClicks(stats, clicks)
    for clickEvent in clicksJson:
      #print("Click Event {0}".format(clickEvent))
      ImpressionStatistics.addRevenue(stats, float(clickEvent["revenue"]))
  
  statsDict = ImpressionStatistics.to_dict(stats)
  print(json.dumps(statsDict))
    
if __name__ == "__main__":
	main()
  