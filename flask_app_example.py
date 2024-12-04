from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', template_folder='.')

# Маршрут для главной страницы
@app.route('/')
def home():
    return render_template('index.html')

# Пример маршрутов для других страниц
@app.route('/brand/')
def brand():
    return render_template('brand.html')

@app.route('/catalog/')
def catalog():
    return render_template('catalog_index.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/delivery-payment/')
def delivery_payment():
    return render_template('delivery_payment.html')

@app.route('/returns/')
def returns():
    return render_template('returns.html')

@app.route('/product_jaqnhas/')
def terms():
    return render_template('product_jaqnhas.html')




if __name__ == '__main__':
    app.run(debug=True)
