Intercom Code Challenge
=======================

### Technical problem

The code challenge has 2 parts:

1. Technical Problem - We have some customer records in a text file (customers.txt) -- one customer per line, JSON
lines formatted. We want to invite any customer within 100km of our Dublin office for some food
and drinks on us. 
Write a program that will read the full list of customers and output the names
and user ids of matching customers (within 100km), sorted by User ID (ascending).
    - You must use the first formula from this [Wikipedia](https://en.wikipedia.org/wiki/Great-circle_distance) article to calculate distance. Don't
forget, you'll need to convert degrees to radians.
    - The GPS coordinates for our Dublin office are *53.339428, -6.257664*.
    - You can find the Customer list [here](https://s3.amazonaws.com/intercom-take-home-test/customers.txt).


2. Proudest Achievement - What's your proudest achievement? It can be a personal project or something you've worked on professionally. Just a short paragraph is fine, but I'd love to know why you're proud of it, what impact it had (If any) and any insights you took from it. 


### Solution
1. Technical Problem:
    - The input file has been stored in the ``store`` folder.
    - Added docker integration for better usage and portability.
    - Add tests
        - Unit Tests
        - Integration Tests
    
    - Used type hint for reducing type mistakes

    #### Requirements
    * Docker
    * Python 3.8.x
    * Tox 3.2.x
        
      ##### How to run the program

        ```bash
           $ make build
           $ make run
        ```
      #### How to run tests
    
        ``` bash
        $ make test
        ```

      