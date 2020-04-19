# import os
# import tempfile
#
# import pytest
#
# from project import app
#
#
# @pytest.fixture
# def client():
#     # db_fd, app.config['DATABASE'] = tempfile.mkstemp()
#     app.config['TESTING'] = True
#
#     # with app.test_client() as client:
#     #     with app.app_context():
#     #         # init_db()
#     #     yield client
#
#     # os.close(db_fd)
#     # os.unlink(app.config['DATABASE'])
#
#
# def test_healthcheck(client):
#     rv = client.get('/healthcheck')
#     assert rv.get_json()['status'] == 'OK'


from flask import json, jsonify

app = flask.Flask(__name__)



@app.route('/healthcheck')
def healthcheck():
    return jsonify(status=g.status)

with user_set(app, my_user):
    with app.test_client() as c:
        resp = c.get('/users/me')
        data = json.loads(resp.data)
        self.assert_equal(data['username'], my_user.username)











#
# with app.test_request_context('/healthcheck'):
#     assert flask.request.path == '/'
#     assert flask.request.args['status'] == 'OK'
