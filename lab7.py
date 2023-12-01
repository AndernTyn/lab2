from flask import Blueprint, render_template, request, abort, jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7')
def main():
    return render_template('lab7/index.html')

@lab7.route('/lab7/drink')
def drink():
    return render_template('lab7/drink.html')

@lab7.route('/lab7/api', methods=['POST'])
def api():
    data = request.json
    
    if data['method'] == 'get-price':
        return get_price(data['params'])
    elif data['method'] == 'pay':
        return pay(data['params'])
    
    abort(400)

def get_price(params):
    return {"result": calculate_price(params), "error": None}

def calculate_price(params):
    drink = params['drink']
    milk = params['milk']
    sugar = params['sugar']

    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if milk:
        price += 30
    if sugar:
        price += 10

    return price
    
def pay(params):
    drink = params.get('drink')
    milk = params.get('milk')
    sugar = params.get('sugar')
    card_num = params.get('card_num')
    cvv = params.get('cvv')

    # Добавьте проверки на корректность данных здесь

    obj = {
        "method": "pay",
        "params": {
            "drink": drink,
            "milk": milk,
            "sugar": sugar,
            "card_num": card_num,
            "cvv": cvv
        }
    }

    response = fetch_data('/lab7/api', obj)
    
    if response.get('result'):
        return jsonify({"result": f'С карты {card_num} списано {response["result"]} руб.'})
    else:
        return jsonify({"error": response.get('error', 'Произошла ошибка при обработке заказа')})

def fetch_data(url, data):
    response = fetch(url, data)
    return response.json() if response else {"error": "Произошла ошибка при отправке запроса"}

def fetch(url, data):
    return requests.post(url, json=data, headers={'Content-Type': 'application/json'})
