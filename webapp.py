# route definition for video upload for analysis
@app.route('/analyze/<filename>')

def analyze(filename):
   # invokes method analyse_video
   return Response(analyse_video(pose_detector, lstm_classifier, filename), mimetype='text/event-stream')
