# python-challenge
This is my firt Python experience done on 2019 iPad Pro. Wish me luck :)

## Business Model

Advertisement banners are displayed to users in a mobile application (app_id) in a country (country code) from an advertiser (advertiser_id). When this happens, an impression event is recorded and stored. Optionally, if the user clicks on the banner, a click event is recorded.

## Input

### Arguments

Appliction accepts 2 lists of file names with click and impression events.

### Impression event schema

* id (string): a UUID that identifies the impression.
* create_datetime_utc (string): the event timestamp formatted using pattern: "YYYY-MM-dd'T'HH:mm:ss.SSSXXX", for example "2000-10-31T01:30:00.000-05:00"
* app_id (integer): an identifier of the application showing the impression.
* country_code (string): a 2-letter code for the country. It doesn't comply to any standard like ISO 3166.
* advertiser_id (integer): an identifier of the advertiser that bought the impression.

Example data can be found on impressions.json.

### Click event schema

* impression_id (string): a reference to the UUID of the impression where the click was produced.
* create_datetime_utc: (string): the event timestamp formatted as ISO-8601: "YYYY-MM-dd'T'HH:mm:ss.SSSXXX"
* revenue (double): the quantity of money paid by the advertiser when the click is tracked.

Example data can be found on clicks.json.
