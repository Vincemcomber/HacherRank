/*
Select by ID
============
Given a City table, whose fields are described as

+-------------+--------------+
| Field       | Type         |
+-------------+--------------+
| ID          | NUMBER       |
| Name        | VARCHAR2 (17)|
| CountryCode | VARCHAR2 (3) |
| District    | VARCHAR2 (20)|
| Population  | int(11)      |
+-------------+--------------+

you have to print all the details of the city with ID is 1661.
*/

SELECT * FROM City WHERE ID=1661;