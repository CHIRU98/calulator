from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route('/math',methods=['POST'])
def math_operation():
    if (request.method=="POST"):
        operation = request.form["operation"]
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if operation == 'add':
            r = num1+num2
            result = 'The sum of '+str(num1) + 'and' + str(num2) +'is' + str(r)
        if operation == 'sub':
            r = num1 - num2
            result = 'The subtraction of '+str(num1) + 'and' + str(num2) +'is' + str(r)
        if operation == 'multi':
            r = num1 * num2
            result = 'The multiplication of '+str(num1) + 'and' + str(num2) +'is' + str(r)
        if (operation == 'division'):
            r = num1/num2
            result = 'The Division of '+str(num1) + 'and' + str(num2) +'is' + str(r)
        return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)


