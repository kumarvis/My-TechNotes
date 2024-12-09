# INTRODUCTION TO PATTERNS

## What’s a Design Pattern ?
Design patterns are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

## Classification of patterns

### **Creational patterns**
Creational patterns provide object creation mechanisms that increase flexibility and reuse of existing code.

*Creational design patterns enhance flexibility and promote reuse by offering mechanisms for object creation. Let me explain with a real-world scenario, using the **Factory Method** pattern, which is one of the creational design patterns discussed in the book.*

### Real-World Scenario: Logistics Management System

Imagine you are developing a logistics application. Your app initially supports only road transportation, and you create a `Truck` class to represent it. Over time, new requirements emerge to handle sea transportation, introducing a `Ship` class. Directly modifying the code every time a new transportation type is added would make it rigid and error-prone.

#### Problem
If every time you add a new transport type (e.g., `Ship`, `Airplane`), you must modify existing code, you risk breaking functionality. This tightly couples the client code (that uses transport objects) to specific classes.

#### Solution: Factory Method Pattern
The Factory Method pattern introduces a **factory method** that encapsulates the creation logic of the transport objects. Instead of instantiating `Truck` or `Ship` directly, you define an interface `Transport` with a method `deliver`. Both `Truck` and `Ship` implement this interface.

You then create abstract `Logistics` and concrete subclasses like `RoadLogistics` and `SeaLogistics`, each implementing a factory method that returns a specific `Transport` object.
Here’s the example using **Factory Method** in C++ for a logistics management system:

### Implementation in C++

1. **Transport Interface**:
   ```cpp
   #include <iostream>
   #include <memory>

   class Transport {
   public:
       virtual void deliver() const = 0;
       virtual ~Transport() = default;
   };

   class Truck : public Transport {
   public:
       void deliver() const override {
           std::cout << "Deliver by land using a truck." << std::endl;
       }
   };

   class Ship : public Transport {
   public:
       void deliver() const override {
           std::cout << "Deliver by sea using a ship." << std::endl;
       }
   };
   ```

2. **Creator Class**:
   ```cpp
   class Logistics {
   public:
       virtual std::unique_ptr<Transport> createTransport() const = 0;
       virtual ~Logistics() = default;
   };

   class RoadLogistics : public Logistics {
   public:
       std::unique_ptr<Transport> createTransport() const override {
           return std::make_unique<Truck>();
       }
   };

   class SeaLogistics : public Logistics {
   public:
       std::unique_ptr<Transport> createTransport() const override {
           return std::make_unique<Ship>();
       }
   };
   ```

3. **Client Code**:
   ```cpp
   int main() {
       std::unique_ptr<Logistics> logistics;

       // Using Road Logistics
       logistics = std::make_unique<RoadLogistics>();
       auto transport = logistics->createTransport();
       transport->deliver();

       // Using Sea Logistics
       logistics = std::make_unique<SeaLogistics>();
       transport = logistics->createTransport();
       transport->deliver();

       return 0;
   }
   ```

### Explanation
- **Transport Interface**: Defines the common behavior for all transport types (`deliver()` method).
- **Truck** and **Ship**: Implement the `Transport` interface.
- **Logistics**: An abstract class that declares the `createTransport()` factory method.
- **RoadLogistics** and **SeaLogistics**: Concrete subclasses that override `createTransport()` to return specific transport types.
- **Client Code**: Works only with the `Logistics` interface and uses the factory method to get transport objects, ensuring decoupling from concrete implementations.

This C++ implementation provides flexibility and adheres to the Factory Method pattern principles.

### **Structural patterns**
Structural patterns explain how to assemble objects and classes
into larger structures, while keeping the structures flexible
and efficient.

Structural design patterns focus on composing classes and objects into larger structures while keeping them flexible and efficient. A good example is the **Adapter Pattern**, which allows classes with incompatible interfaces to work together.

### Real-World Scenario: Power Plug Adapter
Imagine you're developing a system for a travel agency. Different countries have different power socket types. A traveler brings a `USPlugDevice`, but the power socket in Europe requires a `EuropeanPlug`. Instead of modifying the `USPlugDevice` or `EuropeanPlug`, you use an adapter to bridge the two.

---

### Implementation in C++

1. **Target Interface**:
   ```cpp
   #include <iostream>
   #include <memory>

   // Target Interface
   class EuropeanPlug {
   public:
       virtual void connect() const = 0;
       virtual ~EuropeanPlug() = default;
   };

   class EuropeanSocket : public EuropeanPlug {
   public:
       void connect() const override {
           std::cout << "Connecting to a European socket." << std::endl;
       }
   };
   ```

2. **Adaptee**:
   ```cpp
   // Adaptee with an incompatible interface
   class USPlugDevice {
   public:
       void connectToUSPlug() const {
           std::cout << "Connecting to a US plug." << std::endl;
       }
   };
   ```

3. **Adapter**:
   ```cpp
   // Adapter makes USPlugDevice compatible with EuropeanPlug
   class USPlugAdapter : public EuropeanPlug {
   private:
       std::shared_ptr<USPlugDevice> usPlugDevice;

   public:
       explicit USPlugAdapter(std::shared_ptr<USPlugDevice> device)
           : usPlugDevice(std::move(device)) {}

       void connect() const override {
           std::cout << "Adapting from US plug to European socket..." << std::endl;
           usPlugDevice->connectToUSPlug();
       }
   };
   ```

4. **Client Code**:
   ```cpp
   int main() {
       // European device directly connects
       std::shared_ptr<EuropeanPlug> europeanSocket = std::make_shared<EuropeanSocket>();
       europeanSocket->connect();

       // US device needs an adapter
       std::shared_ptr<USPlugDevice> usDevice = std::make_shared<USPlugDevice>();
       std::shared_ptr<EuropeanPlug> adapter = std::make_shared<USPlugAdapter>(usDevice);

       adapter->connect();

       return 0;
   }
   ```

---

### Explanation

1. **Target Interface (`EuropeanPlug`)**:
   - Represents the expected interface for devices that can connect to European sockets.

2. **Adaptee (`USPlugDevice`)**:
   - A class with a specific interface that cannot directly connect to the European socket.

3. **Adapter (`USPlugAdapter`)**:
   - A class that wraps the `USPlugDevice` and translates the calls to the `EuropeanPlug` interface.

4. **Client Code**:
   - Works only with the `EuropeanPlug` interface and is unaware of the `USPlugDevice`'s incompatibility.

---

### Benefits
1. **Flexibility**:
   - Allows existing code to work with new or incompatible classes without modifying them.

2. **Reusability**:
   - Reuses existing classes even if their interfaces are incompatible.

3. **Decoupling**:
   - The client code depends on the abstract `EuropeanPlug` interface, not on the specific `USPlugDevice`.

This example demonstrates how the **Adapter Pattern** can help assemble objects with incompatible interfaces into a flexible structure. Other structural patterns like **Decorator**, **Bridge**, and **Composite** offer similar flexibility for different scenarios. Let me know if you'd like to explore another structural pattern!

## **Behavioral patterns**
Behavioral patterns take care of effective communication and
the assignment of responsibilities between objects.

Behavioral design patterns focus on managing object collaboration and delegation of responsibilities. A classic example is the **Observer Pattern**, which allows an object (the "subject") to notify multiple dependent objects (the "observers") of any state changes.

---

### Real-World Scenario: Weather Monitoring System
Imagine you are building a weather monitoring system. The system gathers weather data and needs to notify multiple displays (e.g., temperature display, humidity display) whenever the data changes. Instead of tightly coupling the displays to the weather station, you can use the Observer Pattern.

---

### Implementation in C++

1. **Subject Interface**:
   ```cpp
   #include <iostream>
   #include <vector>
   #include <memory>
   #include <string>

   // Observer interface
   class Observer {
   public:
       virtual void update(float temperature, float humidity) = 0;
       virtual ~Observer() = default;
   };

   // Subject interface
   class Subject {
   public:
       virtual void attach(std::shared_ptr<Observer> observer) = 0;
       virtual void detach(std::shared_ptr<Observer> observer) = 0;
       virtual void notify() = 0;
       virtual ~Subject() = default;
   };
   ```

2. **Concrete Subject (WeatherStation)**:
   ```cpp
   class WeatherStation : public Subject {
   private:
       std::vector<std::shared_ptr<Observer>> observers;
       float temperature;
       float humidity;

   public:
       void setWeatherData(float temp, float hum) {
           temperature = temp;
           humidity = hum;
           notify();
       }

       void attach(std::shared_ptr<Observer> observer) override {
           observers.push_back(observer);
       }

       void detach(std::shared_ptr<Observer> observer) override {
           observers.erase(std::remove(observers.begin(), observers.end(), observer), observers.end());
       }

       void notify() override {
           for (const auto& observer : observers) {
               observer->update(temperature, humidity);
           }
       }
   };
   ```

3. **Concrete Observers (Displays)**:
   ```cpp
   class TemperatureDisplay : public Observer {
   public:
       void update(float temperature, float humidity) override {
           std::cout << "Temperature Display: Current temperature is " << temperature << "°C." << std::endl;
       }
   };

   class HumidityDisplay : public Observer {
   public:
       void update(float temperature, float humidity) override {
           std::cout << "Humidity Display: Current humidity is " << humidity << "%." << std::endl;
       }
   };
   ```

4. **Client Code**:
   ```cpp
   int main() {
       std::shared_ptr<WeatherStation> weatherStation = std::make_shared<WeatherStation>();

       std::shared_ptr<Observer> tempDisplay = std::make_shared<TemperatureDisplay>();
       std::shared_ptr<Observer> humDisplay = std::make_shared<HumidityDisplay>();

       // Attach observers to the weather station
       weatherStation->attach(tempDisplay);
       weatherStation->attach(humDisplay);

       // Update weather data
       weatherStation->setWeatherData(25.5f, 60.0f);
       weatherStation->setWeatherData(28.0f, 55.0f);

       // Detach an observer
       weatherStation->detach(tempDisplay);

       // Update weather data again
       weatherStation->setWeatherData(22.0f, 70.0f);

       return 0;
   }
   ```

---

### Explanation

1. **Subject Interface (`Subject`)**:
   - Declares methods for attaching, detaching, and notifying observers.

2. **Observer Interface (`Observer`)**:
   - Defines the `update()` method that all concrete observers must implement to receive notifications.

3. **Concrete Subject (`WeatherStation`)**:
   - Maintains a list of observers and notifies them when weather data changes.

4. **Concrete Observers (`TemperatureDisplay`, `HumidityDisplay`)**:
   - Implement the `update()` method to respond to state changes in the subject.

5. **Client Code**:
   - Creates the subject and observers, attaches observers to the subject, and updates the subject’s state.

---

### Benefits
1. **Loose Coupling**:
   - Observers and subjects are decoupled. Adding or removing observers does not affect the subject.

2. **Dynamic Behavior**:
   - Observers can be dynamically added, removed, or changed at runtime.

3. **Scalability**:
   - Multiple observers can monitor the same subject without interfering with each other.

This example demonstrates the **Observer Pattern** and how it facilitates communication between objects while maintaining flexibility. Let me know if you'd like an example of another behavioral pattern, such as **Strategy**, **Command**, or **State**!