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
1. **Technical Problem**:
    - The input file has been stored in the ``src/store`` folder.
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
      
2. **Proudest Achievement**:
   
   *Context* - In my final year of college (2017), I won Smart India Hackthon, where me and my of 5 other members worked on improving
   the approval process for technial institute by the Government of India. In the competition we worked for over 36 hours straight, and competed with 25,000+ engineering graduates from all over India.
   We built a machine-learning model and exposed the same model via single API, which can be later integrated to any government body for predictions.
    This is one my proudest achievements because of the following reasons
   - The solution was judged on the basis of scalability and best industry practices, the fact the our solution was granted the first prize
    it just shows, by hard-work and discipline as well by keeping a growth mindset, you can achieve anything.
     
   - It is my proudest achievement because this was the first-time, when I worked for something that impacts someone other than me.
    This hackathon also changed my perspective towards solving problems for the greater good.
     
   - I collaborated with my team-mates who were well-versed in skills, which I lacked. 
     As we collaborated, one **insight** I got is that how powerful team-work can be if everyone in the team has the same vision for a goal.
     Furthermore, I learnt that it's always better to ask for help from your colleagues who have the skill you lack, as it will allow you to learn from their experience.

      