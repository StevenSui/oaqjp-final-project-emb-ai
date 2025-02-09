from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the response
    emotion_response = emotion_detector(text_to_analyze)
    
    # Format the output
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_response['anger']}, "
        f"'disgust': {emotion_response['disgust']}, "
        f"'fear': {emotion_response['fear']}, "
        f"'joy': {emotion_response['joy']} and "
        f"'sadness': {emotion_response['sadness']}. "
        f"The dominant emotion is {emotion_response['dominant_emotion']}."
    )
    return formatted_output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)