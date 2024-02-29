import requests
from flask import Flask, render_template, request

API_KEY = 'XXXX'  # Replace 'XXXX' with actual API key from Merriam-Webster

app = Flask(__name__)

def get_definition(word):
    # Construct the URL for the Merriam-Webster Dictionary API
    url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}'
    # Send GET request to the API
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Check if the data is a list (multiple entries for the word)
        if isinstance(data, list):
            # Iterate over each entry in the list
            for entry in data:
                # Check if the entry contains 'meta' and 'id' keys
                if 'meta' in entry and 'id' in entry['meta']:
                    # Return the word ID and its short definition
                    return entry['meta']['id'], entry['shortdef'][0] if 'shortdef' in entry else 'Definition not found'
            # If no matching entry is found, return None and 'Word not found' error message
            return None, 'Word not found'
        else:
            # If the data is not a list, return None and 'Word not found' error message
            return None, 'Word not found'
    else:
        # If the request was not successful, return None and 'Error fetching definition' error message
        return None, 'Error fetching definition'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the word entered by the user from the form
        word = request.form['word']
        # Get the definition of the word from the Merriam-Webster API
        word_id, definition = get_definition(word)
        if word_id:
            # If a definition is found, render the result template with the word ID and definition
            return render_template('result.html', word_id=word_id, word=word, definition=definition)
        else:
            # If no definition is found, render the result template with an error message
            return render_template('result.html', error=definition)
    # If the request method is GET, render the index template
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(debug=True)
    # Run the Flask application on host '0.0.0.0' and port 5000
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('SERVE_PORT', 5000)))
