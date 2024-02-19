/* Question 1 */
SELECT course_id, title
FROM Takes
WHERE (semester = 'Fall' AND year = 2009)
   OR (semester = 'Spring' AND year = 2010)
UNION ALL

/* Question 2 */
SELECT course_id, title
FROM Takes
WHERE semester = 'Fall' AND year = 2009
INTERSECT ALL

SELECT course_id, title
FROM Takes
WHERE semester = 'Spring' AND year = 2010;

/* Question 3 */
SELECT course_id, title
FROM Takes
WHERE (semester = 'Fall' AND year = 2009)
MINUS

SELECT course_id, title
FROM Takes
WHERE semester = 'Spring' AND year = 2010;

/* Question 4 */
SELECT C.course_id, C.title
FROM Course C
WHERE NOT EXISTS (SELECT * FROM Takes T WHERE T.course_id = C.course_id);

/* Question 5 */
SELECT course_id, title
FROM Takes
WHERE (semester = 'Fall' AND year = 2009)
   OR (semester = 'Spring' AND year = 2010);

/* Question 6 */
SELECT COUNT(DISTINCT T.ID) AS total_students
FROM Takes T
WHERE T.course_id IN (SELECT course_id FROM Teaches WHERE ID = 10101);

/* Question 7 */
SELECT course_id, title
FROM Takes
WHERE (semester = 'Fall' AND year = 2009)
MINUS ALL

SELECT course_id, title
FROM Takes
WHERE semester = 'Spring' AND year = 2010;

/* Question 8 */
SELECT S.name
FROM Student S, Instructor I
WHERE S.name = I.name;

/* Question 9 */
SELECT name
FROM Instructor
WHERE salary > SOME (SELECT salary FROM Instructor WHERE dept_name = 'Biology');

/* Question 10 */
SELECT name
FROM Instructor
WHERE salary > ALL (SELECT salary FROM Instructor WHERE dept_name = 'Biology');

/* Question 11 */
SELECT dept_name
FROM Instructor
GROUP BY dept_name
HAVING AVG(salary) = (SELECT MAX(avg_salary) FROM (SELECT dept_name, AVG(salary) as avg_salary FROM Instructor GROUP BY dept_name) AS avg_salaries);

/* Question 12 */
SELECT dept_name
FROM Department
WHERE budget < (SELECT AVG(salary) FROM Instructor);

/* Question 13 */
SELECT course_id, title
FROM Takes
WHERE (semester = 'Fall' AND year = 2009)
   AND EXISTS (SELECT * FROM Takes WHERE course_id = Takes.course_id AND semester = 'Spring' AND year = 2010);

/* Question 14 */
SELECT S.name
FROM Student S
WHERE NOT EXISTS (SELECT course_id FROM Course WHERE dept_name = 'Biology' 
                     EXCEPT 
                     SELECT course_id FROM Takes WHERE ID = S.ID);

/* Question 15 */
SELECT course_id, title
FROM Takes
GROUP BY course_id, title
HAVING COUNT(*) <= 1 AND year = 2009;

/* Question 16 */
SELECT S.name
FROM Student S
WHERE (SELECT COUNT(DISTINCT T.course_id)
       FROM Takes T
       WHERE T.ID = S.ID AND T.course_id IN (SELECT course_id FROM Course WHERE dept_name = 'CSE')) >= 2;

/* Question 17 */
SELECT dept_name, AVG(salary) AS avg_salary
FROM Instructor
GROUP BY dept_name
HAVING AVG(salary) > 42000;

/* Question 18 */
CREATE VIEW all_courses AS
SELECT C.course_id, C.title, Sec.building, Sec.room_number
FROM Course C
JOIN Section Sec ON C.course_id = Sec.course_id
WHERE Sec.semester = 'Fall' AND Sec.year = 2009 AND C.dept_name = 'Physics';

/* Question 19 */
SELECT *
FROM all_courses;

/* Question 20 */
CREATE VIEW department_total_salary AS
SELECT dept_name, SUM(salary) AS total_salary
FROM Instructor
GROUP BY dept_name;
