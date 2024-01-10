import requests

url = "https://translation.googleapis.com/language/translate/v2"

data = {
    'q': 'hello world',
    'target': 'es',
    'key': 'AIzaSyBqPMziyFdXzb4NuafTSFS2fRxjFik4K6k'
}

response = requests.post(url, data=data)

print(response)

translation= response.json()

print(translation)

print(type(translation))