from flask import Flask, render_template, send_from_directory, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import boto3
import os

app = Flask(__name__, static_folder='client/build', static_url_path='')
cors = CORS(app)

@app.route('/api')
@cross_origin()
def Welcome():
    return "Welcome to the API!!!"
@app.route('/api/justpie/')
@cross_origin()

def GeneratePie():
    # Get the input data (Wedge is the distance between slices)
    data = [60,40]
    colors = ['#003049','#ffcdb2']
    wedge = 0.05
    # Make a matplotlib (high res) pie chart!
    fig1, ax1 = plt.subplots(figsize=(20,20))
    patches, texts = ax1.pie(data,explode=[float(wedge) for w in
       range(0,len(data))], colors = colors, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    # Save the image temporary on the local machine
    plt.savefig(os.getcwd() + '/test.png')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')