from flask import * 


app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('terminal.html')




@app.route('/terminal')
def terminal():
   
    command =  request.args['terminal']
    back_log = f"$ {command}<br>"
    if  command == "-help" or command == '-h':
        return """
Commands Available: 
    <br>
    -help , -h      -   Produces the list of available commands
    <br>    

"""
    else:
        return f"{back_log}'{command}' is not recognized as an internal or external command, operable program or batch file. <br><br>"


@app.route('/hello')
def hello():

    return render_template(f'{request.args["id"]}.html')



if __name__ == '__main__':
    app.run(debug = True)