PRAGMA Foreign_Keys=True;

DROP TABLE Employee;
CREATE TABLE Employee (
EmpID INTEGER PRIMARY KEY,
Name NOT NULL,
HireDate NOT NULL,
Grade NOT NULL,
ManagerID INTEGER REFERENCES Employee(EmpID)
);

DROP TABLE Salary;
CREATE TABLE Salary (
SalaryID INTEGER PRIMARY KEY,
Grade UNIQUE,
Amount INTEGER DEFAULT 10000
);

