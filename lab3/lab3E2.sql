--Youssef El-Harati


--a).open alum.db

--b) CREATE TABLE "AlumProject" ("ID" INTEGER PRIMARY KEY, "prjName" TEXT, "budget" REAL);

--c) INSERT INTO "AlumProject" VALUES (1,'Cybercab',26.1),(2,'Metaverse',42.7),(3,'Windows12',16.5);

--d) INSERT INTO "AlumProject" VALUES (NULL,'Fortnite2',40);
-- I did not get an error when I did this, instead it was added to the table with the values entered but the ID was automatically generated to be 4.

--e) CREATE TABLE "Alumnus" (name TEXT, ID INTEGER PRIMARY KEY, salary REAL, prjID INTEGER REFERENCES AlumProject(ID) ON DELETE CASCADE);

--f) INSERT INTO "Alumnus" VALUES ('Becca',1,500.0,2),('James',2,3000.0,2),('Jill',3,4000.0,NULL),('Ardy',4,1000.0,3),('Elon',5,2000.0,1),('Mark',6,9900.0,2),('Bill',7,100.0,3);

--g) INSERT INTO "Alumnus" VALUES ('Youssef',8,999999999999999.99,50);
-- Runtime error: FOREIGN KEY constraint failed (19)

--h) INSERT INTO "Alumnus" VALUES ('Youssef',1,999999999999999.99,2);
-- Runtime error: UNIQUE constraint failed: Alumnus.ID (19)

--i) DELETE FROM AlumProject WHERE prjName='Windows12';

--j) SELECT * FROM Alumnus;
-- Becca|1|500.0|2
-- James|2|3000.0|2
-- Jill|3|4000.0|
-- Elon|5|2000.0|1
-- Mark|6|9900.0|2
-- Ardy and Bill are no longer on the Alumnus table.