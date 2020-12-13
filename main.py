import json
from flask import Flask,render_template,request,jsonify,redirect,url_for,make_response
from flask_sqlalchemy import SQLAlchemy 
import razorpay

app= Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payment.db'

class ProcessPayment(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	amount = db.Column(db.Integer,nullable=False)

@app.route('/', methods=['GET','POST'])
def hello():
	if request.method == "POST":
		
		amount = request.form.get('amount')
		user = ProcessPayment(email=email , name =name , amount =amount)

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('pay' , id=user.id))

	return render_template('index.html')

@app.route('/pay/<id>',methods=['GET','POST'])
def pay(id):
	user = ProcessPayment.query.filter_by(id = id).first()
	client = razorpay.Client(auth =("rzp_test_octynudc0TmyFy","QaFDnthl7eTVoXGGXlzVgcuR") )
	payment = client.order.create({'amount':(int(user.amount)*100),'currency':'EUR','payment_capture':'1'})
	return render_template('pay.html',payment = payment)	

@app.route('/success',methods=['GET','POST'])
def success():
	return render_template('success.html')

if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.run()
	FLASK_APP = main.py 