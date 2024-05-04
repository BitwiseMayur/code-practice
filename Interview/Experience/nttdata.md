### Questions

1. Brief introduction about Python, REST APIs, and AWS.
2. I have already built some of the APIs. I want to upgrade from 1.0 to 1.1 and enhance some of the APIs by adding one or more attributes. How can I distinguish which version the user is calling to ensure backward compatibility?
3. In a POST call, I need to verify the request body parameters. Assuming we're creating a new employee record with a complex, nested structure and hundreds of fields, how do we validate this?
4. Difference between PUT and PATCH.
5. Steps to implement OAuth2 in the code. Is JWT different from OAuth2?
6. How can I provide or restrict certain users from accessing specific APIs in Django?
7. I solved flattening the list [[1], [1, 2, 3], [3, 4]] using a for loop and extend. What are the disadvantages of using extend, and is this the most optimized code for this problem?
8. How do we conduct unit testing, integration testing, functional testing, and UAT? From the unit tests, how do we measure code quality? What aspects of code quality are checked from code coverage?
9. I want to support a large volume of users who will call the API, currently it supports 100 req/s and we want to increase it to 1000/s, how do we do it?

### Answers

1. **Python, REST APIs, and AWS:** Python is a versatile, high-level programming language. REST APIs are architectural style for distributed hypermedia systems, which Python can utilize to manage web services. AWS (Amazon Web Services) offers cloud computing services that support applications written in languages like Python.
2. **API Versioning:** Use URI versioning (e.g., /api/v1.0/ vs /api/v1.1/) or headers to manage different API versions. This allows the server to identify and handle API requests according to their specified versions, ensuring backward compatibility.
3. **Validating Complex Structures:** Use a schema validation library like Marshmallow in Python, which allows you to define schemas and validate various fields, including nested structures.
4. **PUT vs PATCH:** PUT is used to replace an entire resource. PATCH is used for making partial updates to a resource.
5. **Implementing OAuth2 and JWT:** OAuth2 is an authorization framework that enables applications to obtain limited access to user accounts. JWT (JSON Web Tokens) can be used as a type of token in OAuth2 but is specifically designed for securely transmitting information between parties as JSON objects.
6. **Access Control in Django:** Use Django’s built-in authentication and permission classes or third-party packages like `django-guardian` to manage user access to APIs.
7. **Flatten List with Extend:** While `extend` efficiently appends elements to the list, it can be suboptimal for very large lists due to potential high memory usage and reallocation overhead. Consider using itertools.chain() or List comprehension for a more optimized solution.
8. **Testing and Code Quality:** 
   - **Unit Testing:** Focus on testing individual components for expected functionality.
   - **Integration Testing:** Ensures that combined parts of the application work together.
   - **Functional and UAT Testing:** Validates the software against functional requirements and user acceptance criteria, respectively.
   - **Code Quality:** Analyze unit test coverage to ensure significant portions of your code are tested, which helps maintain high standards.
9. **Scaling to 1000 Requests/Second:** Optimize application performance, utilize efficient coding practices, implement caching, use a load balancer, and possibly scale horizontally by adding more servers.

