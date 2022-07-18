import json
import ast

from filter import filter_data
from contoller import scrap

from flask import Flask, render_template,request, jsonify

app = Flask(__name__, template_folder='views')

scrap()
 
validate_auth={
  "is_autenticated":False
}


@app.route('/')
def template_login():
  return render_template('index.html')
    
@app.route('/', methods=['POST'])
def autenticate():
  with open("auth/auth.json") as auth_data:
    auth=json.load(auth_data)
    username=auth.get('username')
    password=auth.get('password')

  auth_user={
    "username":request.json['username'],
    "password":request.json['password']
  }

  if username == auth_user.get('username') and password == auth_user.get('password') :
     validate_auth.update(is_autenticated=True)
     return jsonify({"response":"ok"})
  else:
    validate_auth.update(is_autenticated=False)
    return jsonify({"response":"false"}) 


@app.route('/products')
def template_products():   

  if validate_auth.get('is_autenticated')==True:
    return render_template('products.html')
  else: 
    return "<div> <h1>Necesita autenticacion</h1><a href='/'>Ir a inicio de sesion</a></div>"


@app.route('/products/<string:param>/<string:filter_by>/<string:value>')
def get_products(param, filter_by,value):

  with open("data/data.json") as products_data:
   products=json.load(products_data)
  if validate_auth.get('is_autenticated')==True:
   
    if param=="listar":
        return jsonify(products) 

    elif param=="filtrar":
        list_data=filter_data(products,filter_by, value)
        return jsonify(list_data) 

    elif param == "ordenar":
        products.sort(key=lambda product:product.get(value))
        list_data=repr(products)
        output=ast.literal_eval(list_data)
        return jsonify(output )
  
  else: 
    return "<div> <h1>Necesita autenticacion</h1><a href='/'>Ir a inicio de sesion</a></div>"

  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
