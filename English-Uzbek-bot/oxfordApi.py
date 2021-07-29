import requests

from pprint import pprint as print

app_id = "bd871f25"
app_key = "13e7c3b5b8a931a104aa7a82041c8b2d"
language = "en-gb"
word_id = "earth"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'))
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][2]['definitions'])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][3]['definitions'])

# def getDefinitions(word_id):
# 	url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
# 	r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# 	res = r.json()
# 	if 'error' in res.keys():
# 		return False
#
# 	output = {}
# 	senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
# 	definitions = []
# 	for sense in senses:
# 		definitions.append(f"👉 {sense['definitions'][0]}")
# 	output['definitions'] = "\n".join(definitions)
#
# 	if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
# 		output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
#
# 	return output
#
#
# if __name__ == '__main__':
# 	from pprint import pprint as print
#
# 	print(getDefinitions('Great Britain'))
# 	print(getDefinitions('sdsdsdsds'))
