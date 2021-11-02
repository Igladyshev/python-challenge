from datetime import datetime
from ImpressionEvent import ImpressionEvent
import json


class ClickEvent():
    impression_id = ""
    revenue = 0.00

    def __init__(self, impression_id, revenue):
        self.impression_id = impression_id
        self.revenue = revenue

    def to_dict(self):
        return {
            "impression_id": self.impression_id,
            "revenue": self.revenue
        }


def main():
    impression = ImpressionEvent(None, 1, "US", 1)
    click = ClickEvent(impression.id, 2.05)
    dict_click = click.to_dict()
    json_click = json.dumps(click, default=ClickEvent.to_dict)
    print("Json: {0}".format(json_click))
    print("Type of encoded impression {0}".format(type(json_click)))

if __name__ == "__main__":
    main()
