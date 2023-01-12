from flask import *
from formulas.solve import *
    
app = Flask(__name__)

@app.route('/<expression>', methods=['GET'])
def calculate(expression):
    equation = split_equation(expression)
    return str(solve(equation))

if __name__ == "__main__":
    app.run(port=9999)