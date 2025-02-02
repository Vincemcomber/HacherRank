/*
Japanese Cities Attributes:

Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

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

SELECT * FROM City WHERE CountryCode="JPN";