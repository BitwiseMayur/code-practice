### Questions

1. What kind of work have you done in Python?
2. Did you use Django templates, and what are they?
3. Do you have any exposure to GraphQL technology? Do you know the concepts?
4. Have you ever worked on multithreading in Python? Does Python support true multithreading? What are the requirements for using multithreading?
5. Do you know the MRO concept in Python?
6. What are class methods, instance methods, and static methods? What is the use of static methods? Which of these methods will be available in the child class?
7. How can we achieve commit and rollback using ORM in SQLAlchemy or Django ORM?
8. How can we use different joins in Django ORM?
9. What are decorators, and how do we use them?
10. Write a program to swap two numbers without using a third variable.
11. What have you used for testing, pytest or unittest?
12. What all cloud services have you used?
13. Any exposure to CI/CD implementation?
14. Any exposure to HTML, CSS, and JavaScript?

### Answers

1. **Python Work:** I've developed web applications using Flask and Django, automated data processing scripts, and REST APIs. My work primarily focuses on backend development, data manipulation, and process automation.
2. **Django Templates:** Yes, I've used them. Django templates are a templating engine that allows Python-like expressions for creating dynamic HTML web pages. They are used to separate the presentation layer from business logic.
3. **GraphQL Exposure:** I have basic knowledge of GraphQL, which is a data query language that allows clients to request exactly the data they need, making it more efficient than traditional REST APIs.
4. **Multithreading in Python:** Python's multithreading is somewhat limited by the Global Interpreter Lock (GIL), which allows only one thread to execute at a time. However, it can be useful for I/O-bound tasks.
5. **MRO in Python:** MRO, or Method Resolution Order, is the order in which Python looks for a method in a hierarchy of classes. It uses the C3 linearization algorithm.
6. **Methods in Python:**
   - **Class Methods:** Methods that are bound to the class and not the instance of the class. They can modify the class state.
   - **Instance Methods:** Regular methods that are bound to object instances, accessible through the instance.
   - **Static Methods:** Methods that don't operate on an instance or the class but belong to the class's namespace. Static methods are used when some processing is related to the class, but not in an instance-specific way.
   - All these methods are inherited by the child class.
7. **Commit and Rollback in ORM:** Use the session object in SQLAlchemy or the transaction module in Django ORM. For instance, with Django ORM:
   ```python
   from django.db import transaction

   try:
       with transaction.atomic():
           # perform create, update, delete
           pass
   except Exception as e:
       # Handle exception
       pass
8. **Joins in Django ORM:** Django ORM supports different types of joins using its relationship fields. Use `select_related` for SQL JOINs on single-valued relationships, and `prefetch_related` for "manual" joins on many-to-many and other multi-valued relationships. This optimizes query performance by reducing the number of database hits.
9. **Decorators:** Decorators are functions that modify the behavior of another function. They are used extensively in Flask and Django for registering routes, views, and for middleware. Example:
   ```python
   def my_decorator(func):
       def wrapper(*args, **kwargs):
           print("Something is happening before the function is called.")
           result = func(*args, **kwargs)
           print("Something is happening after the function is called.")
           return result
       return wrapper

   @my_decorator
   def say_hello():
       print("Hello!")
10. **Swap Two Numbers:**
    ```python
    a = 5
    b = 10
    a = a + b
    b = a - b
    a = a - b
    print(f"a = {a}, b = {b}")
    ```
11. **Testing Tools:** I have used both pytest and unittest depending on the project requirements. Pytest is preferred for its more powerful fixtures and more flexible, expressive syntax for writing tests. Unittest is used when a more traditional, xUnit-based framework is preferred.

12. **Cloud Services:** I have worked with AWS utilizing services such as EC2, S3, RDS, EMR, Lambda and Batch.

13. **CI/CD Implementation:** I have experience implementing CI/CD pipelines using Jenkins, GitHub Actions, and GitLab CI. These tools automate the software release process, from code integration, testing, to deployment, ensuring consistent and reliable delivery of applications.

14. **HTML, CSS, and JavaScript:** Yes, I have substantial experience in web development with HTML, CSS, and JavaScript. I have used HTML for structuring web content, CSS for styling, and JavaScript for adding interactivity and handling events on web pages.
