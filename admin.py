from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_categories',methods=['get','post'])
def admin_manage_categories():
	data={}
	q="SELECT * FROM  `categories`"
	data['cat']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='update':
		q="SELECT * FROM `categories` WHERE `category_id`='%s'"%(cid)
		data['updatess']=select(q)

	if action=='delete':
		q="delete from categories where category_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('admin.admin_manage_categories'))

	if 'submit' in request.form:
		cname=request.form['cname']
		desc=request.form['desc']
		q="INSERT INTO `categories`(`category_name`,`category_description`)VALUES('%s','%s')"%(cname,desc)
		insert(q)
		flash('sucess...')
		return redirect(url_for('admin.admin_manage_categories'))
	if 'submits' in request.form:
		cname=request.form['cname']
		desc=request.form['desc']
		q="update `categories` set `category_name`='%s',`category_description`='%s' where  category_id='%s'"%(cname,desc,cid)
		update(q)
		flash('sucessfully updated...')
		return redirect(url_for('admin.admin_manage_categories'))

	return render_template('admin_manage_categories.html',data=data)

@admin.route('/admin_manage_subcategory',methods=['get','post'])
def admin_manage_subcategory():
	data={}
	q="select * from categories"
	data['cat']=select(q)

	q="SELECT * FROM  `subcategory` INNER JOIN `categories` USING(`category_id`)"
	data['subcat']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if action=='update':
		q="SELECT * FROM `subcategory` INNER JOIN `categories` USING(`category_id`) WHERE `subcategory_id`='%s'"%(sid)
		data['updatess']=select(q)
		print(q)
	if action=='delete':
		q="delete from subcategory where subcategory_id='%s'"%(sid)
		delete(q)
		flash('removed...')
		return redirect(url_for('admin.admin_manage_subcategory'))

	if 'submits' in request.form:
		cat=request.form['cat']
		sub=request.form['sub']
		q="update `subcategory` set `category_id`='%s',`subcategory`='%s'"%(cat,sub)
		update(q)
		flash('successfully updated...')
		return redirect(url_for('admin.admin_manage_subcategory'))

	if 'submit' in request.form:
		cat=request.form['cat']
		sub=request.form['sub']
		q="INSERT INTO `subcategory`(`category_id`,`subcategory`)VALUES('%s','%s')"%(cat,sub)
		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_manage_subcategory'))
	return render_template('admin_manage_subcategory.html',data=data)

@admin.route('/admin_manage_service',methods=['get','post'])
def admin_manage_service():
	data={}
	q="select * from service"
	data['service']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None

	if action=='update':
		q="select * from service where service_id='%s'"%(sid)
		data['updatess']=select(q)
	if action=='delete':
		q="delete from service where service_id='%s'"%(sid)
		delete(q)
		flash('removed...')
		return redirect(url_for('admin.admin_manage_service'))

	if 'submit' in request.form:
		service=request.form['service']
		q="insert into service(service) values('%s')"%(service)
		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_manage_service'))
	if 'submits' in request.form:
		service=request.form['service']
		q="update service set service='%s' where service_id='%s'"%(service,sid)
		update(q)
		flash('successfully updated...')
		return redirect(url_for('admin.admin_manage_service'))


	return render_template('admin_manage_service.html',data=data)

@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `staff`"
	data['staff']=select(q)

	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	sid=request.args['sid']
	# else:
	# 	action=None
	# if action=='update':
	# 	q="SELECT * FROM `staff` where staff_id='%s'"%(sid)
	# 	data['updatess']=select(q)
	# if action=='delete':
	# 	q="delete from staff where staff_id='%s'"%(sid)
	# 	delete(q)
	# 	flash('removed...')
	# 	return redirect(url_for('admin.admin_manage_staff'))

	# if 'submits' in request.form:
	# 	fname=request.form['fname']
	# 	lname=request.form['lname']
	# 	hname=request.form['hname']
	# 	place=request.form['place']
	# 	pin=request.form['pin']
	# 	phone=request.form['phone']
	# 	email=request.form['email']
	# 	image=request.files['image']
	# 	path="static/uploads/"+str(uuid.uuid4())+image.filename
	# 	image.save(path)
	# 	q="update `staff` set `first_name`='%s',`lastname`='%s',`house_name`='%s',`place`='%s',`pincode`='%s',`phone`='%s',`email`='%s',photo='%s' where staff_id='%s'"%(fname,lname,hname,place,pin,phone,email,path,sid)
	# 	update(q)
	# 	flash('successfully updated...')
	# 	return redirect(url_for('admin.admin_manage_staff'))

	# if 'submit' in request.form:
	# 	fname=request.form['fname']
	# 	lname=request.form['lname']
	# 	hname=request.form['hname']
	# 	place=request.form['place']
	# 	pin=request.form['pin']
	# 	phone=request.form['phone']
	# 	email=request.form['email']
	# 	image=request.files['image']
	# 	path="static/uploads/"+str(uuid.uuid4())+image.filename
	# 	image.save(path)

	# 	uname=request.form['uname']
	# 	pwd=request.form['pwd']
	# 	q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES('%s','%s','%s')"
	# 	login_id=insert(q)
	# 	q="INSERT INTO `staff`(`login_id`,`first_name`,`lastname`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(login_id,fname,lname,hname,place,pin,phone,email,path)
	# 	insert(q)
	# 	flash('success...')
	# 	return redirect(url_for('admin.admin_manage_staff'))
	return render_template('admin_manage_staff.html',data=data)

@admin.route('/admin_assign_service',methods=['get','post'])
def admin_assign_service():
	sid=request.args['sid']
	data={}
	data['sid']=sid

	
	q="SELECT * FROM `service`"
	data['service']=select(q)

	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `assign_staff_service` INNER JOIN `service` USING(`service_id`) INNER JOIN `staff` USING(`staff_id`)"
	data['assign']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
	else:
		action=None
	if action=='update':
		q="SELECT * FROM `assign_staff_service` INNER JOIN `service` USING(`service_id`) WHERE `assign_service_id`='%s'"%(aid)
		data['updatess']=select(q)

	if action=='delete':
		q="delete from assign_staff_service where assign_service_id='%s'"%(aid)
		delete(q)
		flash('removed...')
		return redirect(url_for('admin.admin_assign_service',sid=sid))

	if 'submit' in request.form:
		service=request.form['service']
		# q="SELECT * FROM `assign_staff_service` WHERE staff_id='%s'"%(sid)
		# res=select(q)
		# if res:
		# 	flash('already assigned...')
		# else:

			
		q="INSERT INTO `assign_staff_service`(`service_id`,`staff_id`) VALUES('%s','%s')"%(service,sid)
		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_assign_service',sid=sid))

	if 'submits' in request.form:
		service=request.form['service']
		q="update `assign_staff_service` set `service_id`='%s',`staff_id`='%s' where assign_service_id='%s'"%(service,sid,aid)
		update(q)
		flash('successfully updated...')
		return redirect(url_for('admin.admin_assign_service',sid=sid))
	

	return render_template('admin_assign_service.html',data=data)

@admin.route('/admin_manage_customers',methods=['get','post'])
def admin_manage_customers():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM customer"
	data['customers']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='update':
		q="SELECT * FROM `customer` WHERE `customer_id`='%s'"%(cid)
		data['updatess']=select(q)
	if action=='delete':
		q="delete from customer where customer_id='%s'"%(cid)
		delete(q)
		flash('removed...')
		return redirect(url_for('admin.admin_manage_customers'))

	if 'submits' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		email=request.form['email']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)
		

	
		q="update `customer` set `first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`house_name`='%s',`place`='%s',`pincode`='%s',`photo`='%s' where customer_id='%s'"%(fname,lname,phone,email,hname,place,pin,path,cid)
		update(q)
		flash('successfully updated...')
		return redirect(url_for('admin.admin_manage_customers'))

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		email=request.form['email']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)
		uname=request.form['email']
		pwd=request.form['pwd']

		q="INSERT INTO `login`(`username`,`password`,`usertype`)VALUES('%s','%s','customer')"%(uname,pwd)
		insert(q)
		q="INSERT INTO `customer`(username,`first_name`,`last_name`,`phone`,`email`,`house_name`,`place`,`pincode`,`photo`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,phone,email,hname,place,pin,path)
		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_manage_customers'))

	return render_template('admin_manage_customers.html',data=data)

@admin.route('/admin_view_projects',methods=['get','post'])
def admin_view_projects():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM `project` INNER JOIN `customer` USING(`customer_id`) INNER JOIN `subcategory` USING(`subcategory_id`)"
	data['project']=select(q)

	return render_template('admin_view_projects.html',data=data)


@admin.route('/admin_send_proposal',methods=['get','post'])
def admin_send_proposal():
	data={}
	pid=request.args['pid']
	pname=request.args['pname']
	data['pname']=pname

	q="SELECT * FROM `proposal` INNER JOIN `project` USING(`project_id`)"
	data['proposal']=select(q)

	if 'submit' in request.form:
		amount=request.form['amount']

		q="SELECT * FROM `proposal` WHERE `project_id`='%s'"%(pid)
		res=select(q)
		if res:
			flash('proposal already sent...')
		else:
			q="INSERT INTO `proposal`(`project_id`,`amount`,`date`,`status`) VALUES('%s','%s',curdate(),'pending')"%(pid,amount)
			insert(q)
			flash('success...')
			return redirect(url_for('admin.admin_send_proposal',pid=pid,pname=pname))
	return render_template('admin_send_proposal.html',data=data)

@admin.route('/admin_view_customer_details',methods=['get','post'])
def admin_view_customer_details():
	data={}
	cid=request.args['cid']
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name`FROM `customer` where customer_id='%s'"%(cid)
	data['customer']=select(q)

	return render_template('admin_view_customer_details.html',data=data)

@admin.route('/admin_set_quotation_deposit',methods=['get','post'])
def admin_set_quotation_deposit():
	data={}
	pid=request.args['pid']
	pname=request.args['pname']
	data['pname']=pname

	q="SELECT * FROM `quotation` INNER JOIN `project` USING(`project_id`)"
	data['deposit']=select(q)

	if 'submit' in request.form:
		amount=request.form['amount']

		q="SELECT * FROM `quotation` WHERE `project_id`='%s'"%(pid)
		res=select(q)
		if res:
			flash('quotation already set...')
		else:
			q="INSERT INTO `quotation`(`project_id`,`quotation`)VALUES('%s','%s')"%(pid,amount)
			insert(q)
			flash('Success...')
			return redirect(url_for('admin.admin_set_quotation_deposit',pid=pid,pname=pname))
	return render_template('admin_set_quotation_deposit.html',data=data)

@admin.route('/admin_assign_project_to_staff',methods=['get','post'])
def admin_assign_project_to_staff():
	data={}
	pid=request.args['pid']
	data['pid']=pid
	pname=request.args['pname']
	data['pname']=pname
	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `staff`"
	data['staff']=select(q)

	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `assignproject` INNER JOIN `project` USING(`project_id`) INNER JOIN `staff` USING(`staff_id`)"
	data['assign']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
	else:
		action=None
	if action=='delete':
		q="delete from assignproject where assignproject_id='%s'"%(aid)
		delete(q)
		return redirect(url_for('admin.admin_assign_project_to_staff',pid=pid,pname=pname))
	if action=='update':
		q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM assignproject  INNER JOIN staff USING(`staff_id`) WHERE assignproject_id='%s'"%(aid)
		data['updatess']=select(q)

	if 'submits' in request.form:
	
		staff=request.form['staff']
		q="update `assignproject` set `staff_id`='%s',`date`=curdate(),`status`='pending' where assignproject_id='%s'"%(staff,aid)
		update(q)
		flash('successfuly updated...')
		return redirect(url_for('admin.admin_assign_project_to_staff',pid=pid,pname=pname))



	if 'submit' in request.form:
	
		staff=request.form['staff']
		# q="select * from assignproject where project_id='%s'"%(pid)
		# res=select(q)
		# if res:
		# 	flash('alredy assigned...')
		# else:

		q="INSERT INTO `assignproject`(`project_id`,`staff_id`,`date`,`status`) VALUES('%s','%s',curdate(),'pending')"%(pid,staff)
		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_assign_project_to_staff',pid=pid,pname=pname))

	
	return render_template('admin_assign_project_to_staff.html',data=data)

@admin.route('/admin_view_work_updates')
def admin_view_work_updates():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name`,CONCAT(`assignproject`.`status`) AS `a_status`,CONCAT(`assignproject`.`date`) AS `a_date` FROM `assignproject` INNER JOIN `project` USING(`project_id`) INNER JOIN `staff` USING(`staff_id`)"
	data['work']=select(q)
	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=='confirm':
		q="UPDATE `project` SET `status`='confirm' WHERE `project_id`='%s'"%(pid)
		update(q)
		flash('status updated...')


	return render_template('admin_view_work_updates.html',data=data)


@admin.route('/admin_project_report',methods=['get','post'])
def admin_project_report():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM `project` INNER JOIN `customer` USING(`customer_id`) INNER JOIN `subcategory` USING(`subcategory_id`)"
	data['projectss']=select(q)
	if 'submit' in request.form:
		fdate=request.form['fdate']
		tdate=request.form['tdate']
		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM `project` INNER JOIN `customer` USING(`customer_id`) INNER JOIN `subcategory` USING(`subcategory_id`) WHERE `project`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
		res=select(q)
		if res:

			data['project']=select(q)
		else:
			flash('No results Found...!')
		return redirect(url_for('admin.admin_project_report'))
	

	return render_template('admin_project_report.html',data=data)


