from datetime import datetime, date, timedelta
import json
from pathlib import Path
import os
import sys
import itertools
from collections import OrderedDict

homeDir = Path(__file__).parents[1]
dataDir = "{0}/resources/data".format(homeDir)
modelDir = "{0}/src/model".format(homeDir)
sys.path.insert(1, modelDir)

from ImpressionEvent import ImpressionEvent
from ClickEvent import ClickEvent
from ImpressionStatistics import ImpressionStatistics
from ImpressionStatisticsKey import ImpressionStatisticsKey


def getClickEvent(clicksJson, impression_id):
	for clickEvent in clicksJson:
		if clickEvent["impression_id"] == impression_id:
			return clickEvent


def getClicksFilePath(clickFiles, pattern):
	for path in clickFiles:
		baseName = "{0}".format(os.path.basename(path))
		if baseName == "clicks-{0}".format(pattern):
			return path


def main():
	impressionStatistics = {}
	impressionFiles = [
		f for f in Path(dataDir).iterdir() if f.match("impressions-*.json")
	]
	clickFiles = [f for f in Path(dataDir).iterdir() if f.match("clicks-*.json")]

	for impressionFilePath in impressionFiles:
		with open(impressionFilePath, 'r') as impressionFile:
			data = impressionFile.read()
		impressionFile.close()
		impressionsJson = json.loads(data)

		baseName = os.path.basename(impressionFilePath)
		clicksFilePath = getClicksFilePath(clickFiles, baseName[12:100])
		if clicksFilePath is not None:
			with open(clicksFilePath, 'r') as clicksFile:
				data = clicksFile.read()
			clicksFile.close()
			clicksJson = json.loads(data)

			for impressionEvent in impressionsJson:
				stats = ImpressionStatistics(
					app_id=impressionEvent["app_id"],
					country_code=impressionEvent["country_code"],
					advertiser_id=impressionEvent["advertiser_id"])

				statsKey = ImpressionStatisticsKey.getKey(stats)
				if statsKey.toString() in impressionStatistics:
					stats = impressionStatistics[statsKey.toString()]

				stats = ImpressionStatistics.addImpressions(stats, 1)
				clickEvent = getClickEvent(clicksJson, impressionEvent["id"])
				if clickEvent is not None:
					stats = ImpressionStatistics.addClicks(stats, 1)
					stats = ImpressionStatistics.addRevenue(stats, clickEvent["revenue"])
				impressionStatistics[statsKey.toString()] = stats

	d = OrderedDict()
	for stats in impressionStatistics.values():
		#print(ImpressionStatistics.to_dict(stats))
		d.setdefault((stats.advertiser_id, stats.country_code), set()).add(
			stats.impressions)

if __name__ == "__main__":
	main()
