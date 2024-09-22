import requests

# Send POST request to the locally running Flask app
response = requests.post('http://127.0.0.1:5000/emotion-detect', json={'text': 'I love this new technology.'})

# Print the response
print(response.json())
