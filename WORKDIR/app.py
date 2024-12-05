from flask import Flask, render_template, jsonify

from markupsafe import escape

app = Flask(__name__)

IMAGES1 = ["/static/img1.png", "/static/img2.png"]
IMAGES2 = ["/static/img11.png", "/static/img22.png", "/static/img33.png", "/static/img44.png"]
IMAGES3 = ["/static/img111.png", "/static/img222.png"]
IMAGES4 = ["/static/img1111.png", "/static/img2222.png", "/static/img3333.png"]
IMAGES5 = ["/static/img11111.png", "/static/img22222.png"]
IMAGES6 = ["/static/img111111.png", "/static/img222222.png"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/torneo')
def about1():
    return render_template("torneo.html")

@app.route('/torneo2')
def about2():
    return render_template("torneo2.html")

@app.route('/api/image-set1', methods=['GET'])
def get_image_set1():
    return jsonify(IMAGES1)

@app.route('/api/image-set2', methods=['GET'])
def get_image_set2():
    return jsonify(IMAGES2)

@app.route('/api/image-set3', methods=['GET'])
def get_image_set3():
    return jsonify(IMAGES3)

@app.route('/api/image-set4', methods=['GET'])
def get_image_set4():
    return jsonify(IMAGES4)

@app.route('/api/image-set5', methods=['GET'])
def get_image_set5():
    return jsonify(IMAGES5)

@app.route('/api/image-set6', methods=['GET'])
def get_image_set6():
    return jsonify(IMAGES6)

app.run(host="0.0.0.0")

    
    
    
    
    