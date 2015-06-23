from flask import Flask, request, redirect, url_for, json, Response
from google.appengine.ext import ndb
from model import Menu

app = Flask(__name__)
app.config['DEBUG'] = True

# Menu CRUD
@app.route('/api/menu', methods=["POST"])
def create():
    data = request.get_json(force=True)
    menu = Menu(name=data['name'], address="", items=[])
    key = menu.put()

    return redirect(url_for('get', menu_id=key.id()))

@app.route('/api/menu', methods=["GET"])
def query():
    menus = Menu.query()

    rt = []
    for menu in menus.fetch():
        rt.append(menu.to_dict())

    return Response(json.dumps(rt),  mimetype='application/json')

@app.route('/api/menu/<menu_id>', methods=["GET"])
def get(menu_id):
    key = ndb.Key('Menu', int(menu_id))
    menu = key.get()

    return json.jsonify(menu.to_dict())

@app.route('/api/menu/<menu_id>', methods=["PATCH"])
def patch(menu_id):
    key = ndb.Key('Menu', int(menu_id))
    data = request.get_json(force=True)
    menu = key.get()
    menu.update_from_dict(data)
    menu.put()

    return ""

@app.route('/api/menu/<menu_id>', methods=["DELETE"])
def delete(menu_id):
    key = ndb.Key('Menu', int(menu_id))
    key.delete()

    return ""

