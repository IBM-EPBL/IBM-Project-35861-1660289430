import http.client

conn = http.client.HTTPSConnection("real-time-news-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "29716e7ef6msh1b72b8d74762ee3p1cae99jsnc9896aed6b7e",
    'X-RapidAPI-Host': "real-time-news-data.p.rapidapi.com"
    }

conn.request("GET", "/top-headlines?country=IN&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))