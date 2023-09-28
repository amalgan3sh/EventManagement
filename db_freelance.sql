/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - platform_for_freelancers
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`platform_for_freelancers` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `platform_for_freelancers`;

/*Table structure for table `assign_staff_service` */

DROP TABLE IF EXISTS `assign_staff_service`;

CREATE TABLE `assign_staff_service` (
  `assign_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assign_service_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `assign_staff_service` */

insert  into `assign_staff_service`(`assign_service_id`,`service_id`,`staff_id`) values (1,3,1),(5,2,3),(6,2,1),(7,3,5);

/*Table structure for table `assignproject` */

DROP TABLE IF EXISTS `assignproject`;

CREATE TABLE `assignproject` (
  `assignproject_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assignproject_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `assignproject` */

insert  into `assignproject`(`assignproject_id`,`project_id`,`staff_id`,`date`,`status`) values (1,2,4,'2021-03-30','xcvbnm'),(2,1,3,'2021-04-01','pending'),(3,1,4,'2021-04-01','pending'),(4,1,5,'2021-04-01','asaascvb');

/*Table structure for table `categories` */

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `categories` */

insert  into `categories`(`category_id`,`category_name`,`category_description`) values (1,'cat1','test'),(4,'cat2','testingsss');

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
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`first_name`,`last_name`,`phone`,`email`,`house_name`,`place`,`pincode`,`photo`) values (1,'arun@g.com','arun','s','6778987678','arun@g.com','arun','tirur','670789','static/uploads/30854f56-a687-4da3-8954-b0269f3a9528paris.jpg'),(4,'abc@gmail.com','abc','efg','8798765434','abc@gmail.com','abc','dfghn','345678','static/uploads/d743f6ce-c2da-48a1-a378-2338d972668b454177.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('admin','admin','admin'),('arun@g.com','arun','customer'),('shimi','shimi','customer'),('anu@g.com','anu','staff'),('abc@gmail.com','abc','customer'),('qert@g.com','qert','customer'),('amal@g.com','amal','staff'),('akhi@g.com','akhila','staff');

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
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `messages` */

insert  into `messages`(`message_id`,`sender_id`,`reciever_id`,`message`,`message_date`,`sendertype`) values (1,5,1,'hello','2021-04-01','staff'),(2,1,5,'hyy','2021-04-01','customer'),(3,5,1,'sdgdf','2021-04-01','staff'),(4,5,1,'sdfsdf','2021-04-01','staff'),(5,5,1,'asfsdf','2021-04-01','staff'),(6,5,1,'hello','2021-04-01','staff'),(7,5,1,'accept','2021-04-01','staff'),(8,5,1,'sdgdf','2021-04-01','staff'),(9,5,1,'dffhdfh','2021-04-01','staff'),(10,5,1,'fdghdf','2021-04-01','staff'),(11,5,1,'fhdzgh','2021-04-01','staff'),(12,5,1,'hjfgj','2021-04-01','staff'),(13,5,1,'gjgfj','2021-04-01','staff'),(14,5,1,'dshgdfhh','2021-04-01','staff'),(15,5,1,'fhghj','2021-04-01','staff'),(16,5,1,'fhghj','2021-04-02','staff'),(17,1,3,'xcvbv','2021-04-02','customer'),(18,1,3,'sdcfvb ','2021-04-02','customer'),(19,1,3,'','2021-04-02','customer'),(20,1,3,'dfgh','2021-04-02','customer'),(21,1,3,'','2021-04-02','customer'),(22,1,3,'wedrftghj','2021-04-02','customer'),(23,1,3,'dfghjk','2021-04-02','customer'),(24,1,3,'rfghjk','2021-04-02','customer'),(25,1,3,'vccbcbvbv','2021-04-02','customer'),(26,1,4,'sdfgbn','2021-04-03','customer'),(27,1,4,'bnm','2021-04-03','customer'),(28,1,4,'frghx hjgfdetdf xygazujhx','2021-04-03','customer');

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `project` */

insert  into `project`(`project_id`,`customer_id`,`subcategory_id`,`projectname`,`date`,`status`) values (1,1,1,'pro1','2/3/21','pending'),(2,1,2,'pro2','3/4/21','confirm');

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`project_id`,`amount`,`date`,`status`) values (1,1,'112350','2021-03-29 11:16:49','accept'),(2,2,'12000','2021-03-29 11:19:22','pending');

/*Table structure for table `quotation` */

DROP TABLE IF EXISTS `quotation`;

CREATE TABLE `quotation` (
  `quotation_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `quotation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`quotation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `quotation` */

insert  into `quotation`(`quotation_id`,`project_id`,`quotation`) values (1,1,'112345678'),(2,2,'500');

/*Table structure for table `quotation_deposit` */

DROP TABLE IF EXISTS `quotation_deposit`;

CREATE TABLE `quotation_deposit` (
  `deposit_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `deposit_date` varchar(100) DEFAULT NULL,
  `deposit_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`deposit_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `quotation_deposit` */

insert  into `quotation_deposit`(`deposit_id`,`project_id`,`amount`,`deposit_date`,`deposit_status`) values (1,1,'112345678','2021-04-03','paid');

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `reported` */

insert  into `reported`(`reported_id`,`reported_by_id`,`reported_whom_id`,`reported_date`,`reason`,`reported_status`) values (1,1,3,'2021-04-02','asdfgh','reported'),(2,1,4,'2021-04-02','sdcfvbg','reported'),(3,1,4,'2021-04-02','sdfghj','reported'),(4,1,5,'2021-04-02','swdfghj','reported'),(5,1,4,'2021-04-02','dfghj','reported'),(6,4,1,'2021-04-02','sdfghjk','reported');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`service_id`,`service`) values (1,'asdf'),(2,'xcv'),(3,'sdcfvb'),(6,'sdfghjk');

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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`first_name`,`lastname`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`) values (1,'abi@g.com','abi','s','dfghjk','cvgbh','786786','8798765434','abi@g.com','static/uploads/a3102c05-bb88-4aea-aabf-31e596142720paris.jpg'),(3,'sdfg@g.com','sdfg','dfgh','dfgh','fgh','453567','1234567890','ds@g.com','static/uploads/98daf4c4-49b9-46ec-a27c-b5b6110b08a7454177.jpg'),(4,'anu@g.com','anu','k','sdxfgvbn','tly','556456','1234567890','anu@g.com','static/uploads/5083a1ed-7e1d-4555-8402-4108423d2e6d453386.jpg'),(5,'amal@g.com','amal','ganesh','cfvgbh','erk','456567','6744567776','amal@g.com','static/uploads/350e99de-cd8e-424c-b9ed-6437c333c099454177.jpg'),(6,'akhi@g.com','akhila','c','akhila','calicut','678789','7687564534','akhi@g.com','static/uploads/af6b9eee-34f3-4111-b6e1-90cb6fe5cea6453289.jpg');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `subcategory` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory`) values (1,4,'subcat4'),(2,4,'subcat4'),(6,1,'subcatsss');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
