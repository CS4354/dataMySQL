CREATE TEMPORARY TABLE IF NOT EXISTS test.COAverages
SELECT 
    AVG(p.COMAXVALUE) AS highestAvg,
    p.SITEID,
    a.STATEID,
    a.COUNTYID,
    a.ADDRESSNAME
FROM
    test.Pollutions p
        LEFT JOIN
    test.Addresses a ON p.SITEID = a.SITEID
GROUP BY p.SITEID
ORDER BY AVG(p.COMAXVALUE);

SELECT 
    a.highestAvg, a.SITEID, a.ADDRESSNAME, s.STATENAME
FROM
    test.COAverages a
        LEFT JOIN
    test.States s ON a.STATEID = s.STATEID

