from flask import Flask, request,render_template
import json
import bcp

api = Flask(__name__)


@api.route('/predict', methods=['GET'])
def generateImage():
    input = []
    for i in range(1,49):
        input.append(float(request.args.get('p'+str(i))))
    result = {'predict': []}
    check = bcp.predict(input)
    if check == 1:
        return json.dumps({'predict': 'yes.'})
    else:
        return json.dumps({'predict': 'no.'})

@api.route("/")
def home_view():
    return render_template('index.html', title='Welcome')



if __name__ == '__main__':
    api.run()
