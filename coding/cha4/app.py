from flask import Flask, jsonify, request
from repository import SqlAlchemyRepository
from model import Batch, OrderLine, allocate
from conftest import session_db, session_in_memory_db
from datetime import datetime

app = Flask(__name__)

#session_env = session_in_memory_db()
session_env = session_db()


@app.route('/add_batch', methods = ['POST'])
def add_batch():
    repo = SqlAlchemyRepository(session_env)
    # input example: {"ref": "20200615", "sku": "bed", "eta": "2021-03-09", "qty": 10}
    batch = Batch(ref = request.json['ref'], sku = request.json['sku'], 
                eta = datetime.strptime(request.json['eta'], "%Y-%m-%d"), qty = request.json['qty'])
    try:
        repo.add(batch)
    except Exception as e:
        return jsonify({"code": 400, "msg": str(e)})
    session_env.commit()
    return jsonify({"code": 200})

@app.route('/allocate', methods = ['POST'])
def allocate():
    repo = SqlAlchemyRepository(session_env)
    # input example: {"id": "324212", "sku": "bed", "qty": 5}
    line = OrderLine(orderid = request.json['id'], sku = request.json['sku'], qty = request.json['qty'])
    return jsonify(repo.list())
    """
    try:
        allocate(line, repo.list())
    except Exception as e:
        return jsonify({"code": 400, "msg": str(e)})
    return jsonify({"code": 200})
    """