1. Use Clear naming
   Use simple and clear names and avoid 'get' keyword
   https://mayur.com/api/v1/getproduct/123 - Not a good example
   https://mayur.com/api/v1/products -> To get the products list
   https://mayur.com/api/v1/products/123 -> To get specific product

2. Ensure reliability through idempotent APIs
   idempotent -> Making the call multiple times will have the same response
   Handle the API retry mechanism, usually the POST apis are not idempotent in nature, sending the same request again might create duplicate entries. Handled by generating the Unique ID for      every request.
   GET - Idempotent by default
   PUT - which updates full resource is also idempotent request
   PATCH - Idempotent
   DELETE - Idempotent

3. Add versioning
   https://mayur.com/api/v1/products/123
   https://mayur.com/api/v2/products/123
   Backward compatibility - With time the APIs need to be updated, by using versioning we make sure the existing APIs are supported along with the new features

4. Add Pagination
   Controls the data need to be retrivied by the API. Two common approaches are Page + Offset and cursor based.
   a. Page + Offset, Suppose there are 1000 values present, let's say we set the offset as 50, so for Page 1 the values 1-50 are retrivied and for next page 51-100 are retrivied.
   b. Cursor based - Used mainly for large data sets
   Either ways improve user experience and performance

5. Use clear query strings for sorting and filtering data
   Sort by last login, use GET/users/?sortby=lastlogin
   Filter users based out of city GET/users/?filter=location:bengaluru

6. Security
   For sensitive credentials use HTTP Headers rather than URL
   Access control - Verify keys or tokens on every request

7. Keep cross-resource references simple
   https://mayur.com/api/v2/products/123/items/321 - Good practice
   https://mayur.com/api/v2/products/?product_id=123&item_id=321 - Not so good practice
   
   
   
