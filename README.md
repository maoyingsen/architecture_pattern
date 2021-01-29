[toc]

### Preface

Reference

* *Test-Driven Development with Python* by Harry
* *Domain-Driven Design* by Eric
* *Implementing Domain-Driven Design* by Vaughn
* *Patterns of Enterprise Application Architecture* by Martin

Three tools for managing complexity:

* Test-driven development (TDD)
* Domain-driven design (DDD)
* Loosely coupled (micro) services integrated via messages (also called reactive microservices)

### Introduction

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

**Principles**

Behavior should come first and drive our storage requirements

build model through TDD

Keep model decoupled from technical concerns

build persistence-ignorant code

create stable APIs around our domain 