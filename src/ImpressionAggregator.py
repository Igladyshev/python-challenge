from pathlib import Path
import os
import sys
import pandas as pd

homeDir = Path(__file__).parents[1]
dataDir = "{0}/resources/data".format(homeDir)
modelDir = "{0}/src/model".format(homeDir)
sys.path.insert(1, modelDir)


def reader(filename):
    return pd.read_json(filename)


def get_click_event(clicks_json, impression_id):
    for click_event in clicks_json:
        if click_event["impression_id"] == impression_id:
            return click_event


def get_clicks_file_path(click_files, pattern):
    for path in click_files:
        base_name = "{0}".format(os.path.basename(path))
        if base_name == "clicks-{0}".format(pattern):
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

    impression_clicks_df = pd.DataFrame(pd.concat([impressions_df, clicks_df]))
    values = {'advertiser_id': 0, 'revenue': 0.00, 'impression_id': ''}
    impression_clicks_df.fillna(value=values)
    impression_clicks_clean_df = impression_clicks_df[
        ["id", "country_code", "advertiser_id", "impression_id", "revenue"]]
    impressions_adv_summary_df = impression_clicks_clean_df.groupby(["country_code", "advertiser_id"]).apply(
        lambda s: pd.Series({
            "impressions": s["id"].count()
        })).sort_values(["country_code", "impressions"], ascending=False).reset_index(drop=False)
    print(impressions_adv_summary_df.groupby("country_code").head(5))


if __name__ == "__main__":
    main()
