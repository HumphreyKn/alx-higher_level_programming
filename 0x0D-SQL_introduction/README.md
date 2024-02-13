# Introduction To Relational Database


## What’s a database

A database is an organized collection of data or information that is specially structured for rapid search and retrieval by a computer. Databases are structured to facilitate the storage, modification, and deletion of data in conjunction with various data-processing operations. ¹

## What’s a relational database

A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points. ²

## What does SQL stand for

SQL stands for Structured Query Language, an international standard for database manipulation. SQL is a programming language used by nearly all relational databases to query, manipulate, and define data, and to provide access control. SQL was first developed at IBM in the 1970s with Oracle as a major contributor, which led to implementation of the SQL ANSI standard. ³

## What’s MySQL

MySQL is the world’s most popular open source database. According to DB-Engines, MySQL ranks as the second-most-popular database, behind Oracle Database. MySQL powers many of the most accessed applications, including Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com. Since MySQL is open source, it includes numerous features developed in close cooperation with users over more than 25 years. It supports various programming languages, platforms, and offers high performance, reliability, scalability, security, and flexibility. ⁴

## How to create a database in MySQL

To create a new database in MySQL, you use the CREATE DATABASE statement. The following illustrates the basic syntax of the CREATE DATABASE statement:

```sql
CREATE DATABASE [IF NOT EXISTS] database_name
[CHARACTER SET charset_name]
[COLLATE collation_name];
```

In this syntax:

- First, specify the name of the database after the CREATE DATABASE keywords. The database name must be unique within a MySQL server instance. If you attempt to create a database with an existing name, MySQL will issue an error.
- Second, use the IF NOT EXISTS option to create a database if it doesn’t exist conditionally.
- Third, specify the character set and collation for the new database. If you skip the CHARACTER SET and COLLATE clauses, MySQL will use the default character set and collation for the new database.

For example, the following statement creates a database named testdb with the UTF-8 character set and the utf8_general_ci collation:

```sql
CREATE DATABASE testdb
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

To verify the database creation, you can use the SHOW DATABASES command to list all databases on the server:

```sql
SHOW DATABASES;
```

## What does DDL and DML stand for

DDL stands for Data Definition Language, which is a subset of SQL that is used to define the structure and organization of the data, such as creating, altering, or dropping tables, views, indexes, or constraints. ⁵

DML stands for Data Manipulation Language, which is another subset of SQL that is used to insert, update, delete, or query data from the tables. ⁶

## How to CREATE or ALTER a table

To create a new table in MySQL, you use the CREATE TABLE statement. The following shows the basic syntax of the CREATE TABLE statement:

```sql
CREATE TABLE [IF NOT EXISTS] table_name (
    column_1_definition,
    column_2_definition,
    ...,
    table_constraints
) ENGINE=storage_engine;
```

In this syntax:

- First, specify the name of the table that you want to create after the CREATE TABLE keywords. The name of the table must be unique within a database. If you create a new table using an existing table, the new table will be filled with the existing values from the old table.
- Second, use IF NOT EXISTS option to conditionally create a new table only if it does not exist.
- Third, specify a comma-separated list of column definitions, each of which consists of a column name, a data type, and optional column constraints. You can also specify table constraints that apply to the entire table.
- Fourth, specify the storage engine for the table in the ENGINE clause. The default storage engine is InnoDB.

For example, the following statement creates a table named customers with four columns: customer_id, name, email, and phone:

```sql
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    phone VARCHAR(15)
) ENGINE=InnoDB;
```

To modify an existing table in MySQL, you use the ALTER TABLE statement. The following shows the basic syntax of the ALTER TABLE statement:

```sql
ALTER TABLE table_name
action1,
action2,
...
action_n;
```

In this syntax:

- First, specify the name of the table that you want to change after the ALTER TABLE keywords.
- Second, specify the changes or actions that you want to perform. You can add, delete, or modify columns, indexes, or constraints. You can also change the table options such as the storage engine, character set, or comment.

For example, the following statement adds a new column named address to the customers table:

```sql
ALTER TABLE customers
ADD COLUMN address VARCHAR(100);
```

## How to SELECT data from a table

To select data from a table in MySQL, you use the SELECT statement. The following shows the basic syntax of the SELECT statement:

```sql
SELECT select_list
FROM table_name
WHERE search_condition
GROUP BY group_by_list
HAVING search_condition
ORDER BY order_list
LIMIT row_limit;
```

In this syntax:

- First, specify a comma-separated list of columns that you want to select after the SELECT keyword. You can use the asterisk (*) to select all columns from the table.
- Second, specify the name of the table from which you want to query data after the FROM keyword.
- Third, optionally, apply a condition to filter rows returned from the table after the WHERE keyword.
- Fourth, optionally, group rows into groups after the GROUP BY clause and apply a filter to each group using the HAVING clause.
- Fifth, optionally, sort the rows in the result set using the ORDER BY clause.
- Sixth, optionally, limit the number of rows returned from the query using the LIMIT clause.

For example, the following statement selects the name and email columns from the customers table:

```sql
SELECT name, email
FROM customers;
```

## How to INSERT, UPDATE or DELETE data

To insert data into a table in MySQL, you use the INSERT statement. The following shows the basic syntax of the INSERT statement:

```sql
INSERT INTO table_name(column_1,column_2,...)
VALUES(value_1,value_2,...);
```

In this syntax:

- First, specify the name of the table that you want to insert data after the INSERT INTO keywords.
- Second, specify a comma-separated list of columns in the table surrounded by parentheses.
- Third, specify a comma-separated list of values that correspond to the columns surrounded by parentheses. Each value must have the same data type as the corresponding column.

For example, the following statement inserts a new row into the customers table:

```sql
INSERT INTO customers(name,email,phone)
VALUES('John Doe','john.doe@example.com','1234567890');
```

To update data in a table in MySQL, you use the UPDATE statement. The following shows the basic syntax of the UPDATE statement:

```sql
UPDATE table_name
SET column_1 = value_1,
    column_2 = value_2,
    ...
WHERE search_condition;
```

In this syntax:

- First, specify the name of the table that you want to update data after the UPDATE keyword.
- Second, specify a comma-separated list of column assignments after the SET keyword. Each assignment sets the new value for a column.
- Third, optionally, specify a condition to filter rows that you want to update after the WHERE keyword.

For example, the following statement updates the email and phone columns of the customer whose id is 1:

```sql
UPDATE customers
SET email = 'jane.doe@example.com',
    phone = '0987654321'
WHERE customer_id = 1;
```

To delete data from a table in MySQL, you use the DELETE statement. The following shows the basic syntax of the DELETE statement:

```sql
DELETE FROM table_name
WHERE search_condition;
```

In this syntax:

- First, specify the name of the table from which you want to delete data after the DELETE FROM keywords.
- Second, optionally, specify a condition to filter rows that you want to delete after the WHERE keyword.

For example, the following statement deletes the customer whose id is 1:

```sql
DELETE FROM customers
WHERE customer_id = 1;
```

## What are subqueries

A subquery is a query nested within another query such as SELECT, INSERT, UPDATE, or DELETE. A subquery can be used anywhere that an expression is used and must be enclosed in parentheses. A subquery can return a single value, a single row, a single column, or a table. ⁷


## How to use MySQL functions

MySQL provides various kinds of functions that perform different operations on data. Some of the common types of functions are:

- String functions: these functions manipulate and process strings, such as CONCAT, LENGTH, SUBSTRING, REPLACE, etc.
- Numeric functions: these functions perform calculations and return numeric values, such as ABS, AVG, CEIL, COS, etc.
- Date and time functions: these functions handle date and time values, such as CURDATE, DATE_FORMAT, DATEDIFF, NOW, etc.
- Full-text search functions: these functions perform full-text search operations on text-based data, such as MATCH, AGAINST, etc.
- Cast functions and operators: these functions and operators convert values from one data type to another, such as CAST, CONVERT, BINARY, etc.
- XML functions: these functions extract and update XML data, such as ExtractValue, UpdateXML, etc.
- Bit functions and operators: these functions and operators manipulate bit values, such as BIT_COUNT, BIT_AND, BIT_OR, etc.
- Encryption and compression functions: these functions encrypt, decrypt, and compress data, such as AES_ENCRYPT, AES_DECRYPT, COMPRESS, UNCOMPRESS, etc.
- Locking functions: these functions manage locks on tables, such as GET_LOCK, RELEASE_LOCK, IS_FREE_LOCK, etc.
- Information functions: these functions return information about the server, database, user, or session, such as DATABASE, USER, VERSION, LAST_INSERT_ID, etc.
- Spatial analysis functions: these functions perform spatial operations on geometry values, such as ST_Distance, ST_Contains, ST_Intersects, etc.
- JSON functions: these functions create, modify, and query JSON data, such as JSON_ARRAY, JSON_OBJECT, JSON_EXTRACT, JSON_SET, etc.
- Replication functions: these functions return information about the replication status, such as MASTER_POS_WAIT, GTID_SUBSET, etc.
- Aggregate functions: these functions return a single value from a set of values, such as SUM, MIN, MAX, COUNT, etc.
- Window functions: these functions perform calculations over a set of rows related to the current row, such as ROW_NUMBER, RANK, LAG, LEAD, etc.
- Performance schema functions: these functions return information from the performance schema tables, such as sys.ps_is_account_enabled, sys.ps_is_thread_instrumented, etc.
- Internal functions: these functions are used internally by the server and are not intended for general use, such as GREATEST, LEAST, etc.
- Miscellaneous functions: these functions perform various tasks that do not fit into any of the above categories, such as BENCHMARK, COALESCE, IFNULL, UUID, etc.

To use a MySQL function, you need to follow the syntax of the function, which usually consists of the function name followed by a list of arguments enclosed in parentheses. For example, the syntax of the CONCAT function is:

```sql
CONCAT(string1,string2,...)
```

This function returns a string that is the result of concatenating two or more string arguments. For example:

```sql
SELECT CONCAT('Hello', ' ', 'World');
-> 'Hello World'
```

Some functions may have optional arguments, which are indicated by square brackets in the syntax. For example, the syntax of the DATE_FORMAT function is:

```sql
DATE_FORMAT(date,format[,locale])
```

This function returns a string that represents the date value formatted according to the format string. The optional locale argument can be used to specify a locale for the output. For example:

```sql
SELECT DATE_FORMAT('2024-02-12', '%W, %M %e, %Y');
-> 'Monday, February 12, 2024'
```

Some functions may have no arguments at all, in which case you still need to use the parentheses. For example, the syntax of the NOW function is:

```sql
NOW()
```

This function returns the current date and time. For example:

```sql
SELECT NOW();
-> '2024-02-12 11:37:18'
```

You can find more information and examples for each function in the [MySQL documentation](^2^)..

Source:
(1) . https://bing.com/search?q=relational+database+definition.
(2) What is a relational database? | IBM. https://www.ibm.com/topics/relational-databases.
(3) What Is a Relational Database | Oracle. https://www.oracle.com/database/what-is-a-relational-database/.
(4) Relational Database: Definition, Examples, and More | Coursera. https://www.coursera.org/articles/relational-database.
(5) What Is a Relational Database? - phoenixNAP. https://phoenixnap.com/kb/what-is-a-relational-database.
(6) What is a relational database? - azure.microsoft.com. https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-relational-database/.
(7) . https://bing.com/search?q=SQL+definition.
(8) SQL - Wikipedia. https://en.wikipedia.org/wiki/SQL.
(9) What is SQL? - GeeksforGeeks. https://www.geeksforgeeks.org/what-is-sql/.
(10) SQL - Overview - Online Tutorials Library. https://www.tutorialspoint.com/sql/sql-overview.htm.
(11) SQL Tutorial - GeeksforGeeks. https://www.geeksforgeeks.org/sql-tutorial/.
(12) . https://bing.com/search?q=database+definition.
(13) What Is a Database | Oracle. https://www.oracle.com/database/what-is-database/.
(14) Database - Wikipedia. https://en.wikipedia.org/wiki/Database.
(15) Database | Definition, Types, & Facts | Britannica. https://www.britannica.com/technology/database.
(16) What Is MySQL? | Oracle. https://www.oracle.com/mysql/what-is-mysql/.
(17) MySQL - Wikipedia. https://en.wikipedia.org/wiki/MySQL.
(18) What is MySQL? | DigitalOcean. https://www.digitalocean.com/community/tutorials/what-is-mysql.
(19) MySQL CREATE DATABASE - Creating a New Database in MySQL - MySQL Tutorial. https://www.mysqltutorial.org/mysql-basics/mysql-create-database/.
(20) MySQL CREATE DATABASE Statement - W3Schools. https://www.w3schools.com/mysql/mysql_create_db.asp.
(21) MySQL :: Getting Started with MySQL. https://dev.mysql.com/doc/mysql-getting-started/en/.
(22) Difference Between DDL and DML in DBMS - GeeksforGeeks. https://www.geeksforgeeks.org/difference-between-ddl-and-dml-in-dbms/.
(23) sql - What are DDL and DML? - Stack Overflow. https://stackoverflow.com/questions/2578194/what-are-ddl-and-dml.
(24) Difference between DDL and DML in DBMS - Online Tutorials Library. https://www.tutorialspoint.com/difference-between-ddl-and-dml-in-dbms.
(25) Difference Between DDL and DML in DBMS. https://techdifferences.com/difference-between-ddl-and-dml-in-dbms.html.
(26) MySQL Subquery - MySQL Tutorial. https://www.mysqltutorial.org/mysql-basics/mysql-subquery/.
(27) MySQL :: MySQL 8.0 Reference Manual :: 15.2.15 Subqueries. https://dev.mysql.com/doc/refman/8.0/en/subqueries.html.
(28) MySQL Subqueries - w3resource. https://www.w3resource.com/mysql/subqueries/index.php.
(29) MySQL ALTER TABLE Statement - W3Schools. https://www.w3schools.com/mysql/mysql_alter.asp.
(30) MySQL :: MySQL 8.0 Reference Manual :: 15.1.9 ALTER TABLE Statement. https://dev.mysql.com/doc/refman/8.0/en/alter-table.html.
(31) mysql - Alter table if exists or create if doesn't - Stack Overflow. https://stackoverflow.com/questions/16837134/alter-table-if-exists-or-create-if-doesnt.
(32) Table in MySQL | How to Create, Alter, Delete the Table in MySQL? - EDUCBA. https://www.educba.com/table-in-mysql/.
(33) SQL ALTER TABLE Statement - W3Schools. https://www.w3schools.com/SQl/sql_alter.asp.
(34) MySQL SELECT Statement - W3Schools. https://www.w3schools.com/mysql/mysql_select.asp.
(35) 5.3.4 Retrieving Information from a Table - MySQL. https://dev.mysql.com/doc/refman/8.0/en/retrieving-data.html.
(36) How to insert, update, and delete data in MySQL tables - Prisma. https://www.prisma.io/dataguide/mysql/inserting-and-modifying-data/inserting-and-deleting-data.
(37) MySQL INSERT INTO, UPDATE, DELETE Query Examples. https://www.tutsmake.com/mysql-insert-into-update-table-with-examples/.
(38) How to Insert, Update, Delete Data in Tables - EdTech Books. https://edtechbooks.org/learning_mysql/how_to_insert_update.
(39) undefined. http://www.oxforddictionaries.com/.
(40) github.com. https://github.com/mimiat/my-own-database/tree/56ae2f8b6d4588b267704ceae2e81a1b38bc1501/README.md.
Source: Conversation with Bing, 2/13/2024
(41) MySQL :: MySQL 8.0 Reference Manual :: 14 Functions and Operators. https://dev.mysql.com/doc/refman/8.0/en/functions.html.
(42) MySQL Functions - W3Schools. https://www.w3schools.com/mysql/mysql_ref_functions.asp.
(43) 14.1 Built-In Function and Operator Reference - MySQL. https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html.
(44) en.wikipedia.org. https://en.wikipedia.org/wiki/MySQL.