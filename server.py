from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initiate app
app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyser():
    # Retrieve the text to analyse from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    
    #extract the dominant emotion and then delete it from the response
    dom_emotion=response["dominant_emotion"]
    del response["dominant_emotion"]

    #format the response
    formatted_response = ", ".join(f"{k}: {v}" for k, v in response.items())

    #create the output
    return "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>.".format(formatted_response, dom_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
