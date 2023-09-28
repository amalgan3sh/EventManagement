from flask import *
from database import *
import uuid

customer=Blueprint('customer',__name__)


@customer.route('/customer_home')
def customer_home():
	return render_template('customer_home.html')


@customer.route('/customer_manage_project',methods=['get','post'])
def customer_manage_project():
	data={}
	q="SELECT * FROM `project` inner join subcategory using(subcategory_id) WHERE `customer_id`='%s'"%(session['customer_id'])
	data['project']=select(q)
	return render_template('customer_manage_project.html',data=data)

@customer.route('/customer_view_proposal')
def customer_view_proposal():
	data={}
	pid=request.args['pid']
	data['pid']=pid
	q="SELECT * FROM `proposal` WHERE `project_id`='%s'"%(pid)
	data['proposal']=select(q)


	if 'action' in request.args:
		action=request.args['action']
		prp_id=request.args['prp_id']
	else:
		action=None
	if action=='accept':
		q="update proposal set status='accept' where proposal_id='%s'"%(prp_id)
		update(q)
		flash('proposal has been accepted...')
		return redirect(url_for('customer.customer_view_proposal',pid=pid))

	return render_template('customer_view_proposal.html',data=data)
@customer.route('/customer_view_assigned_staff')
def customer_view_assigned_staff():
	data={}
	pid=request.args['pid']
	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `assignproject` INNER JOIN `staff` USING(`staff_id`) WHERE `project_id`='%s'"%(pid)
	data['staff']=select(q)
	return render_template('customer_view_assigned_staff.html',data=data)

@customer.route('/customer_view_work_status')
def customer_view_work_status():
	data={}
	pid=request.args['pid']
	q="SELECT *,CONCAT(`first_name`,' ',`lastname`) AS `name` FROM `assignproject` INNER JOIN `staff` USING(`staff_id`) WHERE `project_id`='%s'"%(pid)
	data['status']=select(q)
	return render_template('customer_view_work_status.html',data=data)
@customer.route('/customer_rate_project')
def customer_rate_project():

	return render_template('customer_rate_project.html')

@customer.route('/customer_interact_with_staff',methods=['get','post'])
def customer_interact_with_staff():
	data={}
	sid=request.args['sid']
	cid=session['customer_id']
	q="SELECT * FROM `messages` WHERE (`sender_id`='%s' AND `reciever_id`='%s' AND `sendertype`='customer') OR (`sender_id`='%s' AND `reciever_id`='%s' AND `sendertype`='customer')"%(cid,sid,sid,cid)
	data['chat']=select(q)
	if 'submit' in request.form:
		message=request.form['message']
		q="INSERT INTO `messages`(`sender_id`,`reciever_id`,`message`,`message_date`,`sendertype`)VALUES('%s','%s','%s',CURDATE(),'customer')"%(cid,sid,message)
		insert(q)
		return redirect(url_for('customer.customer_interact_with_staff',sid=sid))

	return render_template('/customer_interact_with_staff.html',data=data)
@customer.route('/customer_report_staff',methods=['get','post'])
def customer_report_staff():
	data={}
	sid=request.args['sid']
	pid=request.args['pid']
	cid=session['customer_id']

	if 'submit' in request.form:
		reason=request.form['reason']
		q="INSERT INTO `reported`(`reported_by_id`,`reported_whom_id`,`reported_date`,`reason`,`reported_status`) VALUES('%s','%s',curdate(),'%s','reported')"%(cid,sid,reason)
		insert(q)
		flash('success...')
		return redirect(url_for('customer.customer_view_assigned_staff',sid=sid,pid=pid))

	return render_template('customer_report_staff.html',data=data)
	
@customer.route('/customer_view_quotation',methods=['get','post'])
def customer_view_quotation():
	data={}
	pid=request.args['pid']
	q="SELECT * FROM `quotation` WHERE `project_id`='%s'"%(pid)
	data['quotation']=select(q)
	return render_template('customer_view_quotation.html',data=data)


@customer.route('/customer_make_payment',methods=['get','post'])
def customer_make_payment():
	data={}
	pid=request.args['pid']
	amount=request.args['amount']
	data['amount']=amount
	if 'pay' in request.form:
		amount=request.form['amount']
		q="INSERT INTO `quotation_deposit`(`project_id`,`amount`,`deposit_date`,`deposit_status`) VALUES('%s','%s',curdate(),'paid')"%(pid,amount)
		insert(q)
		flash('Payment Successfull...')

	return render_template('customer_make_payment.html',data=data)

