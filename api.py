from flask import Flask
from flask_restful import Resource, Api
from catfeeder import feed

app = Flask(__name__)
api = Api(app)


class Feed(Resource):
    def post(self):
        try:
            feed()
            return {'success': True}
        except Exception as e:
            return {'failure': e}


class HealthCheck(Resource):
    def get(self):
        return {'status': 'OK'}


api.add_resource(HealthCheck, '/')
api.add_resource(Feed, '/feed')

if __name__ == '__main__':
    app.run(debug=True)
