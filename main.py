from flask import Flask
app = Flask('JaoshCoinServer')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'


@app.route('/', methods=['GET', 'POST'])
def add_message():
    print("vghj")


    content = request.json
    print(content)

    print(content['mytext'])
    return (content)

app.run(host='0.0.0.0', port=8080)
