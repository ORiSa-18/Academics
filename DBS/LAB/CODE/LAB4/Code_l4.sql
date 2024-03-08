/* Solution 1*/
select title 
from course,section 
where section.year=2009 and section.semester="Fall" 
union 
select title 
from course,section 
where section.year=2010 and section.semester="Spring";

/* Solution 3*/
SELECT D.dept_name, COUNT(C.course_id) AS total_courses
FROM Department D
LEFT JOIN Course C ON D.dept_name = C.dept_name
GROUP BY D.dept_name;

/*Solution 4*/
SELECT dept_name, AVG(salary) AS average_salary
FROM Instructor
GROUP BY dept_name
HAVING AVG(salary) > 42000;

/*Solution 5*/
SELECT
    s.course_id,
    s.semester,
    s.year,
    COUNT(t.ID) AS enrollment
FROM
    Section s
LEFT JOIN
    Takes t ON s.course_id = t.course_id
          AND s.sec_id = t.sec_id
          AND s.semester = t.semester
          AND s.year = t.year
WHERE
    s.semester = 'Spring' AND s.year = 2009
GROUP BY
    s.course_id, s.semester, s.year;

/*Solution 6*/
SELECT
    c.course_id,
    c.title AS course_title,
    p.prereq_id
FROM
    Course c
LEFT JOIN
    Prereq p ON c.course_id = p.course_id
ORDER BY
    c.course_id, p.prereq_id;

/*Solution 7*/
SELECT
    ID,
    name,
    dept_name,
    salary
FROM
    Instructor
ORDER BY
    salary DESC;

/*Solution 8*/
SELECT
    dept_name,
    SUM(salary) AS total_salary
FROM
    Instructor
GROUP BY
    dept_name
ORDER BY
    total_salary DESC
LIMIT 1;

/*Solution 9*/
SELECT
    dept_name,
    AVG(salary) AS avg_instructor_salary
FROM
    Instructor
GROUP BY
    dept_name
HAVING
    AVG(salary) > 42000;

/*Solution 10*/
