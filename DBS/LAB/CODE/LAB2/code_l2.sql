/*Answer 9*/

SELECT ID, name, dept_name
FROM Student;

/*Answer 10*/

SELECT ID, name
FROM Instructor
WHERE dept_name = 'CSE';

/*Answer 11*/

SELECT title
FROM Course
WHERE dept_name = 'CSE' AND credits = 3;

/*Answer 12*/

SELECT title
FROM Course
WHERE dept_name = 'CSE' AND credits = 3;

/*Answer 13*/

SELECT T.course_id, C.title
FROM Takes T
JOIN Course C ON T.course_id = C.course_id
WHERE T.ID = 12345;

/*Answer 13*/

SELECT ID, name, salary
FROM Instructor
WHERE salary BETWEEN 40000 AND 90000;

/* Question 14 */
SELECT ID
FROM Instructor
WHERE ID NOT IN (SELECT DISTINCT id FROM Teaches);

/* Question 15 */
SELECT S.name AS student_name, C.title AS course_name, T.year
FROM Takes T
JOIN Student S ON T.ID = S.ID
JOIN Course C ON T.course_id = C.course_id
JOIN Section Sec ON T.course_id = Sec.course_id AND T.sec_id = Sec.section_id
WHERE Sec.room_number = 303;

/* Question 16 */
SELECT S.name AS student_name, T.year, T.course_id AS c_id, C.title AS c_name
FROM Takes T
JOIN Student S ON T.ID = S.ID
JOIN Course C ON T.course_id = C.course_id
WHERE T.year = 2015;

/* Question 17 */
SELECT ID, name, salary AS inst_salary
FROM Instructor
WHERE salary > (SELECT MAX(salary) FROM Instructor WHERE dept_name = 'CSE');

/* Question 18 */
SELECT ID, name
FROM Instructor
WHERE dept_name LIKE '%ch%';

/* Question 19 */
SELECT name AS student_name, LENGTH(name) AS name_length
FROM Student;

/* Question 20 */
SELECT dept_name, SUBSTRING(dept_name FROM 3 FOR 3) AS chars_from_3rd_pos
FROM Department;

/* Question 21 */
SELECT UPPER(name) AS upper_case_name
FROM Instructor;

/* Question 22 */
-- Assuming you want to replace NULL with 0 in the salary column of the Instructor table
UPDATE Instructor
SET salary = COALESCE(salary, 0);

/* Question 23 */
SELECT salary, ROUND(salary / 3, -2) AS salary_divided_by_3_rounded
FROM Instructor;

/* Question 24 */
SELECT TO_CHAR(birth_date, 'DD-MON-YYYY') AS format_1,
       TO_CHAR(birth_date, 'DD-MON-YY') AS format_2,
       TO_CHAR(birth_date, 'DD-MM-YY') AS format_3
FROM Employee;

/* Question 25 */
SELECT name AS employee_name,
       TO_CHAR(birth_date, 'YYYY') AS full_year,
       TO_CHAR(birth_date, 'Year') AS year_full_spelled,
       TO_CHAR(birth_date, 'year') AS year_lower_spelled
FROM Employee;

/* Question 26 */
SELECT name AS employee_name,
       TO_CHAR(birth_date, 'Day') AS day_full_spelled,
       TO_CHAR(birth_date, 'DAY') AS day_upper_full_spelled
FROM Employee;

/* Question 27 */
SELECT name AS employee_name,
       TO_CHAR(birth_date, 'Month') AS month_full_spelled,
       TO_CHAR(birth_date, 'MONTH') AS month_upper_full_spelled
FROM Employee;

/* Question 28 */
SELECT name AS employee_name,
       TO_CHAR(LAST_DAY(birth_date), 'DD-MON-YYYY') AS last_day_of_month
FROM Employee
WHERE name = 'Mr. X';

/* Question 29 */
SELECT name AS employee_name,
       EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM birth_date) AS age
FROM Employee;

/* Question 30 */
SELECT name AS employee_name,
       birth_date + INTERVAL '60 years' AS saturday_following_60th_birthday
FROM Employee;

/* Question 31 */
SELECT name AS employee_name
FROM Employee
WHERE EXTRACT(YEAR FROM birth_date) = &X;

/* Question 32 */
SELECT name AS employee_name
FROM Employee
WHERE EXTRACT(YEAR FROM birth_date) BETWEEN &X AND &Y;

/* Question 33 */

SELECT name AS employee_name,
       birth_date + INTERVAL '60 years' AS retirement_year
FROM Employee
WHERE EXTRACT(YEAR FROM birth_date) + 60 = &X;


