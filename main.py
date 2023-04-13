from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)


def formula(a, b, c):
    result = "$"
    if a == 1:
        result += "x^2"
    elif a != 0:
        result += f"{a:g}x^2"

    if b == 1:
        result += "x"
    elif b != 0:
        result += f"{b:+g}x"

    if c != 0:
        result += f"{c:+g}"

    result += "=0$"
    return result



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

        if A == 0:
            return render_template('error.html',
                                   formula=formula(A, B, C),
                                   error="Данное уравнение не является квадратным.")

        D = B ** 2 - 4 * A * C
        if D < 0:
            return render_template('error.html',
                                   formula=formula(A, B, C),
                                   error=f"Дискриминант уравнения равен ${D}$. Уравнение не имеет действительных корней.")
        elif D == 0:
            X = -B / 2 / A
            return render_template('answer.html',
                                   formula=formula(A, B, C),
                                   x1=f"$x = {X}$")
        else:
            X1 = (-B + sqrt(D)) / 2 / A
            X2 = (-B - sqrt(D)) / 2 / A
            return render_template('answer.html',
                                   formula=formula(A, B, C),
                                   x1=f"$x_1 = {X1}$",
                                   x2=f"$x_2 = {X2}$")


if __name__ == "__main__":
    app.run()
