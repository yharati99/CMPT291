--Youssef El-Harati

--Commands used:
--.open picnic.db
--CREATE TABLE "picnicTab" ("Id" INTEGER, "Table Type" TEXT, "Surface Material" TEXT, "Structural Material
--.mode csv
--.import --skip 1 Public_Picnic_Table_Locations.csv picnicTab
--SELECT * FROM "picnicTab";

--d) I think this table is a good design choice because it contains all the
--information needed to identify the picnic tables in the park. The table type, surface material, and structural
--material are all relevant attributes that can help in identifying the tables. The table also has a unique ID for
--each table, which is important for tracking and managing the tables. The table type can help in identifying the
--purpose of the table, such as whether it is a picnic table or a regular table. The surface material can help in
--identifying the durability and maintenance requirements of the table, while the structural material can help in
--identifying the strength and stability of the table. Overall, this table design is a good choice for managing
--picnic tables in the park.