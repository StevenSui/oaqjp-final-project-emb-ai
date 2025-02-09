# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting required set of emotions from the response
    anger_score = formatted_response['emotionPredictions']['emotion']['anger']
    disgust = formatted_response['emotionPredictions']['disgust']
    fear = formatted_response['emotionPredictions']['fear']
    joy = formatted_response['emotionPredictions']['joy']
    sadness = formatted_response['emotionPredictions']['sadness']
    

    # Return the response text from the API
    return response.text