from flask import *
from database import *


staff=Blueprint('staff',__name__)


@staff.route('/staff_home')
def staff_home():
	return render_template('staff_home.html')

@staff.route('/staff_profile')
def staff_profile():
    data = {}
    staff_id = session.get('staff_id')  # Get staff_id from the session

    if staff_id:
        q = "SELECT * FROM staff WHERE `staff_id`='%s'" % staff_id
        staff_data = select(q)

        if staff_data:
            data['staff'] = staff_data[0]  # Use [0] to access the first (and likely only) row
            return render_template('staff_profile.html', data=data)
        else:
            return render_template('error.html', error_message='Staff data not found')
    else:
        return render_template('error.html', error_message='Staff ID not available in session')


@staff.route('/staff_view_assigned_job')
def staff_view_assigned_job():
	data={}
	q="SELECT *,CONCAT(`assignproject`.`status`) AS `a_status`FROM `assignproject` INNER JOIN `project` USING(`project_id`) WHERE `staff_id`='%s'"%(session['staff_id'])
	data['assign']=select(q)

	return render_template('staff_view_assigned_job.html',data=data)

@staff.route('/staff_view_feedback')
def staff_view_feedback():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM feedback INNER JOIN customer USING (customer_id) WHERE `staff_id`='%s'"%(session['staff_id'])
	data['feedback']=select(q)

	return render_template('staff_view_feedback.html',data=data)

@staff.route('/staff_view_customer_details')
def staff_view_customer_details():
	data={}
	uname=session['username']
	cid=request.args['cid']
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM `customer` WHERE `customer_id`='%s'"%(cid)
	data['customer']=select(q)


	return render_template('staff_view_customer_details.html',data=data)

@staff.route('/staff_report_customer',methods=['get','post'])
def staff_report_customer():
	data={}
	cid=request.args['cid']
	sid=session['staff_id']

	if 'submit' in request.form:
		reason=request.form['reason']
		q="INSERT INTO `reported`(`reported_by_id`,`reported_whom_id`,`reported_date`,`reason`,`reported_status`) VALUES('%s','%s',curdate(),'%s','reported')"%(sid,cid,reason)
		insert(q)
		flash('success...')
		return redirect(url_for('staff.staff_view_customer_details',cid=cid))
	return render_template('staff_report_customer.html',data=data)

@staff.route('/saff_update_work_status',methods=['get','post'])
def saff_update_work_status():
	aid=request.args['aid']
	if 'submit' in request.form:
		status=request.form['status']
		q="UPDATE `assignproject` SET `status`='%s' WHERE `assignproject_id`='%s'"%(status,aid)
		update(q)
		flash('work status updated...')
		return redirect(url_for('staff.staff_view_assigned_job'))

	return render_template('saff_update_work_status.html')

@staff.route('/staff_interact_with_customer',methods=['get','post'])
def staff_interact_with_customer():
	data={}
	cid=request.args['cid']
	sid=session['staff_id']
	q="SELECT * FROM `messages` WHERE (`sender_id`='%s' AND `reciever_id`='%s' AND `sendertype`='staff') OR (`sender_id`='%s' AND `reciever_id`='%s' AND `sendertype`='customer')"%(sid,cid,cid,sid)
	data['chat']=select(q)
	if 'submit' in request.form:
		message=request.form['message']
		q="INSERT INTO `messages`(`sender_id`,`reciever_id`,`message`,`message_date`,`sendertype`)VALUES('%s','%s','%s',CURDATE(),'staff')"%(session['staff_id'],cid,message)
		insert(q)
		
		return redirect(url_for('staff.staff_interact_with_customer',cid=cid))
	return render_template('staff_interact_with_customer.html',data=data)