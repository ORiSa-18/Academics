/* Solution 1*/
select title 
from course,section 
where section.year=2009 and section.semester="Fall" 
union 
select title 
from course,section 
where section.year=2010 and section.semester="Spring";

/* Solution 2*/
