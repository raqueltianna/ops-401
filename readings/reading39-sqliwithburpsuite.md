# Reading 39: SQLi with Burp Suite, WebGoat

### Article Links: 
- [Understanding SQL Injection, Identification and Prevention](https://www.varonis.com/blog/sql-injection-identification-and-prevention-part-1/)

### What is SQL injection? 
- SQL injection is a cyber attack where malicious SQL code is put into fields of a web application and it used to exploit vulnerabilities in the application's code to manipulate the database, steal data, and other malicious actions.

### Can you give an example of how a hacker could use SQL injection to gain unauthorized access?
- An example of how the hacker could use SQL injection is let's say an application uses SQL to check username and password that the user entered. A hacker can manipulate the fields by entering a SQL code instead of the username or password. This would make the query return true which allows the hacker to bypass and gain access as an administrator without need the right credentials.

### What are some ways to prevent SQL injection attacks on a web server? 
-  Some ways to prevent an SQL injection attack are: 
    - You can implement input validation and sanitize user input to remove malicious characters.
    - Use least privilege principle for users, only giving them the needed permissions. 
    - Update and patch web applications frequently to fix known vulnerabilities. 
    - Use web application firewalls to filter and block suspicious requests. 