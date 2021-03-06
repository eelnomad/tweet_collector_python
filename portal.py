import json, time
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
import backend.mongo_utils as mongo
import backend.twitter_utils as twitter

app = Flask(__name__,
            static_folder="frontend/dist/",
            static_url_path="")
# CORS(app)
active_stream = None


@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def catch_all(e):
    return redirect('/')


@app.route('/api/list')
def list_collections():
    return json.dumps(mongo.get_collections()), 200, {'ContentType': 'application/json'}


@app.route('/api/run')
def run_collection():
    id = request.args.get('id')
    if id:
        global active_stream
        if active_stream:
            active_stream = None
            time.sleep(2)

        active_stream = twitter.TwitterStream(id)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False, 'message': 'Missing ID'}), 404, {'ContentType': 'application/json'}


@app.route('/api/stop')
def stop_collection():
    global active_stream
    active_stream = None
    time.sleep(2)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/new')
def create_collection():
    id, created = mongo.create_collection(request.args.getlist('keywords[]'), request.args.get('desc'))
    return json.dumps({'id': id, 'created': created}), 200, {'ContentType': 'application/json'}


@app.route('/api/delete')
def delete_collection():
    id = request.args.get('id')
    if id:
        result = mongo.delete_collection(id)
        time.sleep(2)

        return json.dumps({'success': result}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False, 'message': 'Missing ID'}), 404, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True)
