select count(distinct job_id) from employees;
select avg(salary) as AvarageSalary, count(employee_id) as CountEmployee from employees where DEPARTMENT_ID=90;
select job_id, count(employee_id) CountEmployee from employees group by JOB_ID;
select first_name, last_name, department_id from employees;
select e.FIRST_NAME, e.LAST_NAME, e.JOB_ID, e.DEPARTMENT_ID, d.DEPARTMENT_NAME from employees e join departments d on (e.DEPARTMENT_ID = d.DEPARTMENT_ID) join locations l on (d.LOCATION_ID = l.LOCATION_ID) where l.CITY = 'London';