from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/answer', methods=['post', 'get'])
def form():
    if request.method == 'GET':
        return render_template('get.html')
    elif request.method == 'POST':
        A = float(request.form.get('coef_a'))
        B = float(request.form.get('coef_b'))
        C = float(request.form.get('coef_c'))

        D = B ** 2 - 4 * A * C
        if D < 0:
            return render_template('error.html',
                                   formula=f"{A}x<sup>2</sup> + {B}x + {C} = 0",
                                   error=f"Дискриминант уравнения равен {D}. Уравнение не имеет действительных корней.")
        else:
            X1 = (-B + sqrt(D)) / 2 / A
            X2 = (-B - sqrt(D)) / 2 / A
            return render_template('answer.html',
                                   formula=f"{A}x<sup>2</sup> + {B}x + {C} = 0",
                                   x1=X1, x2=X2)


if __name__ == "__main__":
    app.run()
