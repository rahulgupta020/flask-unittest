from flask import Flask, request
app=Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    print("add_numbers")
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1+num2
    return {"Addition": result}

if __name__=="__main__":
    app.run(debug=True)