from flask import Flask, jsonify, request
from flask_cors import CORS
from .types import InteractiveRssType, InteractiveFunctionType


class Server:
    def __init__(self, interactive_function: InteractiveFunctionType):
        self.app = Flask(__name__)

        CORS(self.app)

        @self.app.route('/')
        def index():
            return "Hello, World!"

        @self.app.route('/model', methods=['POST'])
        def model():
            rss = request.get_json()
            # print(rss)
            rss_modeled = InteractiveRssType(
                "", rss['paragraphs'])

            res = interactive_function(rss_modeled)
            return jsonify([block.__dict__ for block in res])

        @self.app.route('/submit', methods=['POST'])
        def submit():
            return {
                "success": True
            }

    def run(self):
        self.app.run(debug=True)
