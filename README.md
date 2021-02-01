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

#### Domain Modeling Concept

* Among the three-layered architecture (presentation layer, business logic, database layer), the domain model is close to business logic. The domain model is the mental map that business owners have of their buseinesses. (p14) 
* The book shows the basic of building a domain model, and building an architecture around it that leaves the model as free as possible from external constraints. (p15)
* Domain modeling is closest to the business. Make it easy to understand and modify. (22)

### The Allocation System

We have separate systems that are responsible for buying stock, selling stock to customers, and shipping goods to customers. The allocation system needs to coordinate the process by allocating stock to a custormers' orders. (p15) We build a simple domain model that can allocate orders to batches of stock.

<img src="D:\tutorial\Architecture_Patterns_with_Python\Allocation_system.PNG" alt="Allocation_System" style="zoom:75%;" />

A batch now keeps track of a set of allocated OrderLine objects. When we allocate, if we have enought available quantity, we just add to the set. (p19)

![batch_order_UML](D:\tutorial\Architecture_Patterns_with_Python\batch_order_UML.PNG)



**Value Object**

* Whenever we have a business concept that has data but no identity, we often choose to represent it using *Value Object* pattern. A value object is any domain object that is uniquely identified by the data it holds; we usually make them immutable. (p19)
* An order line is uniquely identifies by its order ID, SKU, and quantity; if we change one of those values, we now have a new line. (p20)

**Entities**

* Entities, unlike values, have identity equality. We can change their values, and they are sitll recognizable the same thing. （p20)
* Batches, in our example, are entities. We can allocate lines to batch, or change the data that we expect it to arrive, and it will still be the same entity. （p20)

**Domain Service**

* Domain service operations don't have a natural home in an entity or value object. A function that allocates an order line, given a set of batches, is a domain service.（p21)
* Domain services are not the same thing as services from the *service layer*. A domain service represents a business concept or process, whereas a service-layer service represents a use case for your application. Often the service layer will call a domain service.（p23)

![domain_modeling](D:\tutorial\Architecture_Patterns_with_Python\domain_modeling.PNG)

### Chapter 2. Repository Pattern

**Repository Pattern:** A simplifying abstraction over the data storage, allowing us to decouple our model layer from the data layer.

![repositories](D:\tutorial\Architecture_Patterns_with_Python\repositories.PNG)