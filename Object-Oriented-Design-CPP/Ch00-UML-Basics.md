![UML class diagram](images\uml-conversion.svg)



# **What is `<<interface>>` in UML?**
- In UML, `<<interface>>` denotes an **interface** type, which specifies a contract of methods that a class must implement without providing the implementation itself.
- An interface in UML is usually represented as a class with the `<<interface>>` stereotype.

In C++, there are no explicit interface keywords like in Java or C#. Instead, interfaces are implemented using **abstract base classes** that:
1. Contain only pure virtual methods.
2. Do not have member data.

---

## **UML Representation of `<<interface>>`**
- An interface in UML:
  - Appears as a rectangle with the label `<<interface>>` above its name.
  - Lists the operations (methods) the interface defines.
- Example:

```
<<interface>>
IShape
+ draw() : void
+ resize(scale: double) : void
```

- This means any class implementing `IShape` must define the `draw` and `resize` methods.

---

## **C++ Implementation of an Interface**
Here’s how to implement the `IShape` interface in C++:

## **Interface Definition**
```cpp
class IShape {
public:
    virtual void draw() const = 0;      // Pure virtual method
    virtual void resize(double scale) = 0; // Pure virtual method

    virtual ~IShape() = default;       // Virtual destructor
};
```

## **Class Implementing the Interface**
```cpp
class Circle : public IShape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}

    void draw() const override {
        std::cout << "Drawing a Circle with radius " << radius << std::endl;
    }

    void resize(double scale) override {
        radius *= scale;
        std::cout << "Resized Circle to radius " << radius << std::endl;
    }
};
```

### **Using the Interface**
```cpp
int main() {
    IShape* shape = new Circle(5.0);
    shape->draw();               // Output: Drawing a Circle with radius 5
    shape->resize(2.0);          // Output: Resized Circle to radius 10
    delete shape;                // Clean up
    return 0;
}
```

---

# **Understanding `<<abstract>>` in UML**
In UML, the `<<abstract>>` stereotype represents an **abstract class**. 

An abstract class in UML:
- Serves as a base class for other classes.
- Cannot be instantiated directly.
- May contain:
  - **Abstract methods** (pure virtual functions in C++) that must be implemented by derived classes.
  - **Concrete methods** (fully defined methods) that derived classes inherit as-is.

---

## **UML Representation of an Abstract Class**
- The `<<abstract>>` stereotype is displayed above the class name.
- Abstract methods are italicized or explicitly marked as `abstract`.
  
**Example UML Abstract Class:**
```
<<abstract>>
Shape
+ draw() : void  {abstract}
+ calculateArea() : double {abstract}
+ move(x: int, y: int) : void
```

This means:
1. `Shape` cannot be instantiated.
2. Derived classes must implement `draw` and `calculateArea`.
3. `move` is a concrete method that all derived classes inherit.

---

### **Abstract Classes in C++**
C++ implements abstract classes using:
1. **Pure virtual functions** for abstract methods.
2. A virtual destructor to ensure proper cleanup for derived classes.

---

#### **C++ Implementation Example**

**Abstract Class Definition:**
```cpp
class Shape {
public:
    // Abstract methods (pure virtual functions)
    virtual void draw() const = 0;
    virtual double calculateArea() const = 0;

    // Concrete method
    void move(int x, int y) {
        std::cout << "Moving shape to (" << x << ", " << y << ")" << std::endl;
    }

    // Virtual destructor for cleanup
    virtual ~Shape() = default;
};
```

**Derived Class Implementation:**
```cpp
class Rectangle : public Shape {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    void draw() const override {
        std::cout << "Drawing a rectangle of width " << width << " and height " << height << std::endl;
    }

    double calculateArea() const override {
        return width * height;
    }
};
```

**Using Abstract Classes:**
```cpp
int main() {
    Shape* shape = new Rectangle(5.0, 3.0);

    shape->draw(); // Output: Drawing a rectangle of width 5 and height 3
    std::cout << "Area: " << shape->calculateArea() << std::endl; // Output: Area: 15
    shape->move(10, 15); // Output: Moving shape to (10, 15)

    delete shape; // Clean up
    return 0;
}
```

---

### **Key Points**
1. Abstract classes can include both abstract and concrete methods.
2. Pure virtual functions (`= 0`) in C++ define the methods that must be implemented by derived classes.
3. Virtual destructors ensure derived classes clean up correctly when deleted via a base-class pointer.

---

In C++, the terms **abstract class** and **interface** are closely related but serve slightly different purposes. Let’s break down the differences.

---

### **1. Abstract Class**
An **abstract class** in C++ is a class that:
- Can have both **pure virtual methods** (methods with `= 0`) and **concrete methods** (fully defined).
- May contain member variables (data members) and constructors.
- Serves as a base class to provide a common implementation or shared functionality to derived classes.

**Example: Abstract Class**
```cpp
class AbstractShape {
protected:
    double x, y; // Data members for position

public:
    AbstractShape(double x = 0, double y = 0) : x(x), y(y) {}

    // Pure virtual function (abstract method)
    virtual void draw() const = 0;

    // Concrete method
    void move(double newX, double newY) {
        x = newX;
        y = newY;
        std::cout << "Moved shape to (" << x << ", " << y << ")\n";
    }

    virtual ~AbstractShape() = default;
};
```

Derived classes must implement the `draw()` method but can also use the `move()` method as-is.

---

# **2. Interface**
An **interface** in C++ is a **specialized abstract class** designed to represent a contract:
- **Only pure virtual methods**: All methods are abstract (pure virtual functions).
- **No data members**: Interfaces only define behavior, not state.
- Typically, interfaces are used when multiple classes need to share a common API but may not share any implementation.

**Example: Interface**
```cpp
class IShape {
public:
    virtual void draw() const = 0;         // Pure virtual function
    virtual void resize(double scale) = 0; // Pure virtual function

    virtual ~IShape() = default;           // Virtual destructor
};
```

Classes implementing this interface must provide implementations for all methods:
```cpp
class Circle : public IShape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}

    void draw() const override {
        std::cout << "Drawing a Circle with radius " << radius << std::endl;
    }

    void resize(double scale) override {
        radius *= scale;
        std::cout << "Resized Circle to radius " << radius << std::endl;
    }
};
```

---

### **Key Differences Between Abstract Classes and Interfaces**
| **Feature**                | **Abstract Class**                          | **Interface**                           |
|----------------------------|---------------------------------------------|-----------------------------------------|
| **Methods**                | Can have a mix of concrete and abstract methods. | All methods are pure virtual (abstract). |
| **Data Members**           | Can include data members.                   | Cannot include data members.            |
| **Purpose**                | Shares functionality and behavior.          | Defines a contract without implementation. |
| **Inheritance**            | Supports single inheritance for base classes. | Can be "mimicked" with multiple inheritance. |
| **Use Case**               | Used when some functionality needs to be shared among derived classes. | Used when only the behavior (contract) is needed. |

---

### **When to Use Which?**

#### Use an **Abstract Class** when:
- You need to share some implementation (e.g., `move()` in `AbstractShape`).
- You want to provide default behavior that some derived classes can reuse.

#### Use an **Interface** when:
- You only want to enforce a contract (e.g., ensuring all shapes implement `draw()`).
- You need to allow multiple inheritance of behavior (C++ does not allow multiple base classes with implementation, but interfaces solve this).

---

   <<interface>>
   Drawable
      + draw() : void

         ▲
         |
     Circle
      + draw() : void


### **Understanding Generalization: `A implements B`**

1. **"Implements"** means a class (`A`) fulfills the contract defined by an interface (`B`).
   - If `B` is an interface, `A` provides the implementation for all the methods defined in `B`.

---

### **Example in UML**

#### Generalization: `A Implements B`
1. **UML Notation**:
   - **Interface**: `<<interface>> Drawable`
   - **Class**: `Circle`

**Diagram**:
```
   <<interface>>
   Drawable
      + draw() : void

         ▲
         |
     Circle
      + draw() : void
```

This UML diagram means:
- `Drawable` is an interface that declares the method `draw()`.
- `Circle` implements the `Drawable` interface by providing the implementation for the `draw()` method.

---

### **Step 1: Generalization in OOP**

#### Definition:
1. **Interface Definition**:
   The base `B` defines the abstract contract.
   ```cpp
   class Drawable {
   public:
       virtual void draw() const = 0; // Pure virtual function
       virtual ~Drawable() = default;
   };
   ```

2. **Class Implementation**:
   The derived `A` (e.g., `Circle`) implements the behavior.
   ```cpp
   class Circle : public Drawable {
   public:
       void draw() const override {
           std::cout << "Drawing a Circle!" << std::endl;
       }
   };
   ```

3. **Usage Example**:
   ```cpp
   int main() {
       Drawable* drawable = new Circle();
       drawable->draw(); // Output: Drawing a Circle!
       delete drawable;
       return 0;
   }
   ```

---

### **Step 2: Generalization in UML with Multiple Implementations**

Sometimes, a class can implement multiple interfaces (allowed in C++). For example:
- `Shape` defines geometric properties.
- `Drawable` defines drawing behavior.

**UML Diagram**:
```
   <<interface>>    <<interface>>
      Shape          Drawable
      + area()       + draw()

           ▲            ▲
            \          /
              Rectangle
      + area() : double
      + draw() : void
```

**C++ Example**:
```cpp
class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Drawable {
public:
    virtual void draw() const = 0;
    virtual ~Drawable() = default;
};

// Rectangle implements both Shape and Drawable
class Rectangle : public Shape, public Drawable {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double area() const override {
        return width * height;
    }

    void draw() const override {
        std::cout << "Drawing a Rectangle!" << std::endl;
    }
};

// Using the implementations
int main() {
    Rectangle rect(5.0, 3.0);

    Drawable* drawable = &rect;
    drawable->draw(); // Output: Drawing a Rectangle!

    Shape* shape = &rect;
    std::cout << "Area: " << shape->area() << std::endl; // Output: Area: 15

    return 0;
}
```

---

### **Summary of `A Implements B` in UML and C++**

1. **In UML**:
   - The relationship is represented with a hollow triangle pointing from the implementing class (`A`) to the interface (`B`).
   - `<<interface>>` denotes that `B` is an interface.

2. **In C++**:
   - Implement interfaces using abstract classes with pure virtual functions.
   - A class implementing the interface must:
     - Provide concrete definitions for all pure virtual functions.
   - Multiple inheritance allows a class to implement multiple interfaces.

---
### **Understanding Generalization: `A inherits from B` (A "is-a" B)**

In the context of **OOP** and **UML**, inheritance establishes a hierarchical relationship where:
- Class `A` (the derived class or subclass) **inherits from** class `B` (the base class or superclass).
- This relationship signifies that `A` **"is-a"** type of `B`.

---

### **Key Points of `A inherits from B`**
1. **Generalization**:
   - The base class (`B`) defines common attributes and behaviors.
   - The derived class (`A`) extends or specializes the base class.
   - In UML, this is represented with a **solid line with a hollow triangle arrowhead** pointing from `A` (subclass) to `B` (superclass).

2. **Polymorphism**:
   - `A` can override methods from `B` to provide specialized behavior.
   - A reference to the base class (`B`) can point to an object of the derived class (`A`).

3. **UML Representation**:
   - **Class**: `Shape`
     - Attributes: `x`, `y` (position).
     - Methods: `move(x, y)`.
   - **Derived Class**: `Circle`
     - Adds a `radius` attribute.
     - Overrides `draw`.

---

### **Step 1: UML Diagram for A "is-a" B**

**UML Example:**
```
   Shape
   + move(x: int, y: int) : void

       ▲
       |
    Circle
    + radius: double
    + draw() : void
```

This diagram means:
1. `Shape` is the base class with shared attributes and behavior.
2. `Circle` inherits from `Shape` and adds new behavior (`draw()`) and attributes (`radius`).

---

### **Step 2: A "is-a" B in C++**

#### **Base Class Definition (`B`)**
The base class contains shared attributes and methods:

```cpp
class Shape {
protected:
    int x, y; // Position of the shape

public:
    Shape(int x = 0, int y = 0) : x(x), y(y) {}

    void move(int newX, int newY) {
        x = newX;
        y = newY;
        std::cout << "Moved shape to (" << x << ", " << y << ")" << std::endl;
    }

    virtual void draw() const = 0; // Pure virtual method

    virtual ~Shape() = default;
};
```

#### **Derived Class Definition (`A`)**
The derived class specializes the base class by:
- Adding specific attributes (`radius`).
- Implementing or overriding base methods (`draw`).

```cpp
class Circle : public Shape {
private:
    double radius;

public:
    Circle(int x, int y, double r) : Shape(x, y), radius(r) {}

    void draw() const override {
        std::cout << "Drawing a Circle at (" << x << ", " << y << ") with radius " << radius << std::endl;
    }
};
```

---

### **Step 3: Using Inheritance in C++**

#### **Example Program**
```cpp
int main() {
    Circle circle(10, 15, 5.0); // Create a Circle

    circle.draw(); // Output: Drawing a Circle at (10, 15) with radius 5
    circle.move(20, 25); // Output: Moved shape to (20, 25)
    circle.draw(); // Output: Drawing a Circle at (20, 25) with radius 5

    return 0;
}
```

---

### **Key Concepts in the Example**
1. **Shared Behavior in the Base Class (`Shape`)**:
   - The `move()` method is implemented in `Shape` and shared by all derived classes.
   
2. **Specialized Behavior in the Derived Class (`Circle`)**:
   - The `Circle` class adds specific attributes (`radius`) and implements the abstract `draw()` method.

3. **Polymorphism**:
   - A `Shape` pointer can refer to a `Circle` object.

#### Example of Polymorphism:
```cpp
int main() {
    Shape* shape = new Circle(10, 15, 5.0); // Polymorphic behavior
    shape->draw(); // Output: Drawing a Circle at (10, 15) with radius 5
    shape->move(20, 25); // Output: Moved shape to (20, 25)
    delete shape;
    return 0;
}
```

---

### **Step 4: UML Extended Example**

What if there are more shapes, like `Rectangle`?

**UML Diagram**:
```
   Shape
   + move(x: int, y: int) : void

       ▲
    --------
    |      |
 Circle  Rectangle
 + radius + width, height
 + draw() + draw()
```

**C++ Example with Multiple Derived Classes**:
```cpp
class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(int x, int y, double w, double h) : Shape(x, y), width(w), height(h) {}

    void draw() const override {
        std::cout << "Drawing a Rectangle at (" << x << ", " << y << ") with width " 
                  << width << " and height " << height << std::endl;
    }
};
```

**Usage Example:**
```cpp
int main() {
    Shape* shapes[] = {
        new Circle(10, 15, 5.0),
        new Rectangle(5, 10, 20.0, 15.0)
    };

    for (Shape* shape : shapes) {
        shape->draw(); // Calls the appropriate draw() based on the type
        delete shape;
    }

    return 0;
}
```

---

### **Summary of A "is-a" B in UML and C++**

1. **UML Representation**:
   - Inheritance is depicted as a hollow triangle pointing to the base class.
   - Derived classes specialize and extend the base class.

2. **C++ Implementation**:
   - Base class (`B`) defines shared attributes and virtual methods.
   - Derived class (`A`) extends the base class by adding specific attributes and overriding methods.

---

### **Understanding Aggregation in OOP and UML**

Aggregation is a **"has-a" relationship** in OOP that indicates a **whole-part relationship** between two classes. It represents a situation where:
- One class (the whole) contains or owns instances of another class (the parts).
- The parts can exist independently of the whole. This is the key difference from composition (where parts are strongly tied to the whole).

![aggregation](images/aggregation.png)
---

### **Key Characteristics of Aggregation**
1. **Loose Coupling**:
   - The lifetime of the parts is independent of the whole.
   - If the whole object is destroyed, the part objects may still exist.

2. **UML Representation**:
   - Depicted with a **hollow diamond** at the association end that represents the whole.

3. **Real-World Example**:
   - A `Team` has `Players`. The players can exist without the team.

---

### **Step 1: UML Example of Aggregation**

**Scenario**: 
- A `Team` has multiple `Player` objects.
- The players can exist independently (e.g., a player may leave the team but still exist).

**UML Diagram**:
```
Team <>------ Player
+ name         + name
+ addPlayer()  + play()
+ getPlayers()
```

---

### **Step 2: Aggregation in C++**

#### **Defining the Part Class (`Player`)**
The `Player` class represents individual players.

```cpp
#include <iostream>
#include <string>

class Player {
private:
    std::string name;

public:
    Player(const std::string& name) : name(name) {}

    void play() const {
        std::cout << name << " is playing!" << std::endl;
    }

    std::string getName() const {
        return name;
    }
};
```

#### **Defining the Whole Class (`Team`)**
The `Team` class contains a list of players.

```cpp
#include <vector>

class Team {
private:
    std::string name;
    std::vector<Player*> players; // Aggregation: Players are not owned by the team

public:
    Team(const std::string& name) : name(name) {}

    void addPlayer(Player* player) {
        players.push_back(player); // Add existing player to the team
    }

    void showPlayers() const {
        std::cout << "Team: " << name << " has players: " << std::endl;
        for (const auto& player : players) {
            std::cout << "- " << player->getName() << std::endl;
        }
    }
};
```

---

### **Step 3: Using Aggregation**

#### **Example Program**
```cpp
int main() {
    // Create independent players
    Player* player1 = new Player("Alice");
    Player* player2 = new Player("Bob");
    Player* player3 = new Player("Charlie");

    // Create a team
    Team team("Warriors");

    // Add players to the team
    team.addPlayer(player1);
    team.addPlayer(player2);

    // Show team players
    team.showPlayers();

    // Player can exist independently of the team
    player3->play(); // Output: Charlie is playing!

    // Cleanup
    delete player1;
    delete player2;
    delete player3;

    return 0;
}
```

---

### **Key Takeaways**
1. **Lifetime Independence**:
   - *`Player` objects are created and managed outside the `Team`.*
   - *The team holds references to the players without owning them.*

2. **Loose Coupling**:
   - *Players can exist and function outside the context of a team.*

3. **UML Notation**:
   - Hollow diamond on the `Team` end of the association line indicates aggregation.

---

### **Understanding Composition in OOP and UML**

**Composition** is another **"has-a" relationship**, but with a stronger dependency between the whole and its parts. It represents a relationship where:
- The parts **cannot exist independently** of the whole.
- The whole is responsible for the lifetime of its parts.

![compostion](images/composition.png)
---

### **Key Characteristics of Composition**
1. **Strong Coupling**:
   - If the whole object is destroyed, the parts are also destroyed.
   - The part object is owned by the whole object.

2. **UML Representation**:
   - Depicted with a **solid diamond** at the association end that represents the whole.

3. **Real-World Example**:
   - A `Car` has an `Engine`. The engine cannot exist without the car.

---

### **Step 1: UML Example of Composition**

**Scenario**: 
- A `Car` has an `Engine` and `Wheels`. The engine and wheels are integral parts of the car and cannot exist without it.

**UML Diagram**:
```
      Car
    + start()
    + stop()

      ◆
      |
    Engine
    + startEngine()
```

---

### **Step 2: Composition in C++**

#### **Defining the Part Class (`Engine`)**
The `Engine` class represents the part that is tightly coupled with the `Car`.

```cpp
#include <iostream>

class Engine {
public:
    Engine() {
        std::cout << "Engine created." << std::endl;
    }

    void startEngine() {
        std::cout << "Engine started." << std::endl;
    }

    void stopEngine() {
        std::cout << "Engine stopped." << std::endl;
    }

    ~Engine() {
        std::cout << "Engine destroyed." << std::endl;
    }
};
```

---

#### **Defining the Whole Class (`Car`)**
The `Car` class owns an `Engine` object. The engine’s lifecycle is managed by the car.

```cpp
class Car {
private:
    Engine engine; // Composition: Engine is a part of the car

public:
    Car() {
        std::cout << "Car created." << std::endl;
    }

    void start() {
        std::cout << "Car is starting..." << std::endl;
        engine.startEngine();
    }

    void stop() {
        std::cout << "Car is stopping..." << std::endl;
        engine.stopEngine();
    }

    ~Car() {
        std::cout << "Car destroyed." << std::endl;
    }
};
```

---

### **Step 3: Using Composition**

#### **Example Program**
```cpp
int main() {
    Car myCar;

    myCar.start(); // Output: Car is starting... Engine started.
    myCar.stop();  // Output: Car is stopping... Engine stopped.

    return 0;
}
```

---

### **Key Takeaways**
1. **Lifetime Dependency**:
   - The `Engine` object is created and destroyed along with the `Car` object.

2. **Ownership**:
   - The `Car` owns the `Engine`, and the `Engine` cannot exist outside the context of the `Car`.

3. **UML Notation**:
   - Solid diamond on the `Car` end of the association line indicates composition.

---

### **Step 4: Extending the Example**

#### Adding Multiple Parts (e.g., `Wheels`)
**UML Diagram**:
```
      Car
    + start()
    + stop()

      ◆
     / \
 Engine Wheels
```

**Code**:
```cpp
class Wheel {
public:
    Wheel() {
        std::cout << "Wheel created." << std::endl;
    }

    void roll() {
        std::cout << "Wheel is rolling..." << std::endl;
    }

    ~Wheel() {
        std::cout << "Wheel destroyed." << std::endl;
    }
};

class Car {
private:
    Engine engine;
    Wheel wheels[4]; // Composition: Car contains 4 wheels

public:
    Car() {
        std::cout << "Car created with 4 wheels." << std::endl;
    }

    void start() {
        std::cout << "Car is starting..." << std::endl;
        engine.startEngine();
        for (auto& wheel : wheels) {
            wheel.roll();
        }
    }

    ~Car() {
        std::cout << "Car destroyed." << std::endl;
    }
};
```

**Example Program**:
```cpp
int main() {
    Car myCar;
    myCar.start(); // Car starts and wheels roll
    return 0;
}
```

---

### **Difference Between Aggregation and Composition**
| **Feature**         | **Aggregation**                            | **Composition**                          |
|----------------------|--------------------------------------------|------------------------------------------|
| **Lifetime**         | Parts can exist independently of the whole.| Parts depend on the whole for existence. |
| **Ownership**        | Whole does not own the parts.              | Whole owns the parts.                    |
| **UML Notation**     | Hollow diamond.                           | Solid diamond.                           |

---
# Relations Between Objects

## Association
Association is a type of relationship in which one object uses or interacts(communicate) with another.

---
**UML Association. Professor communicates with students.**
![Association](images/association.png)
---
In UML diagrams the association relationship
is shown by a simple arrow drawn from an object and
pointing to the object it uses. **By the way, having a bi-directional association is a completely normal thing. In this case, the arrow has a point at each end.**