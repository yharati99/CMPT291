--Youssef El-Harati

--h)
CREATE TABLE "Enrollment" (
    sID INT NOT NULL,
    cID TEXT NOT NULL
);

--i)
INSERT INTO "Enrollment"
    VALUES
        (23929340, 'BIOL101'),
        (23929340, 'PHIL101'),
        (23929340, 'MATH101'),
        (23929340, 'CHEM102'),
        (21921015, 'MATH101'),
        (21921015, 'CHEM102'),
        (21921015, 'PHIL102'),
        (01028190, 'MATH307');

--j)
SELECT * FROM "Enrollment";

--k)
INSERT INTO "Enrollment"
    VALUES
        (123456, NULL);
        --Runtime error: NOT NULL constraint failed: Enrollment.cID (19)

--l)
DROP TABLE Enrollment;