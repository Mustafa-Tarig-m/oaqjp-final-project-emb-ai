import flask, requests, json 

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=input_json)
    
    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion_score = 0.0
    dominant_emotion_name = ""
    for emotion, score in emotions.items():
        if score > dominant_emotion_score:
            dominant_emotion_score = score
            dominant_emotion_name = emotion

    emotions["dominant_emotion"] = dominant_emotion_name
    return emotions