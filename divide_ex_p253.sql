select distinct emp
from EmpSkills ES1
where not exists
			(select skill 
			  from Skills
			 except 
			   select skill
			    from EmpSkills ES2 
			 where ES1.emp = ES2.emp);