# FISH VAN

created project on the 6th of July 2020


Simon Kindlen, 
DevOps and Cloud Consultant,
QA 

![Simon kindlen](https://i.imgur.com/DAaZve5.jpg)
>Introduction: In the next 20 minutes you will be taken through my project for DevOps Core Fundamentals. Demonstrating the technologies learnt in the last 5 weeks by deploying a CRUD web application.

# Content

* Brief
* Resources
* Scope
* Overview of the Application
* Overview of the Project Management
* Design
  * Functionality
  * Wireframe
  * Data
  
* The Technology Stack
  * Why chosen certain technologies
* CI Pipeline
* Front-end Design
* Risk Assessment
* Demo
* Lessons
* Future Features


## Brief

>The purpose of this project is to demonstrate our understanding of the technologies and methods covered in the initial 5 weeks of the Academy by applying those technologies and methods in developing a CRUD application and project management of the software life cycle.

### Resources
Project Management Trello: https://trello.com/b/v1pyqQxJ/fishvan

Fishvan Github: https://github.com/sipeki/fishvan.git


### Project Scope
* Trello board
* Relation Database, 2 tables joined
* Documentation
* Functional CRUD
* Functional website with Flask API
* Version Control System Feature Branch integrated into CI and Cloud VM



### Overview of the Application

![Paul Fishvan](https://i.imgur.com/pgWEcPI.jpg)


Website for customers to place orders with the local mobile fishmonger. Reducing wait times for customers.

The project was inspired by a conversation with fishmonger Paul whose business is to drive around the local villages for customers to come to the van to plaice orders at the van and take home then there. Due to the increase in customers he was getting later and later, special during lock down, 3 hours late! I collected my fish at 9:30pm last Tuesday.  The benefit to Paul and his loyal customers was that the website would enable Paul’s customers to order at their convenience in advance to Paul’s visit. Orders could then be prepared in advance for collection from the van.
 

![pittenweem](https://i.imgur.com/ClrvJGF.jpg)

Current time with each customer is on average 5 minutes, using the website would reduce the time to 1 minute. A fifth of the time spent with a customer. Reducing the time for each stop. Paul’s working day is at least 12 hours, 8 of those spent with customers. Theory reducing his working day to 5.5 hours. Giving him the option to deliver to more customers or spend more time with his family in Pittenweem.


### Overview of the Project Management

![Trello](https://i.imgur.com/wGlJwrf.jpg)

#### Trello
Trello was used to PM for the life cycle of the project. Jira was used in a previous Academy project. To keep the overhead of PM the project to scale with the project Trello was a better option.

#### Agile
Agile methodology was implemented. Requirements, Analysis, Design, Coding and testing. Empirical Process Control was fully embraced. 

#### SCRUM
Scrum Framework. Product Backlog listing all the desired features as user stories. Sprint Backlog with features for the next sprint. The Product Owner was myself. Workflow of the first sprint being to meet the CRUD requirement.
Morning stand ups were held with development team members. To review yesterday and the day ahead and report any blockers. Each taking weekly turns at Scrum Master reporting back to the overall PM. The stand ups were very beneficial and enabled the transfer of knowledge and focus.  

#### MoSCoW
![MoSCOW](https://i.imgur.com/SBKdjf9.jpg)
MoSCoW prioritisation technique used to define the Epic’s. 

* Must - Epic Sprint 
* Should - Epic Sprint 
* Could - Epic Sprint
* Won’t - Epic Sprint 
  

## Design
To meet the brief and deliver a website that has full CRUD implementation the first Epic of Must - Epic sprint was completed.
Orders placed with stock code. Orders listed with details of the order; item ordered, quantity and calculated price. Listing orders required joining two tables. Order updated, order deleted or all orders deleted.
 
### Functionality
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

### Wireframe
The wireframes were kept high level and abstract. Which helped me conceptualise the data as well as how the data would be presented on the browser.
My initial idea was to have orders updated in line with the orders listed but due to technical constraints updates to orders were done on a separate page.


#### Wireframe basic CRUD - create order
![wireframe basic CRUD - create order](https://i.imgur.com/oGKo5R0.jpg)

#### Wireframe basic CRUD - list orders (Read)
![wireframe basic CRUD - list orders (Read)](https://i.imgur.com/15LBJM4.jpg)


#### Wireframe basic CRUD -  Update order
![wireframe basic CRUD -  Update order](https://i.imgur.com/2ZRyUg8.jpg)



#### Wireframe basic CRUD -  Delete order
![ireframe basic CRUD -  Delete order](https://i.imgur.com/U0cHavc.jpg)



### Data
Complete design of the data was carried out for the full MoSCoW Epic Sprints. The first two sprints are shown here Must and Should.
The application is data driven which makes it important to get the relationship correct before developing the methods to manipulate the data.
 

#### Minimum Viable Product CRUD Van App - Orders List
The relationship shown here is that a stock item will appear in many order lines.

![Must CRUD TABLE MVP](https://i.imgur.com/YpB4ycP.jpg)

![Must CRUD TABLE MVP Relation](https://i.imgur.com/hcCMt16.jpg)


#### Should: Fish Van Application
A user, customer user_type = 1, has many order lines. The order line has many stock items.

![Should CRUD TABLE MVP](https://i.imgur.com/z0uJIXE.jpg)

![Should CRUD TABLE MVP Relation](https://i.imgur.com/14StbmA.jpg)




### Risk Assessment
As well as looking at the risk of the application in production but also in development.

![fishvan risk assesment](https://i.imgur.com/Yo6IiQf.jpg)


## The Technology Stack
A list of the technologies deployed to meet the requirements of the scope.
* <b>Trello:</b> project management Kanban Board
* <b>GCP SQL:</b> Running a cloud instance of MYSQL 5.7 
* <b>GCP Compute Engine:</b> running a cloud instance VM Ubuntu 20.4 LTS SSD 20GB
* <b>Github:</b> Version control with branching
* <b>Python:</b> Programming language
* <b>Flask:</b> Lightweight WSGI web application micro-framework
* <b>Jinja2:</b> Template engine
* <b>Pycharm:</b> IDE for source code development, integrated with Github and pytest
* <b>Jenkins:</b> As CI server
* <b>NGIX:</b> Load balancing and application web server

### Why these technologies?
![git hub newtork](https://i.imgur.com/j6yA7v7.jpg)
During the initial weeks of Academy in teams we looked at the technologies required to deploy CI Pipeline. There are alot of options out there. It is possible to choose a provider that meets all the parts required for the pipeline. As it is important to have full integration between the steps to enable smooth flow for software to be developed. A robust pipeline, like any constant process manufacturing, produces a consistent high quality product.
Without testing each option fully it would be difficult to ascertain the claims of the software manufacturer to be actuarial or vapourware.
The current experience of myself required research on others more knowledgeable on CI to form my opinion on what technologies to choose.
Thus it came down to what tools best integrated best with the core technologies. Tried and tested by the community at large. Researching on g2.com and other websites

* Python makes it easy to learn and develop applications quickly. Integration features and extensive support libraries.
* Github: was chosen due to a large community, not centralized, and was free for 500GB.
* Jenkins: Works as a standalone CI server or a continuous delivery platform. Pre-built packages for Unix, Windows, and OS X ensures an easy installation process. A web interface that can be used to quickly configure your server. Free

## CI Pipeline for Fishvan
![CI Pipeline for Fishvan](https://i.imgur.com/JtLWrWw.jpg?1)



# DEMO

## Lessons

* Keep focused on the brief at hand deliver MVP before ambition.
* Choosing meaningful variables
* Simpler is more robust.
* Better understanding of data modeling
* Running before I could walk, or even crawl! Spent valuable time trying to try and deliver order filtering on . Rather than deliver more incremental functionality.


## Future Features
* CSS and Branding

### Should - Epic Sprint User Stories
* <i>Login as a customer user</i>
  * <b>Read</b> - List Customer Orders
  * <b>Create</b> - Customer Place Order
  * <b>Update</b> - Customer modifies order
  * <b>Delete</b> - Remove Unwanted Order

### Could - Epic Sprint User Stories
* <i>Login as a fishmonger user and manage stock</i>
  * <b>Create</b> - Create Stock Item
  * <b>Read</b> - List Stock Items 
  * <b>Update</b> - Modify Stock Item
  * <b>Delete</b> - Remove Stock Item

### Won’t - Epic Sprint User Stories
* <i>Login as a fishmonger user and manage customer orders</i>
  * <b>Create</b> - Create order for customer
  * <b>Read</b> - List particular customers orders
  * <b>Update</b> - Modify a customers order
  * <b>Delete</b> - Remove Customer order

# Thank You! 




