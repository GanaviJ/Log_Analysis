# Log_Analysis
Queries to extract data from the database.

### Description
This is a project to extract particular information such as <br>
* identifying authors of the popular artices
* popular articles of all time
* which days had more than 1% error requests
from the real world data.

### Installation
1.Install [Virtual Box](https://www.virtualbox.org/)
2.Install [Vagrant](https://www.vagrantup.com/)
3.Download or Clone the [repository](https://github.com/udacity/fullstack-nanodegree-vm)
4.You now have newsdata.sql with which u can work.

### How to run<br>
1. Change to the directory containing vagrant file<br>
2. run **vagrant up** to start<br>
3. **vagrant ssh** to login into vm<br>
4. change directory to vagrant **cd /**<br>
5. use command **psql -d news -f newsdata.sql** to load database<br>
    -use **\c** to connect to database="news"<br>
    -use **\dt** to see the tables in database<br>
    -use **\dv** to see the views in database<br>
    -use **\q** to quit the database<br>
6. use command **python log.py** to run the programm<br>

## Views
#### article_view
```
  CREATE VIEW article_view AS
  SELECT path AS article,count(path) AS views
  FROM log
  WHERE status='200 OK' and path!='/'
  GROUP BY path
  ORDER BY count(path) desc
  LIMIT 3;
``` 
#### newslug_view
```
CREATE VIEW  newslug_view AS 
SELECT id,('/article/'|| slug) AS newslug,author
FROM articles;
```
#### count_view
```
CREATE VIEW count_view AS
SELECT path,count(path) AS tot 
FROM log 
WHERE status='200 OK' and path!='/' 
GROUP BY path;
```
#### join_view
```
CREATE VIEW join_view AS
SELECT tot,path,newslug,author
FROM newslug_view nv,count_view cv 
WHERE cv.path=nv.newslug;
```
#### total_view
```
CREATE VIEW total_view AS 
SELECT tot,author,name 
FROM join_view jv,authors 
WHERE authors.id=jv.author;
```
#### failure_count
```
CREATE VIEW failure_count AS 
SELECT date(time) AS dat,cast(count(*) AS  decimal(10,4)) AS  countfailure 
FROM log
WHERE status!='200 OK' 
GROUP BY date(time);
```
#### total_cunt
```
CREATE VIEW total_count AS 
SELECT date(time) AS  dat,cast(count(*) AS decimal(10,4)) AS  countfull 
FROM log 
GROUP BY date(time);
```
#### error_percentage
```
CREATE VIEW error_percentage AS
SELECT to_char(failure_count.dat,'Mon DD,YYYY') AS date,cast((countfailure*100)/countfull AS decimal(10,4)) as error 
FROM failure_count ,total_count 
WHERE failure_count.dat=total_count.dat;
```
    
