from flask import *
from database import *
from flask import url_for
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


@customer.route('/customer_give_feedback', methods=['get', 'post'])
def customer_give_feedback():
    data = {}
    q = "SELECT * FROM `feedback`"
    data['feedback'] = select(q)

    cid=session['customer_id']
    if 'submit' in request.form:
        ftitle = request.form['ftitle']
        q = "INSERT INTO `feedback`(`feedback_description`,`datetime`,`customer_id`) VALUES ('%s', CURDATE(),'%s')" % (ftitle,cid)
        insert(q)
        flash('Successfully inserted feedback...')
        return redirect(url_for('customer.customer_give_feedback'))


    return render_template('customer_give_feedback.html', data=data)

@customer.route('/customer/delete_feedback/<int:feedback_id>', methods=['GET'])
def delete_feedback(feedback_id):
    # Construct the SQL query to delete the feedback entry
    sql_query = "DELETE FROM feedback WHERE feedback_id = %s" % feedback_id

    # Execute the SQL query to delete the feedback entry
    delete(sql_query)  # Assuming that `delete` is a function to execute SQL queries

    # Flash a message to indicate successful deletion
    flash('Feedback deleted successfully')

    # Redirect back to the customer_give_feedback page
    return redirect(url_for('customer.customer_give_feedback'))

@customer.route('/customer_view_categories')
def customer_view_categories():
    data = {}
    q = "SELECT * FROM `subcategory`"
    data['categories'] = select(q)
    return render_template('customer_view_categories.html', data=data)

@customer.route('/customer_specify_requirments',methods=['get','post'])
def customer_specify_requirments():

    cid=session['customer_id']
    if 'submit' in request.form:
        subcategory_id = request.args['subcategory_id']
        venue = request.form['venue']
        date = request.form['date']
        days = request.form['days']
        budget = request.form['budget']
        other = request.form['other']
        q = "INSERT INTO `requirments`(`subcat_id`,`venue`,`date`,`days_required`,`budget`,`other`,`customer_id`)VALUE('%s','%s','%s','%s','%s','%s','%s')" % (subcategory_id,venue,date,days,budget,other,cid)
        insert(q)
        flash('Requirments added')
        return redirect(url_for('customer.customer_view_event_planners'))

    return render_template('customer_specify_requirments.html')

@customer.route('/customer_view_event_planners')
def customer_view_event_planners():
    data = {}
    q = "SELECT *,CONCAT(first_name,' ',lastname) staff_name FROM staff"
    data['event_planners'] = select(q)
    return render_template('customer_view_event_planners.html', data=data)

@customer.route('/customer_confirm_requirements')
def customer_confirm_requirements():
    data = {}
    q = "SELECT * FROM `requirments`"
    data['requirments'] = select(q)
    
    staff_id = request.args.get('staff_id')
    
    if 'action' in request.args:
        requirement_id = request.args.get('requirment_id')
        action = request.args.get('action')
    else:
        action = None

    if action == 'confirm':
        q = "INSERT INTO `assigned_event` (`requirment_id`, `staff_id`, `customer_id`) VALUES ('%s', '%s', '%s')"%(requirement_id,'1',session['customer_id'])
        insert(q)  # Assuming you have a function to insert data and use a tuple of values.
        
        flash('Event assigned to the staff', 'success')  # Display a success message

    return render_template('customer_confirm_requirments.html', data=data)

@customer.route('/customer_view_assigned_events')
def customer_view_assigned_events():
    data = {}
    q = "SELECT *,CONCAT(first_name,' ',lastname) AS event_planner FROM `assigned_event` INNER JOIN requirments USING(requirment_id) INNER JOIN staff USING(staff_id)"
    data['assigned_events'] = select(q)
    return render_template('customer_view_assigned_events.html', data=data)



