import requests as request
from bs4 import BeautifulSoup


class GoogleTrends:
    def __init__(self):
        self.page = request.get(
            "https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN"
        )
        self.document = BeautifulSoup(self.page.text, "lxml")

    def unitTest(self):
        print(self.document.text)

    def getReason(self, keywords: str) -> str:
        pass


x = GoogleTrends().unitTest()
