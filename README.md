# python-challenge
This is my firt Python experience done on 2019 iPad Pro. Wish me luck :)

## Requirements

Requirements are in [Verve Group Engineering Challenge](https://gist.github.com/alexnastetsky/b02e292ae127450aa82781c83762a37d#business-model) gihub repo

## Project structure

* src: the source code folder
  * model : the model objects
    * ImpressionEvent.py 
    * ClickEvent.py 
    * ImpressionStatistics.py
  * ImpressionAggregator.py: thre main application doing all the magic
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

## How to execute statistics Aggregator?
Even easier!  
1. Open src/ImoressionAggregator.py in your favorite Python IDE
2. Run it
3. Read output in console:  
`{
  "app_id": 1, 
  "country_code": "US", 
  "period_start": "2021-10-21", 
  "period_end": "2021-10-22", 
  "impressions": 155801,
  "clicks": 62340, 
  "revenue": 31013.0
}`
