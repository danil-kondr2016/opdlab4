from flask import Flask, render_template, request
from quadratic import formula, solve_quadratic

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

        if A == 0:
            return render_template('error.html',
                                   formula=formula(A, B, C),
                                   error="Данное уравнение не является квадратным.")

        D, X1, X2 = solve_quadratic(A, B, C)

        if D < 0:
            return render_template('error.html',
                                   formula=formula(A, B, C),
                                   error=f"Дискриминант уравнения равен ${D}$. Уравнение не имеет действительных корней.")
        elif D == 0:
            return render_template('answer.html',
                                   formula=formula(A, B, C),
                                   x1=f"$x = {X1}$")
        else:
            return render_template('answer.html',
                                   formula=formula(A, B, C),
                                   x1=f"$x_1 = {X1}$",
                                   x2=f"$x_2 = {X2}$")


if __name__ == "__main__":
    app.run()
