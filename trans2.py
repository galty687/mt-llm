import requests

def translate_text_with_api_key(text, target_language):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': text,
        'target': target_language,
        'key': 'AIzaSyBqPMziyFdXzb4NuafTSFS2fRxjFik4K6k'  # Replace with your actual API key
    }
    response = requests.post(url, params=params)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    translation = response.json()
    # Extract the translated text
    translated_text = translation.get('data', {}).get('translations', [{}])[0].get('translatedText', '')
    return translated_text

print(translate_text_with_api_key("Hello, world!", "zh-CN"))
