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
Even easier!
Just run the `Aggregator.py` and you will get something like this:
```
   country_code  advertiser_id  impressions
0            US            1.0          119
1            US            2.0          109
2            US            5.0          102
3            US           10.0          101
4            US            4.0          100
10           UA           10.0          121
11           UA            1.0          116
12           UA            2.0          107
13           UA            8.0          105
14           UA            4.0           97
20           IS            5.0          112
21           IS            9.0          107
22           IS            2.0          106
23           IS            7.0          106
24           IS            3.0           99
```


