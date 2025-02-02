/*
Japanese Cities' Name

Query the the names of all the Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

Input Format

The CITY table is described as follows:

+-------------+---------------+
| Field       | Type          |
+-------------+---------------+
| ID          | NUMBER        |
| Name        | VARCHAR2 (17) |
| CountryCode | VARCHAR2 (3)  |
| District    | VARCHAR2 (20) |
| Population  | NUMBER        |
+-------------+---------------+
*/

SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';