DELIMITER //
CREATE TRIGGER test.MonoxideCheck 
AFTER INSERT ON test.Pollutions
FOR EACH ROW
	BEGIN
	   IF NEW.COMAXVALUE >= 400.00 THEN
		   SET @dangersum = @dangersum + 1;
	   ELSEIF NEW.amount < 400 THEN
		   SET @safesum = @safesum + 1;
	   END IF;
	END;//
delimiter ;
