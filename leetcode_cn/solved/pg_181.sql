SELECT a.name AS "Employee"
FROM employee a
         LEFT JOIN employee b ON a.managerid = b.id
WHERE a.salary > b.salary;