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
	advertiser_id = 0
	impressions = 0
	clicks = 0
	revenue = 0.00
	period_start = "1970-01-01"
	period_end = "2022-01-01"

	def __init__(self, app_id, country_code, advertiser_id):
		self.app_id = app_id
		self.country_code = country_code
		self.advertiser_id = advertiser_id
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

	def addRevenue(statistics, revenue):
		#if isinstance(revenue, double):
		statistics.revenue += revenue

		return statistics

	def calculateRevenue(clicks):
		totalRevenue = 0.00
		for click in clicks:
			if click.revenue is not None:
				totalRevenue += click.revenue
		return totalRevenue

	def to_dict(self):
		return {
			"app_id": self.app_id,
			"country_code": self.country_code,
			"advertiser_id": self.advertiser_id,
			"impressions": self.impressions,
			"clicks": self.clicks,
			"revenue": self.revenue
		}


DATETIME_FORMAT = "%Y%m%dT%H%M%S"
COUNTRIES = ["US", "IS", "UA"]


def main():
	"The main function is to generate test data"
	impressionEvents = []
	for i in range(100):

		impressionEvents.append(
			ImpressionEvent(
				id=None,
				app_id=random.randint(1, 9),
				country_code=COUNTRIES[random.randint(0, len(COUNTRIES) - 1)],
				advertiser_id=random.randint(1, 10)))

	clicks = []
	for impression in impressionEvents:
		if random.randint(1, 10) >= 3:
			clicks.append(ClickEvent(impression.id, random.random()))
	homeDir = Path(__file__).parents[2]
	dataDir = "{0}/{1}".format(homeDir, "resources/data")

	fileImpressions = open("{1}/impressions-{0}.json".format(
		datetime.now().strftime(DATETIME_FORMAT), dataDir), "a")

	fileImpressions.write(
		json.dumps(impressionEvents, default=ImpressionEvent.to_dict))

	fileImpressions.flush()
	fileImpressions.close()

	fileClicks = open("{1}/clicks-{0}.json".format(
		datetime.now().strftime(DATETIME_FORMAT), dataDir), "a")

	fileClicks.write(json.dumps(clicks, default=ClickEvent.to_dict))

	fileClicks.flush()
	fileClicks.close()


if __name__ == "__main__":
	main()

