/*DELIMITER //

CREATE FUNCTION dept_count(dept_name VARCHAR(100)) RETURNS INTEGER
BEGIN
    DECLARE d_count INTEGER;
    SELECT COUNT(*) INTO d_count FROM department WHERE department.dep_name = dept_name;
    RETURN d_count;
END //
*/

SELECT dep_name FROM department where dept_count(dep_name)>0;
