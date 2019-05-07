CREATE INDEX YearInd ON
test.Pollutions(POLLUTIONDATE);

-- CREATE VIEW `test`.`MarkerView` AS
--     SELECT 
--         `a`.`ADDRESSNAME` AS `AddressName`,
--         `a`.`LATITUDE` AS `Latitude`,
--         `a`.`LONGITUDE` AS `Longitude`,
--         `p`.`NO2MEAN` AS `NO2Mean`,
--         `p`.`NO2MAXVALUE` AS `NO2MaxValue`,
--         `p`.`NO2MAXHOUR` AS `NO2MaxHour`,
--         `p`.`NO2AQI` AS `NO2AQI`,
--         `p`.`O3MEAN` AS `O3Mean`,
--         `p`.`O3MAXVALUE` AS `O3MaxValue`,
--         `p`.`O3MAXHOUR` AS `O3MaxHour`,
--         `p`.`O3AQI` AS `O3AQI`,
--         `p`.`SO2MEAN` AS `SO2Mean`,
--         `p`.`SO2MAXVALUE` AS `SO2MaxValue`,
--         `p`.`SO2MAXHOUR` AS `SO2MaxHour`,
--         `p`.`SO2AQI` AS `SO2AQI`,
--         `p`.`COMEAN` AS `COMean`,
--         `p`.`COMAXVALUE` AS `COMaxValue`,
--         `p`.`COMAXHOUR` AS `COMaxHour`,
--         `p`.`COAQI` AS `COAQI`
--     FROM
--         (`test`.`Pollutions` `p`
--         JOIN `test`.`Addresses` `a`)
--     WHERE
--         (`a`.`SITEID` = `p`.`SITEID`)