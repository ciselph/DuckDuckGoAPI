import requests

url_ddg = "https://api.duckduckgo.com/"


def test_ddg0():

    resp = requests.get(url_ddg + "?q=presidents%20of%20the%20united%20states&format=json")

    rsp_data = resp.json()

    assert "Presidents of the United States" in rsp_data["Heading"]

    presidents_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler", "Polk",
             "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
             "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover",
             "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Clinton",
             "Bush", "Obama", "Trump", "Biden"]

    president_search = resp.json()
    RelatedTopics = president_search["RelatedTopics"]

    for president_lastname in presidents_list:
        A = False
        for SingleTopic in RelatedTopics:
            if president_lastname in SingleTopic["FirstURL"]:
                A = True
                print(SingleTopic["Text"])
                break
        if A == False:
            assert "President " + president_lastname + " not found!"
