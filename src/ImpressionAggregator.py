from datetime import datetime, date, timedelta
import json
from pathlib import Path
import os
import sys
import pandas as pd
from multiprocessing import Pool

homeDir = Path(__file__).parents[1]
dataDir = "{0}/resources/data".format(homeDir)
modelDir = "{0}/src/model".format(homeDir)
sys.path.insert(1, modelDir)

from ImpressionEvent import ImpressionEvent
from ClickEvent import ClickEvent
from ImpressionStatistics import ImpressionStatistics
from ImpressionStatisticsKey import ImpressionStatisticsKey


def reader(filename):
	return pd.read_json(filename)


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
	impression_files = [
		f for f in Path(dataDir).iterdir() if f.match("impressions-*.json")
	]
	click_files = [f for f in Path(dataDir).iterdir() if f.match("clicks-*.json")]

	impressions_df_list = []
	for impressions_file_path in impression_files:
		impressions_df_list.append(reader(impressions_file_path))
	impressions_df = pd.concat(impressions_df_list)

	clicks_df_list = []
	for clicks_file_path in click_files:
		clicks_df_list.append(reader(clicks_file_path))
	clicks_df = pd.concat(clicks_df_list)

	impression_clicks_df = pd.DataFrame(
		pd.concat([impressions_df, clicks_df]),
		columns=[
			"id", "country_code", "advertiser_id", 'impression_id', 'revenue'
		])
	
	"""
	Here it starts to be shady for me. I need more time and better resources learning it.
	I will spend some time later to do the following:
		1. Add impressions (int, default 1) column to the impression_clicks_df
		2. Add clics clumn as expression (0 if impression_clicks_df[impression_id] is None else 1)
		3. build aggregated_df as the following (I would use SQL now)
			select 
						app_id,
						country_code,
						sum(impressions) as total_imptressions,
						sum(clicks) as total_clicks,
						sum(case when revenue is null then 0 else revenue end) as total_revenue
			from impression_clicks_df
			group by app_id, country_code
			order by app_id, country_code, total_revenue desc, total_clicks desc, total_impressions desc
		4. Build recommendation as the following:
			with app_country_stats as (
				select 
					app_id, 
					country_code, 
					count(*) as total_impressions,
					sum(case when impression_id is null then 0 else 1 end) as total_clicks,
					sum(case when impression_id is null then 0.00 else cast(revenue as decimal(18,2)) as total_revenue
				from impression_clicks_df
				group by app_id, country_code
				)
			select 
						app_id,
						country_code,
						(select advertiser_id, count(*) as total_impressions
						 from impression_clicks_df as ic
						 where ic.country_code = asc.country_code
						 and ic.app_id = asc.app+id
						 order by total_impressions desc
						 limit 5) as recommended_advertiser_ids
			from app_country_stats as acs
			
			
	"""

if __name__ == "__main__":
	main()

