from flask import Flask, request, send_from_directory
import random
import json
import hashlib


app = Flask('JoshCoinServer', static_url_path='/static')


x = open('database.json', 'r')
z = x.read()
y = json.loads(z)
def generateHash():
  global realNum
  realNum = random.randrange(3, 99999)
  bytesRealNum = bytes(realNum)
  realHash = (hashlib.sha512(bytesRealNum).hexdigest())
  
  ff = open("static/targetHash.txt", 'w')
  
  ff.write(realHash)
  ff.close()

generateHash()
print(realNum)

@app.route('/targetHash')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route('/', methods=['POST'])
def result():
  action = (request.form['action'])
  print("Target hash requested")
  value = (request.form['value']) 
  name = (request.form['name'])
  print("Sgrgrgrgrgrgrggrgrgr")
    
  return 'Received !' # response to your request.


@app.route('/buy', methods=['POST'])
def buy():
  print("Item bought")
  value = (request.form['value']) 
  name = (request.form['name'])
  

  return 'Received !' # response to your request.


@app.route('/redeem', methods=['POST'])
def redeem():
  print("Redeeming JoshCoin")
  testNum = (request.form['number']) 
  name = (request.form['name'])
  global realNum

  testNum = str(testNum)
  realNum = str(realNum)
  print("testNum:", testNum)
  print(realNum)
  if testNum == realNum:
    global y
    amount = (y[(name)]["amount"])
    amount = amount+1
    y.update()
    
    (y[name]["amount"]) = (y[name]["amount"])+1
    print(json.dumps(y))
    
    
    a_file = open("database.json", "w")
    json.dump(y, a_file)
    a_file.close()

    generateHash()
  else:
    print("Number incorrect")

    
  

  return 'Received !' # response to your request.





#https://www.geeksforgeeks.org/machine-learning/?ref=shm
























app.run(host='0.0.0.0', port=8080)
