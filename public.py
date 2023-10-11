from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)


@public.route('/')
def main_home():
	return render_template('main_home.html')


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE(`username`='%s' AND `password`='%s')"%(uname,pwd)
		res=select(q)
		print(res)
		if res:
			session['username']=res[0]['username']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.admin_home'))

			if res[0]['usertype']=='staff':
				q="select * from staff where username='%s'"%(session['username'])
				res=select(q)
				session['staff_id']=res[0]['staff_id']
				return redirect(url_for('staff.staff_home'))
				
			if res[0]['usertype']=='customer':
				q="select * from customer where username='%s'"%(session['username'])
				res=select(q)
				session['customer_id']=res[0]['customer_id']
				return redirect(url_for('customer.customer_home'))
			
		else:
			flash('Access Denied...')
	return render_template('login.html')

@public.route('/staff_register',methods=['get','post'])
def staff_register():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)

		uname=request.form['email']
		pwd=request.form['pwd']
		q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES('%s','%s','staff')"%(uname,pwd)
		insert(q)
		q="INSERT INTO `staff`(`username`,`first_name`,`lastname`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,hname,place,pin,phone,email,path)
		insert(q)
		flash('success...')
		return redirect(url_for('public.login'))
	return render_template('staff_register.html')

@public.route('/public_customer_register',methods=['get','post'])
def public_customer_register():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)
		uname=request.form['email']
		pwd=request.form['pwd']
		q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES('%s','%s','customer')"%(uname,pwd)
		insert(q)
		q="INSERT INTO `customer`(`username`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,hname,place,pin,phone,email,path)
		insert(q)
		flash('success...')
		return redirect(url_for('public.login'))
	return render_template('public_customer_register.html')