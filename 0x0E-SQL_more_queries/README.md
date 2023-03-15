# 0x0E. SQL - More queries
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
How to create a new MySQL user   
How to manage privileges for a user to a database or table   
What’s a PRIMARY KEY   
What’s a FOREIGN KEY   
How to use NOT NULL and UNIQUE constraints    
How to retrieve datas from multiple tables in one request   
What are subqueries    
What are JOIN and UNION     
### More Info
Comments for your SQL file:  
`$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$`     

#### Install MySQL 8.0 on Ubuntu 20.04 LTS  

`$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$`
