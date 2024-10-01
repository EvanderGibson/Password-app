from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')


@app.route("/response")
def render_response():
    color = request.args['color']
    animal = request.args['animal']
    symbol = request.args['symbol']
    number = request.args['number']
   
    reply1 = animal + color + number + symbol
    
   
        
       
    return render_template('response.html', response = reply1)
    
@app.route("/response2")
def render_response2():
    color1 = request.args['color1']
    animal1 = request.args['animal1']
    symbol1 = request.args['symbol1']
    number1 = request.args['number1']
    city1 = request.args['city1']
    capital1 = request.args['capital1']
   
    reply2 =  color1 + animal1 + city1 + symbol1 + capital1 + number1
   
        
       
    return render_template('response.html', response = reply2)
    

if __name__=="__main__":
    app.run(debug=True)
    
    
    