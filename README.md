# python-challenge
This is my first Python experience done on 2019 iPad Pro. Wish me luck :)

## Requirements

Requirements are in [Verve Group Engineering Challenge](https://gist.github.com/alexnastetsky/b02e292ae127450aa82781c83762a37d#business-model) gihub repo

## Project structure

* src: the source code folder
  * model : the model objects
    * ImpressionEvent.py 
    * ClickEvent.py 
    * ImpressionStatistics.py
  * ImpressionAggregator.py: the main application doing all the magic
* resources: different resource files
  * data: here I keep the test data
    * impressions-20211022T065924.json: impression test data JSON file. 
    * impressions-...
    * clicks- 20211022T065924.json: clicks test data JSON file
    * clicks-...

## How to generate Test Data?
Short answer is: "Easy!":
1. Clone the project to your local computer/ipad
2. Open src/model/ImpressionStatistics.py in your favorite Python IDE
3. modify the code bellow to your desire:
4. execute *ImpressionStatistics.py*  
  
Generated files are stored into `dataDir` which is calculated as the following:  
`
homeDir = Path(__file__).parents[2] // this is being calculated within src/model/ImpressionStatistics.py
dataDir = "{0}/resources/data".format(homeDir)
`  
Files being named as the following:  
`"{1}/clicks-{0}.json".format(datetime.now().strftime(DATETIME_FORMAT), dataDir`,  
where `DATETIME_FORMAT = "%Y%m%dT%H%M%S"`

### Code to modify when test generating
```
  // You can change countries array
  COUNTRIES = ["US", "CA", "MX", "UK", "FR", "UA", "GE", "CZ", "DA", "NO", "SE", "ES"]

def main():
  "The main function is to generate test data"
  impressionEvents = []
  // here you set the number of impressionEvents to be generated
  for i in range(12345):
    
    impressionEvents.append(ImpressionEvent(id = None, app_id = random.randint(1, 9), country_code = COUNTRIES[random.randint(0, len(COUNTRIES) - 1)], advertiser_id = random.randint(5, 10)))
    
  clicks = []
  for impression in impressionEvents :
    // here we define how often click event happens related to impreassionEvents
    if random.randint(1,10) >= 7:
```
## How to execute statistics Aggregator?
I tried, but it is too much to absorb in a few days, so here is what I would do, if I knew Python. I try to explain it in language I most familiar with, SQL:

		1. Add impressions (int, default 1) column to the impression_clicks_df
		2. Add clics clumn as expression (0 if impression_clicks_df[impression_id] is None else 1)
		3. build aggregated_df as the following (I would use SQL now)
  ```
			select 
						app_id,
						country_code,
						sum(impressions) as total_imptressions,
						sum(clicks) as total_clicks,
						sum(case when revenue is null then 0 else revenue end) as total_revenue
			from impression_clicks_df
			group by app_id, country_code
			order by app_id, country_code, total_revenue desc, total_clicks desc, total_impressions desc
   ```
		4. Build recommendation as the following:
  ```
			with app_country_stats as (
				select 
					app_id, 
					country_code, 
					count(*) as total_impressions,
					sum(case when impression_id is null then 0 else 1 end) as total_clicks,
					sum(case when impression_id is null then 0.00 else cast(revenue as decimal(18,2)) as total_revenue
				from impression_clicks_df
				group by app_id, country_code)
			select 
						app_id,
						country_code,
						(select advertiser_id, count(*) as total_impressions
						 from impression_clicks_df as ic
						 where ic.country_code = asc.country_code
						 and ic.app_id = asc.app+id
						 order by total_impressions desc
						 limit 5) as recommended_advertiser_ids
   from app_country_stats 
```

