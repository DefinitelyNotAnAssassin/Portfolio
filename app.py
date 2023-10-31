from flask import * 


app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():

    return render_template(f'{request.args["id"]}.html')



if __name__ == '__main__':
    app.run(debug = True)