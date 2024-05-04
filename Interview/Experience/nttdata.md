1. Brief introduction about Python, RESTapi and AWS.
2. I have already built some of the APIs, I want to upgrade from 1.0 to 1.1 and I want to enhance some of the API's, I want to add one of more attribute. I have to provide backward compatibility from code point of view, when the request comes to the server how will I distinguish what version the user is making the call?
3. In a POST call, I will have to verify the req body parameters are right or not. Let's say we are creating new employee record how do we do the validation. The input is a complex resource and it will include nested structure, there are like 100s of fields how do we validate?
4. Difference between PUT and PATCH.
5. Steps to implement OAuth2 in the code. JWT is it different from Oauth.
6. How will I provide/restrict certain users to access certain APIs, how can we achieve this in Django.
7. Flatten the list - solved it using for loop and extend
``` 
[[1], [1, 2, 3], [3, 4]]
```
What are the disadvantages of using extend, is this the best optimised code for this problem.
8. How do we do Unittesting, integration testing, functional testing and UAT testing. From the unittest, how do we measure the code quality. What things do we check in code quality from code coverage. 
9. I want to support large volume of users who will call the API, currently it is supporting 100 req/s and we want to increase 1000/s, how do we do it. 
