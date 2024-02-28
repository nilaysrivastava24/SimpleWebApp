from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import os
import identity
import identity.web
from werkzeug.middleware.proxy_fix import ProxyFix

CLIENT_ID = "c7320191-085c-4393-973b-80735077908a"
CLIENT_SECRET = "c5ff174f-d524-4eec-b8c7-f1eb620e2d9e"
os.environ["TENANT_ID"] = "0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
AUTHORITY = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID', 'common')}"

app = Flask(__name__)
Session(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

auth = identity.web.Auth(
    session=session,
    authority=AUTHORITY,
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
