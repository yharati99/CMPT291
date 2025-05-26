--Schema and insert statements for the database
CREATE TABLE M (
    mID INTEGER PRIMARY KEY,
    mName TEXT,
    mState TEXT,
    mCountry TEXT
);

CREATE TABLE D (
    dID INTEGER PRIMARY KEY,
    dName TEXT,
    dState TEXT,
    dCountry TEXT
);

CREATE TABLE I (
    iID INTEGER PRIMARY KEY,
    desc TEXT,
    color TEXT,
    weight INTEGER,
    price INTEGER,
    qty INTEGER,
    mID INTEGER,
    dID INTEGER,
    FOREIGN KEY (mID) REFERENCES M(mID),
    FOREIGN KEY (dID) REFERENCES D(dID)
);

INSERT INTO M (mID, mName, mState, mCountry) VALUES
(1, 'Sonia', 'AB', 'Canada'),
(2, 'Mikana', 'AB', 'Canada'),
(3, 'Ree', 'CL', 'USA'),
(4, 'Zox', 'NY', 'USA');

INSERT INTO D (dID, dName, dState, dCountry) VALUES
(1, 'Global', 'AB', 'Canada'),
(2, 'REX', 'ON', 'Canada'),
(3, 'Zee', 'NY', 'USA'),
(4, 'FEE', 'NJ', 'USA'),
(5, 'Known', 'AB', 'Canada');

INSERT INTO I (iID, desc, color, weight, price, qty, mID, dID) VALUES
(1, 'Chair', 'Brown', 25, 20, 100, 1, 1),
(2, 'Table', 'Green', 100, 25, 50, 1, 2),
(3, 'Book', 'Green', 10, 5, 300, 3, 1),
(4, 'Screen', 'Silver', 75, 30, 50, 4, 3),
(5, 'Printer', 'White', 20, 10, 200, 2, 4),
(6, 'Door', 'Green', 200, 40, 2, 4, 1);

--1. Find all items in Green Color.
SELECT * FROM I WHERE color = 'Green';
--2. Find all items with Green Color and the price is less than 10.
SELECT * FROM I WHERE color = 'Green' AND price < 10;
--3. Find the name of all distributors from the USA.
SELECT dName FROM D WHERE dCountry = 'USA';
--4. Find the Desc. of items with Qty more than 60.
SELECT desc FROM I WHERE qty > 60;
--5. Find names of Manufacturers from AB.
SELECT mName FROM M WHERE mState = 'AB';
--6. Find all manufacturers' names from the USA who made items with Brown Color.
SELECT m.mName FROM M JOIN I ON M.mID = I.mID WHERE I.color = 'Brown' AND M.mCountry = 'USA';
--7. Find the description of all items manufactured in the USA and is made of Brown Color.
SELECT desc FROM I WHERE mID IN (SELECT mID FROM M WHERE mCountry = 'USA') AND color = 'Brown';
--8. Find the description of all items manufactured in the USA and distributed by a Canadian Company.
SELECT I.desc FROM I JOIN M ON I.mID = M.mID JOIN D ON I.dID = D.dID WHERE M.mCountry = 'USA' AND D.dCountry = 'Canada';
--9. Find Desc of all items manufactured and distributed in Canada.
SELECT I.desc FROM I JOIN M ON I.mID = M.mID JOIN D ON I.dID = D.dID WHERE M.mCountry = 'Canada' AND D.dCountry = 'Canada';
--10. Find Desc of items manufactured and distributed in the same country.
SELECT I.desc FROM I JOIN M ON I.mID = M.mID JOIN D ON I.dID = D.dID WHERE M.mCountry = D.dCountry;
--11. Find Desc of items manufactured and distributed in dierent countries.
SELECT I.desc FROM I JOIN M ON I.mID = M.mID JOIN D ON I.dID = D.dID WHERE M.mCountry != D.dCountry;
--12. Find a colour that is only manufactured in Canada (for example, Brown for chair is only made in Canada. No product manufactured in the USA has a brown colour).
--13. Find Colors that are manufactured in both the USA and Canada (Green, for example).
--14. Find the name of the distributor who never distributed any item.
--15. Find the total number of items each State/province manufactured.
--16. Find the total number of items each country distributed.
--17. Find the name of state/provinces that distributed more than 500 items (in total Qty).