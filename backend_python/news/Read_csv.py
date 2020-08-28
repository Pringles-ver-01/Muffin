import csv
import json


class Read_csv_create_wordcloud:
    def read(self):
        with open('data/30_news_threeDays_mining.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            t = list()
            for x, y in data:
                aa = dict(text=x, value=y)
                print(aa)
                print(type(aa))
                t.append(aa)
            p = json.dumps(t)
        return p


if __name__ == '__main__':
    Read_csv_create_wordcloud
