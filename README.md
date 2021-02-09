[toc]

## Preface

Reference

* *Test-Driven Development with Python* by Harry
* *Domain-Driven Design* by Eric
* *Implementing Domain-Driven Design* by Vaughn
* *Patterns of Enterprise Application Architecture* by Martin

Three tools for managing complexity:

* Test-driven development (TDD)
* Domain-driven design (DDD)
* Loosely coupled (micro) services integrated via messages (also called reactive microservices)

## Introduction

**Encapsulation and Abstraction（封装和抽象）**

* Simplifying behavior and hiding data
* Encapsulating behavior by identifying a task that needs to be done in our code and giving that task a well-defined object or function. We call that object of function an *abstraction*
* Encapsulating behavior by using abstractions is a powerful tool for making code more expressive, more testable, and easier to maintain.

**Layering（分层）**

When one function, module, or object uses another, we say that the one depends on the other. The interactions between our objects and functions may causes chaos, and the layered architectrues are one way of trackling this problem. The three-layered architecture(presentation layer, business logic, database layer) is one of the most common example.

* Presentation layer: user-interface components, like a web page, and API, or a command line
* Business logic: business rules and our workflows
* database layer: storing and retrieving data

Business logic becomes spread throughout the layers of our application is a common bad practice.

**依赖倒置原则（The Dependency Inversion Principle）**

A. High level modules should not depend upon low level modules. Both should depend upon abstractions.

B. Abstractions should not depend upon details. Details should depend upon abstraction.

A. 高层模块不应该依赖于低层模块，二者都应该依赖于抽象。

B. 抽象不应该依赖于具体实现细节，而具体实现细节应该依赖于抽象。

**Principles **(p12)

Behavior should come first and drive our storage requirements 

build model through TDD 

Keep model decoupled from technical concerns

build persistence-ignorant code

create stable APIs around our domain 

## Chapter 1. Domain Modeling

### Domain Modeling Concept

* Among the three-layered architecture (presentation layer, business logic, database layer), the domain model is close to business logic. The domain model is the mental map that business owners have of their buseinesses. (p14) 
* The book shows the basic of building a domain model, and building an architecture around it that leaves the model as free as possible from external constraints. (p15)
* Domain modeling is closest to the business. Make it easy to understand and modify. (22)

### The Allocation System

We have separate systems that are responsible for buying stock, selling stock to customers, and shipping goods to customers. The allocation system needs to coordinate the process by allocating stock to a custormers' orders. (p15) 

<img src="D:\tutorial\Architecture_Patterns_with_Python\Allocation_system.PNG" alt="Allocation_System" style="zoom:75%;" />

Now we build a simple domain model that can allocate orders to batches of stock. Below is the related domain knowlege.

* Customers place orders. An order is identified by an order reference and comprises multiple order lines, where each line has  SKU and a quantity.

* Purchasing department orders small batches of stock. A batch of stock has a unique ID called a reference, a SKU, and a quantity.

* When we allocate an order line to a batch, we will send stock from that specific batch to the customer's delivery address.

 A batch now keeps track of a set of allocated OrderLine objects. When we allocate, if we have enought available quantity, we just add to the set. (p19)

<img src="D:\tutorial\Architecture_Patterns_with_Python\batch_order_UML.PNG" alt="batch_order_UML" style="zoom:80%;" />



**Value Object**

* Whenever we have a business concept that has data but no identity, we often choose to represent it using *Value Object* pattern. A value object is any domain object that is uniquely identified by the data it holds; we usually make them immutable. (p19)
* An order line is uniquely identifies by its order ID, SKU, and quantity; if we change one of those values, we now have a new line. (p20)

**Entities**

* Entities, unlike values, have identity equality. We can change their values, and they are sitll recognizable the same thing. （p20)
* Batches, in our example, are entities. We can allocate lines to batch, or change the data that we expect it to arrive, and it will still be the same entity. （p20)

**Domain Service**

* A function that allocates an order line, given a set of batches, is a domain service. Domain service operations don't have a natural home in an entity or value object. （p21)

```python
def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f'Out of stock for sku {line.sku}')
```

* Domain services are not the same thing as services from the *service layer*. A domain service represents a business concept or process, whereas a service-layer service represents a use case for your application. *Often the service layer will call a domain service*.（p23)

### Wrap Up

<img src="D:\tutorial\Architecture_Patterns_with_Python\domain_modeling.PNG" alt="domain_modeling" style="zoom:67%;" />

## Chapter 2. Repository Pattern

### Repository Pattern/依赖倒置原则（The Dependency Inversion Principle）

* A simplifying abstraction over the data storage, allowing us to decouple our model layer from the data layer.
* The repository pattern is an abstraction over persistent storage. It hids the boring details of data access by pretending that all of our data is in memory (the objects are all in memory). (p27)

![repositories](D:\tutorial\Architecture_Patterns_with_Python\repositories.PNG)

* Our domain model has no dependencies whatsoever (Depending on a helper library is fine; depending on an ORM or a web framework is not). (p25)

![onion_architecture](D:\tutorial\Architecture_Patterns_with_Python\onion_architecture.PNG)

* We don't want infrastructure concerns bleeding over into our domain model and slowing our unit tests or our ability to make changes.(p25)

### ORM

*  **persistence ignorance**: the domain model doesn't need to know anything about how data is loaded and persisted.(p26)

**persistence**（持久化）: 把数据（如内存中的对象）保存到可永久报错的存储设备中（如磁盘）

在目前的企业应用系统设计中，MVC，即 Model（模型）- View（视图）- Control（控制）为主要的系统架构模式。MVC 中的 Model 包含了复杂的业务逻辑和数据逻辑，以及数据存取机制（如 JDBC的连接、SQL生成和Statement创建、还有ResultSet结果集的读取等）等。*将这些复杂的业务逻辑和数据逻辑分离，以将系统的紧耦 合关系转化为松耦合关系（即解耦合），是降低系统耦合度迫切要做的，也是持久化要做的工作。*MVC 模式实现了架构上将表现层（即View）和数据处理层（即Model）分离的解耦合，而持久化的设计则实现了数据处理层内部的业务逻辑和数据逻辑分离的解耦合。 而 ORM 作为持久化设计中的最重要也最复杂的技术，也是目前业界热点技术。

简单来说，按通常的系统设计，使用 JDBC 操作数据库，业务处理逻辑和数据存取逻辑是混杂在一起的。
一般基本都是如下几个步骤：
1、建立数据库连接，获得 Connection 对象。
2、根据用户的输入组装查询 SQL 语句。
3、根据 SQL 语句建立 Statement 对象 或者 PreparedStatement 对象。
4、用 Connection 对象执行 SQL语句，获得结果集 ResultSet 对象。
5、然后一条一条读取结果集 ResultSet 对象中的数据。
6、根据读取到的数据，按特定的业务逻辑进行计算。
7、根据计算得到的结果再组装更新 SQL 语句。
8、再使用 Connection 对象执行更新 SQL 语句，以更新数据库中的数据。
7、最后依次关闭各个 Statement 对象和 Connection 对象。

* **SQLAlchemy classical mapping**: Define the schema separately, and to define an explicit mapper for how to convert between the schema and our domain model. 

```python
from sqlalchemy.orm import mapper, relationship
import model

metadata = MetaData()
order_lines = Table(
	'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)

def start_mappers():
    lines_mapper = mapper(Model.Orderline, order_lines)
```

* The ORM imports the domain model, and not the other way around.
* If we call the mapper function, we will be able to easily load and save domain model instances from and to the database. But if we never call that function, our domain model classes stay blissfully unaware of the database.

Using SQLAlchemy directly in our API endpoint:

```python
@flask.route.gubbins
def allocate_endpoint():
	session = start_session()
	line = OrderLine(request.json['orderid'], request.json['sku'], request.json['qty'])
    # load all batches from the DB
    batches = session.query(Batch).all()
    # call our domain service
    allocate(line, batches)
	#save the allocation back to the database
    session.commit()
    return 201
```



### The Repository Pattern

* The repository pattern is an abstraction over persistent storage. It hides the boring details of data access by predending that all of our data is in memory.
* We swape the *SQLAlchemy abstraction(session.query(Batch))* for a *repository one (batches_repo.get)*

<img src="D:\tutorial\Architecture_Patterns_with_Python\repository.PNG" alt="repository" style="zoom:50%;" />

Using the repository directly in our API endpoint:

```python
@flask.route.gubbins
def allocate_endpoint():
	batches = SqlAlchemyRepository.list()
	lines = [OrderLine(l['orderid'], l['sku'], l['qty']) for l in request.params...]
	allocate(lines, batches)
	session.commit()
	return 201
```

```python
class SqlAlchemyRepository(AbstractRepository):
	def __init__(self, session):
		self.session = session
	def add(self, batch):
		self.session.add(batch)
	def get(self, reference):
		return self.session.query(model.Batch).filter_by(reference=reference).one()
	def list(self):
		return self.session.query(model.Batch).all()
```



## Chapter 3. A Brief Interlude: On Coupling and Abstractions

Coupling(耦合)： When we're unable to change component A for fear of breaking component B, we say that the component have become coupled.

