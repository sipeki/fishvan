#FISH VAN

created project on the 6th of July 2020

###Simon Kindlen
####DevOps and Cloud Consultant
####QA

>Introduction: In the next 20 minutes you will be taken through my project for DevOps Core Fundamentals. Demonstrating the technologies learnt in the last 5 weeks by deploying a CRUD web application.

#Content

* Brief

* Resources

* Scope



* Overview of the Application

* Overview of the Project Management

* Design

 * Wireframe

 * Data

* The Technology Stack
 Why chosen certain technologies

* CI Pipeline

*Front-end Design

* Risk Assessment

* Demo

* Lessons

* Future Features

* Author


##Brief

>The purpose of this project is to demonstrate our understanding of the technologies and methods covered in the initial 5 weeks of the Academy by applying those technologies and methods in developing a CRUD application and project management of the software life cycle.

###Resources
Project Management Trello: https://trello.com/b/v1pyqQxJ/fishvan

Fishvan Github: https://github.com/sipeki/fishvan.git


###Project Scope
* Trello board
* Relation Database, 2 tables joined
* Documentation
* Functional CRUD
* Functional website with Flask API
* Version Control System Feature Branch integrated into CI and Cloud VM



###Overview of the Application
<picture of paul and van>

Website for customers to place orders with the local mobile fishmonger. Reducing wait times for customers.

The project was inspired by a conversation with fishmonger Paul whose business is to drive around the local villages for customers to come to the van to plaice orders at the van and take home then there. Due to the increase in customers he was getting later and later, special during lock down, 3 hours late! I collected my fish at 9:30pm last Tuesday.  The benefit to Paul and his loyal customers was that the website would enable Paul’s customers to order at their convenience in advance to Paul’s visit. Orders could then be prepared in advance for collection from the van.
 
<picture of pittenweem>

Current time with each customer is on average 5 minutes, using the website would reduce the time to 1 minute. A fifth of the time spent with a customer. Reducing the time for each stop. Paul’s working day is at least 12 hours, 8 of those spent with customers. Theory reducing his working day to 5.5 hours. Giving him the option to deliver to more customers or spend more time with his family in Pittenweem.


###Overview of the Project Management

<picture of Trello>

####Trello
Trello was used to PM for the life cycle of the project. Jira was used in a previous Academy project. To keep the overhead of PM the project to scale with the project Trello was a better option.

####Agile
Agile methodology was implemented. Requirements, Analysis, Design, Coding and testing. Empirical Process Control was fully embraced. 

####SCRUM
Scrum Framework. Product Backlog listing all the desired features as user stories. Sprint Backlog with features for the next sprint. The Product Owner was myself. Workflow of the first sprint being to meet the CRUD requirement.
Morning stand ups were held with development team members. To review yesterday and the day ahead and report any blockers. Each taking weekly turns at Scrum Master reporting back to the overall PM. The stand ups were very beneficial and enabled the transfer of knowledge and focus.  

####MoSCoW
MoSCoW prioritisation technique used to define the Epic’s. 

* Must - Epic Sprint 
* Should - Epic Sprint 
* Could - Epic Sprint
* Won’t - Epic Sprint 
  

## Design
To meet the brief and deliver a website that has full CRUD implementation the first Epic of Must - Epic sprint was completed.
Orders placed with stock code. Orders listed with details of the order; item ordered, quantity and calculated price. Listing orders required joining two tables. Order updated, order deleted or all orders deleted.
 
###Functionality
The user stories that satisfied the brief:
* **_Must - Epic Sprint_**
  * **Create - Add Order**
    * _As any user I want to create an order line. So I can place a order._ 
  * **Read - List Orders**
    * _As any user I want to list order lines. So I can list all orders on the system and know the orders placed._
  * **Update - Modify Order**
    * _As any user I want to update the order line. So I can modify the order._
  * **Delete - Remove Order**
    * _As any user I want to delete an order. So I can remove an order from the system._

###Wireframe
The wireframes were kept high level and abstract. Which helped me conceptualise the data as well as how the data would be presented on the browser.
My initial idea was to have orders updated in line with the orders listed but due to technical constraints updates to orders were done on a separate page.


####wireframe basic CRUD - create order
https://docs.google.com/drawings/d/1svqFg9nDJm6gcjOqlnO--hQcLwyq_bupfMxwmyhMSnE/edit?usp=sharing

####wireframe basic CRUD - list orders (Read)
https://docs.google.com/drawings/d/1TsmxfqafClHriCTp6RvydeXJ7E72oHuFuWzeaD8oyvM/edit?usp=sharing

####wireframe basic CRUD -  Update orde
https://docs.google.com/drawings/d/1ClOTYLsifT9sLwcF5WKFx2RcB0wFAz1CB_UyIhcG2HY/edit?usp=sharing


####wireframe basic CRUD -  Delete order
https://docs.google.com/drawings/d/176OBYFL-XwpqBz1ASPWxvTz-ysGprSGWo4MecTlKcEo/edit?usp=sharing


###Data
Complete design of the data was carried out for the full MoSCoW Epic Sprints. The first two sprints are shown here Must and Should.
The application is data driven which makes it important to get the relationship correct before developing the methods to manipulate the data.
 

####Basic CRUD Van App - Orders List
The relation shown here is that a stock item will appear in many order lines.
# Basic CRUD Van App - Orders List


<table>
  <tr>
   <td colspan="2" ><strong>Stock </strong>
   </td>
   <td>
   </td>
   <td colspan="2" ><strong>Order Line</strong>
   </td>
  </tr>
  <tr>
   <td>stock_id
   </td>
   <td>Int (auto Prime not null
   </td>
   <td>1..x--->
   </td>
   <td>order_id 
   </td>
   <td>Int (auto Prime Required)
   </td>
  </tr>
  <tr>
   <td>detail
   </td>
   <td>varchar(50) not null
   </td>
   <td>
   </td>
   <td>fk_stock_id
   </td>
   <td>Int (foreign)
   </td>
  </tr>
  <tr>
   <td>price
   </td>
   <td>Decimal not null
   </td>
   <td>
   </td>
   <td>order_date
   </td>
   <td>date
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>quantity
   </td>
   <td>int
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>status
   </td>
   <td>int
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>


**Stock table**

create table if not exists stock(

stock_id int not null auto_increment,

detail varchar(50) is not null,

quantity int is not null,

price decimal is not null,

primary key(stock_id));

**Order Line table **

create table if not exists order_line(

order_id int not null auto_increment,

fk_stock_id int,

order_date,

quantity int,

status int,

primary key(order_id),

foreign key fk_stock_id references stock(stock_id),

foreign key fk_user_id references user(user_id));

**Join for orders list**

select u.f_name, u.f_name,  s.detail, ol.quantity, s.price*ol.quantity 

from user u

join stock s using(stock_id)

Join order_line ol using(order_id));


<table>
  <tr>
   <td>X
   </td>
   <td><strong>Orders</strong>
   </td>
   <td><strong>Stock</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Order_Line</strong>
   </td>
   <td>
   </td>
   <td>contain
   </td>
  </tr>
  <tr>
   <td><strong>Stock</strong>
   </td>
   <td>are part of
   </td>
   <td>
   </td>
  </tr>
</table>





# Should: Fish Van Application


<table>
  <tr>
   <td colspan="2" ><strong>Stock </strong>
   </td>
   <td>
   </td>
   <td colspan="2" ><strong>Order Line</strong>
   </td>
   <td>
   </td>
   <td colspan="2" ><strong>User</strong>
   </td>
  </tr>
  <tr>
   <td>stock_id
   </td>
   <td>Int (auto Prime not null
   </td>
   <td>1..x--->
   </td>
   <td>order_id 
   </td>
   <td>Int (auto Prime Required)
   </td>
   <td><p style="text-align: right">
x..1--->     </p>

   </td>
   <td>user_id
   </td>
   <td>Int (auto Prime Required)
   </td>
  </tr>
  <tr>
   <td>detail
   </td>
   <td>varchar(50) not null
   </td>
   <td>
   </td>
   <td>fk_stock_id
   </td>
   <td>Int (foreign)
   </td>
   <td>
   </td>
   <td>user_type
   </td>
   <td>int not null
   </td>
  </tr>
  <tr>
   <td>quantity
   </td>
   <td>Int not null
   </td>
   <td>
   </td>
   <td>fk_user_id
   </td>
   <td>Int (foreign)
   </td>
   <td>
   </td>
   <td>user_name
   </td>
   <td>varchar(15) not null
   </td>
  </tr>
  <tr>
   <td>price
   </td>
   <td>Decimal not null
   </td>
   <td>
   </td>
   <td>order_date
   </td>
   <td>date
   </td>
   <td>
   </td>
   <td>f_name
   </td>
   <td>varchar(20) not null
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>quantity
   </td>
   <td>int
   </td>
   <td>
   </td>
   <td>l_name
   </td>
   <td>varchar(20) not null
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>status
   </td>
   <td>int
   </td>
   <td>
   </td>
   <td>address
   </td>
   <td>varchar(50) not null
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>email
   </td>
   <td>varchar(25) not null
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>mobile
   </td>
   <td>int not null
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>





<table>
  <tr>
   <td>X
   </td>
   <td><strong>User Customer (user_type =1)</strong>
   </td>
   <td><strong>Orders</strong>
   </td>
   <td><strong>Stock</strong>
   </td>
  </tr>
  <tr>
   <td><strong>User Customer (user_type =1)</strong>
   </td>
   <td>
   </td>
   <td>make
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Order_Line</strong>
   </td>
   <td>are made by
   </td>
   <td>
   </td>
   <td>contain
   </td>
  </tr>
  <tr>
   <td><strong>Stock</strong>
   </td>
   <td>
   </td>
   <td>are part of
   </td>
   <td>
   </td>
  </tr>
</table>


**Stock table**

create table if not exists stock(

stock_id int not null auto_increment,

detail varchar(50) is not null,

quantity int is not null,

price decimal is not null,

primary key(stock_id));

**Order Line table **

create table if not exists order_line(

order_id int not null auto_increment,

fk_stock_id int,

fk_user_id int,

order_date,

quantity int,

status int,

primary key(order_id),

foreign key fk_stock_id references stock(stock_id),

foreign key fk_user_id references user(user_id));

**User table**

create table if not exists user(

user_id is not null auto_increment,

user_type int not null default 1,

f_name varchar(20) is not null,

l_name varchar(20) is not null,

Address varchar(50) is not null,

email varchar(25) is not null,

mobile int not null,

primary key(user_id),

unique(user_id));

**Join for orders list**

select u.f_name, u.f_name,  s.detail, ol.quantity, s.price*ol.quantity 

from user u

join stock s using(stock_id)

Join order_line ol using(order_id));

 


# 

X
Orders
Stock
Order_Line


contain
Stock
are part of



####Should: Fish Van Application
A user, customer user_type = 1, has many order lines. The order line has many stock items.



###Risk Assessment
As well as looking at the risk of the application in production but also in development.
Risk
Assessment
Chances
Impact
Responsible
Initial action
Further Action
Response
Tolerance
Github unavailable
During development Github was not available Monday mornings for login
High
Medium
Provider
None
Wait until commit and push successful
If persists change provider
Tolerable
SQL Offline
SQL Database goes offline would stop all functionality 
Low
High
Povider
none
Keep SQL image current run locally
Check service status. Look at alternative providers.
Tolerable
Production code deleted
Production files and data delete
Low
High
Provider / App owner
Restore
Carry out investigation
Learn lesson and mitigate 
Intolerable
Man in the middle attack
Possible compromise of user particulars impact legal compliance
High
High
App Owner
None
HTTPS access only. Data encrypted between endpoints.
Disclose attack to users and regulator body
Action required


##The Technology Stack
A list of the technologies deployed to meet the requirements of the scope.
*Trello project management Kanban Board
*GCP SQL : Running a cloud instance of MYSQL 5.7 
*GCP Compute Engine: running a cloud instance VM Ubuntu 20.4 LTS SSD 20GB
*Github: Version control with branching
*Python: Programming language
*Flask: Lightweight WSGI web application micro-framework
*Jinja2: Template engine
*Pycharm: IDE for source code development, integrated with Github and pytest
*Jenkins: As CI server
*NGIX: Load balancing and application web server

###Why these technologies?
During the initial weeks of Academy in teams we looked at the technologies required to deploy CI Pipeline. There are alot of options out there. It is possible to choose a provider that meets all the parts required for the pipeline. As it is important to have full integration between the steps to enable smooth flow for software to be developed. A robust pipeline, like any constant process manufacturing, produces a consistent high quality product.
Without testing each option fully it would be difficult to ascertain the claims of the software manufacturer to be actuarial or vapourware.
The current experience of myself required research on others more knowledgeable on CI to form my opinion on what technologies to choose.
Thus it came down to what tools best integrated best with the core technologies. Tried and tested by the community at large. Researching on g2.com and other websites

*Python makes it easy to learn and develop applications quickly. Integration features and extensive support libraries.
*Github: was chosen due to a large community, not centralized, and was free for 500GB.
*Jenkins: Works as a standalone CI server or a continuous delivery platform. Pre-built packages for Unix, Windows, and OS X ensures an easy installation process. A web interface that can be used to quickly configure your server. Free

##CI Pipeline


#DEMO

##Lessons
Keep focused on the task at hand and do not let your focus be affected by others perceived progress.
Choosing meaningful variables
Simpler is more robust.
Better understanding of data modeling
Running before I could walk, or even crawl! Spent trying to try and deliver order filtering on . Rather than deliver more incremental functionality.


##Future Features

###Should - Epic Sprint User Stories
*Login as a customer user
*Read - List Customer Orders
*Create - Customer Place Order
*Update - Customer modifies order
*Delete - Remove Unwanted Order

###Could - Epic Sprint User Stories
*Login as a fishmonger user
*Create - Create Stock Item
*Read - List Stock Items 
*Update - Modify Stock Item
*Delete - Remove Stock Item

###Won’t - Epic Sprint User Stories
*Login as a fishmonger user and order for customer
*Create - Create order for customer
*Read - List particular customers orders
*Update - Modify a customers order
*Delete - Remove Customer order






