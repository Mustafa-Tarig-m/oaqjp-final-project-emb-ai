from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection API")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze", "")
   
    analysis_result = emotion_detector(text_to_analyze)
    anger_score = analysis_result.get("anger", 0.0)
    disgust_score = analysis_result.get("disgust", 0.0)
    fear_score = analysis_result.get("fear", 0.0)
    joy_score = analysis_result.get("joy", 0.0)
    sadness_score = analysis_result.get("sadness", 0.0)
    dominant_emotion = analysis_result.get("dominant_emotion", "")
    
    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)