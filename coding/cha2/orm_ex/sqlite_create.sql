--create a database: sqlite3 D:\tutorial\Architecture_Patterns_with_Python\coding\cha2\db_test.db
--create the table
CREATE TABLE test (
    id integer PRIMARY KEY,
   sku text,
   price integer
);


INSERT INTO test(sku, price)
VALUES ("lamp", 13);

SELECT * FROM test;

---show all tables
--- .tables

--show all databases
-- .databases

-- drop table
-- drop table test;
--exit
--.exit