from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Matrix Multiplication</h2>
        <form action="/multiply" method="post">
            Matrix A (2x2, comma separated rows):<br>
            <input name="a1"><br>
            <input name="a2"><br><br>
            Matrix B (2x2, comma separated rows):<br>
            <input name="b1"><br>
            <input name="b2"><br><br>
            <input type="submit" value="Multiply">
        </form>
    '''

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Get matrix rows
        a1 = list(map(int, request.form['a1'].split(',')))
        a2 = list(map(int, request.form['a2'].split(',')))
        b1 = list(map(int, request.form['b1'].split(',')))
        b2 = list(map(int, request.form['b2'].split(',')))

        # Create matrices
        A = [a1, a2]
        B = [b1, b2]

        # Multiply A × B
        result = [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

        return f"<h3>Result:</h3><p>{result[0]}<br>{result[1]}</p>"

    except:
        return "Invalid input. Please enter rows as comma-separated integers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
