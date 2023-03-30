import requests
from flask_restful import Resource

# SECURITY_NODE_URL = "http://security-node:5000"
SECURITY_NODE_URL = "http://localhost:8000"
REGISTER_NODE_ENDPOINT = "/register-node"


class SecurityNodeResource(Resource):
    def post(self):
        req = requests.post(url=SECURITY_NODE_URL + REGISTER_NODE_ENDPOINT)
        return req.text, req.status_code
