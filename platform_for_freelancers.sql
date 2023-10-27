/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.10.2-MariaDB : Database - platform_for_freelancers
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`platform_for_freelancers` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;

USE `platform_for_freelancers`;

/*Table structure for table `assign_staff_service` */

DROP TABLE IF EXISTS `assign_staff_service`;

CREATE TABLE `assign_staff_service` (
  `assign_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assign_service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `assign_staff_service` */

/*Table structure for table `assigned_event` */

DROP TABLE IF EXISTS `assigned_event`;

CREATE TABLE `assigned_event` (
  `assigned_id` int(11) NOT NULL AUTO_INCREMENT,
  `requirment_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'pending',
  PRIMARY KEY (`assigned_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `assigned_event` */

insert  into `assigned_event`(`assigned_id`,`requirment_id`,`staff_id`,`customer_id`,`status`) values 
(1,1,1,1,'accepted'),
(2,2,1,1,'pending');

/*Table structure for table `assignproject` */

DROP TABLE IF EXISTS `assignproject`;

CREATE TABLE `assignproject` (
  `assignproject_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assignproject_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `assignproject` */

/*Table structure for table `categories` */

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `categories` */

insert  into `categories`(`category_id`,`category_name`,`category_description`) values 
(1,'Photography','Photography is the art, application, and practice of creating images by recording light'),
(2,'Graphic design','Graphic Designing is the most popular types of freelance job market dominated by freelance workers'),
(3,'Web development','Web development is the work involved in developing a website for the Internet or an intranet'),
(4,'Digital marketing','Digital marketing includes all marketing that use digital technologies'),
(5,'Accounting','Accounting, also known as accountancy, is the processing of information about economic entities');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`first_name`,`last_name`,`phone`,`email`,`house_name`,`place`,`pincode`,`photo`) values 
(1,'customer@gmail.com','rahul','ganesh','7894563256','customer@gmail.com','abc house','alappuzha','688001','static/uploads/b2454f46-6eea-49af-b53e-0199900797b9boy.jpg');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_title` varchar(50) DEFAULT NULL,
  `feedback_description` varchar(200) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `datetime` varbinary(20) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback_title`,`feedback_description`,`customer_id`,`datetime`) values 
(1,NULL,'Good',1,'2023-10-25');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values 
('admin','admin','admin'),
('staff@gmail.com','staff123','staff'),
('customer@gmail.com','customer123','customer'),
('musk@gmail.com','musk1234','staff');

/*Table structure for table `messages` */

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `reciever_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `message_date` varchar(100) DEFAULT NULL,
  `sendertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `messages` */

insert  into `messages`(`message_id`,`sender_id`,`reciever_id`,`message`,`message_date`,`sendertype`) values 
(1,1,1,'hi','2023-10-25','customer'),
(2,1,1,'hello','2023-10-25','customer'),
(3,1,1,'yes','2023-10-25','staff');

/*Table structure for table `project` */

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `subcategory_id` int(11) DEFAULT NULL,
  `projectname` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `project` */

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `proposal` */

/*Table structure for table `quotation` */

DROP TABLE IF EXISTS `quotation`;

CREATE TABLE `quotation` (
  `quotation_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `quotation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`quotation_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `quotation` */

/*Table structure for table `quotation_deposit` */

DROP TABLE IF EXISTS `quotation_deposit`;

CREATE TABLE `quotation_deposit` (
  `deposit_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `deposit_date` varchar(100) DEFAULT NULL,
  `deposit_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`deposit_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `quotation_deposit` */

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `freelancer_id` int(11) DEFAULT NULL,
  `hirer_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `rated_point` varchar(100) DEFAULT NULL,
  `rated_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `ratings` */

/*Table structure for table `reported` */

DROP TABLE IF EXISTS `reported`;

CREATE TABLE `reported` (
  `reported_id` int(11) NOT NULL AUTO_INCREMENT,
  `reported_by_id` int(11) DEFAULT NULL,
  `reported_whom_id` int(11) DEFAULT NULL,
  `reported_date` varchar(100) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `reported_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`reported_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `reported` */

/*Table structure for table `requirments` */

DROP TABLE IF EXISTS `requirments`;

CREATE TABLE `requirments` (
  `requirment_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcat_id` int(11) DEFAULT NULL,
  `venue` varchar(50) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `days_required` varchar(300) DEFAULT NULL,
  `budget` varchar(100) DEFAULT NULL,
  `other` varchar(200) DEFAULT NULL,
  `customer_id` int(200) DEFAULT NULL,
  PRIMARY KEY (`requirment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `requirments` */

insert  into `requirments`(`requirment_id`,`subcat_id`,`venue`,`date`,`days_required`,`budget`,`other`,`customer_id`) values 
(1,3,'Crown plaza','31/12/2023','30','1000000','DJ party',1),
(2,1,'Le Meridian','2023-10-20','1','50000','Concert',1);

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `service` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`first_name`,`lastname`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`) values 
(1,'staff@gmail.com','amal','ganesh','parambath house','kannur','670331','7356529545','staff@gmail.com','static/uploads/5dd030c1-136e-49be-9ef0-02abc1d78f72webdeveloper.png'),
(2,'musk@gmail.com','elon','musk','musk house','USA','788998','9898565265','musk@gmail.com','static/uploads/fb3098fe-f16f-457a-a80c-fa66e997110c');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `subcategory` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory`) values 
(1,1,'Fashion Photography'),
(2,1,'Wildlife Photography'),
(3,1,'Wedding photography'),
(4,2,'Product design'),
(5,2,'Branding design'),
(6,2,'Animation design'),
(7,3,'Frontend development'),
(8,3,'Backend development'),
(9,3,'Fullstack development'),
(10,4,'Content Strategist'),
(11,4,'SEO and SEM Specialist'),
(12,5,'Financial accounting'),
(13,5,'Tax accounting');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
