import requests

class Translator:
	def __init__(self):
		self.url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
		self.language = {
			"target": "es",
			"source": "en"
		}
		self.headers = {
			"content-type": "application/x-www-form-urlencoded",
			"Accept-Encoding": "application/gzip",
			"X-RapidAPI-Key": "6740e4e7fdmsh66015f978d5a068p138505jsn80cefe6a66ec",
			"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
		}

	# Send connection test
	def detect_language(self, text):
		return requests.post(self.url+"/detect", text, self.headers).json()

	def set_target_language(self, lang):
		self.language["target"] = lang

	def set_source_language(self, lang):
		self.language["source"] = lang

	def translate(self, text):

		payload = {
			"q": text,
			"target": self.language.get("target"),
			"source": self.language.get("source")
		}

		return requests.post(self.url, data=payload, headers=self.headers).json()

	def get_languages(self):
		return requests.get(self.url+"/languages", headers=self.headers).json()

if __name__ == '__main__':
    print(Translator().check_connection())