
import requests
import json



def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"  # URL of the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyse }}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    # response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # return response.text  # Return the response text from the API


    response = requests.post(url, json=myobj, headers=header)


    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    else:
        # Handle 400 or 500 errors
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


    
