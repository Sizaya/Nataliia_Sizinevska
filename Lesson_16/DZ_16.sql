select * from employees order by FIRST_NAME, LAST_NAME;
select first_name, last_name, salary, salary * 0.15 as taxes from employees;
select sum(salary) as SalarySum from employees;
select min(salary) as SalaryMin, max(salary) as SalaryMax from employees;
select avg(salary) as AverageSalary, count(employee_id) as NumberOfEmployees from employees;