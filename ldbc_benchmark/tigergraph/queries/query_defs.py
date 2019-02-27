from tornado.httputil import url_concat
from datetime import datetime
from csv import DictReader

ENDPOINT_URL_PREFIX = "http://127.0.0.1:9000/query/ldbc_snb/"

def get_messages_from_person(person_id, max_num_seeds):
  params = {"seed": person_id, "num_messages": max_num_seeds}
  return url_concat(ENDPOINT_URL_PREFIX + "get_messages_from_person", params)

def is_queries(ids, query_num):
  urls = []
  for id in ids:
    params = {"seed": id}
    url = url_concat(ENDPOINT_URL_PREFIX + "is_{}".format(query_num), params)
    urls.append(url)
  return urls

def ic_queries(path_to_seeds, max_num_seeds, query_num):
  with open(path_to_seeds + "interactive_{}_param.txt".format(query_num), "r") as f:
    reader = DictReader(f, delimiter="|")
    seeds = []
    count = 0
    for row in reader:
      if query_num == 1:
        seed = {"personId":row["personId"], "firstName":row["firstName"]}
      elif query_num == 2:
        max_date = datetime.fromtimestamp(int(row["minDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"personId":row["personId"], "maxDate":max_date}
      elif query_num == 3:
        start_date = datetime.fromtimestamp(int(row["startDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"personId":row["personId"], "startDate":start_date, "durationDays":row["durationDays"], "countryXName":row["countryXName"], "countryYName":row["countryYName"]}
      elif query_num == 4:
        start_date = datetime.fromtimestamp(int(row["startDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"personId":row["personId"], "startDate":start_date, "durationDays":row["durationDays"]}
      elif query_num == 5:
        min_date = datetime.fromtimestamp(int(row["minDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"personId":row["personId"], "minDateEpoch":min_date}
      elif query_num == 6:
        seed = {"personId":row["personId"], "tagName":row["tagName"]}
      elif query_num == 7:
        seed = {"personId":row["personId"]}
      elif query_num == 8:
        seed = {"personId":row["personId"]}
      elif query_num == 9:
        max_date = datetime.fromtimestamp(int(row["minDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"personId":row["personId"], "maxDate":max_date}
      elif query_num == 10:
        month = int(row["month"])
        next_month = (month + 1) if month < 12 else 1
        seed = {"personId":row["personId"], "month":month, "nextMonth":next_month}
      elif query_num == 11:
        seed = {"personId":row["personId"], "countryName":row["countryName"], "workFromYear":row["workFromYear"]}
      elif query_num == 12:
        seed = {"personId":row["personId"], "tagClassName":row["tagClassName"]}
      elif query_num == 13:
        seed = {"person1Id":row["person1Id"], "person2Id":row["person2Id"]}
      elif query_num == 14:
        seed = {"person1Id":row["person1Id"], "person2Id":row["person2Id"]}

      seeds.append(seed)
      count += 1
      if count >= max_num_seeds:
        break
  urls = []
  for seed in seeds:
    url = url_concat(ENDPOINT_URL_PREFIX + "ic_{}".format(query_num), seed)
    urls.append(url)
  return urls

def bi_queries(path_to_seeds, max_num_seeds, query_num):
  with open(path_to_seeds + "bi_{}_param.txt".format(query_num), "r") as f:
    reader = DictReader(f, delimiter="|")
    seeds = []
    count = 0
    for row in reader:
      if query_num == 1:
        date = datetime.fromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"date":date}
      elif query_num == 2:
        date1 = datetime.fromtimestamp(int(row["date1"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        date2 = datetime.fromtimestamp(int(row["date2"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"date1":date1, "date2":date2, "country1":row["country1"], "country2":row["country2"]}
      elif query_num == 3:
        seed = {"year":row["year"], "month":row["month"]}
      elif query_num == 4:
        seed = {"tagClass":row["tagClass"], "country":row["country"]}
      elif query_num == 5:
        seed = {"country":row["country"]}
      elif query_num == 6:
        seed = {"tag":row["tag"]}
      elif query_num == 7:
        seed = {"tag":row["tag"]}
      elif query_num == 8:
        seed = {"tag":row["tag"]}
      elif query_num == 9:
        seed = {"tagClass1":row["tagClass1"], "tagClass2":row["tagClass2"], "threshold":row["threshold"]}
      elif query_num == 10:
        date = datetime.fromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"tgtTag":row["tag"], "date":date}
      elif query_num == 11:
        seed = {"country":row["country"], "blacklist":row["blacklist"].split(";")}
      elif query_num == 12:
        date = datetime.fromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"date":date, "likeThreshold":row["likeThreshold"]}
      elif query_num == 13:
        seed = {"tgtCountry":row["country"]}
      elif query_num == 14:
        start_date = datetime.fromtimestamp(int(row["startDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.fromtimestamp(int(row["endDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"startDate":start_date, "endDate":end_date}
      elif query_num == 15:
        seed = {"country":row["country"]}
      elif query_num == 16:
        seed = {"personId":row["person"], "tgtCountry":row["country"], "tgtTagClass":row["tagClass"], "minPathDistance":row["minPathDistance"], "maxPathDistance":row["maxPathDistance"]}
      elif query_num == 17:
        seed = {"country":row["country"]}
      elif query_num == 18:
        date = datetime.fromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"date":date, "lengthThreshold":row["lengthThreshold"], "languages":row["languages"].split(";")}
      elif query_num == 19:
        date = datetime.fromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"date":date, "tagClass1":row["tagClass1"], "tagClass2":row["tagClass2"]}
      elif query_num == 20:
        seed = {"tagClasses":row["tagClasses"]}
      elif query_num == 21:
        end_date = datetime.fromtimestamp(int(row["endDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"tgtCountry":row["country"], "endDate":end_date}
      elif query_num == 22:
        seed = {"country1":row["country1"], "country2":row["country2"]}
      elif query_num == 23:
        seed = {"country":row["country"]}
      elif query_num == 24:
        seed = {"tagClass":row["tagClass"]}
      elif query_num == 25:
        start_date = datetime.fromtimestamp(int(row["startDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.fromtimestamp(int(row["endDate"])/1000).strftime('%Y-%m-%d %H:%M:%S')
        seed = {"person1Id":row["person1Id"], "person2Id":row["person2Id"], "startDate":start_date, "endDate":end_date}

      seeds.append(seed)
      count += 1
      if count >= max_num_seeds:
        break
  urls = []
  for seed in seeds:
    url = ENDPOINT_URL_PREFIX + "bi_{}?".format(query_num)
    args = ""
    for key, value in seed.items():
      if not type(value) is list:
        args += "{}={}&".format(key, value)
      else:
        for v in value:
          args += "{}={}&".format(key, v)
    url += args[:-1]
    urls.append(url)
  return urls