import json
import requests
app_id  = "<my_app_id>"
app_key  = "<my_app_key>"
endpoint = "entries"
language_code = "en-us"
word_id = "example"
url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))