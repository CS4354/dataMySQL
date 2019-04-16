CREATE TABLE IF NOT EXISTS test.States (
  STATEID INT PRIMARY KEY,
  STATENAME VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS test.Counties (
  COUNTYID INT PRIMARY KEY,
  COUNTYNAME VARCHAR(255),
  STATEID INT NOT NULL,
  FOREIGN KEY (STATEID) REFERENCES test.States(STATEID)
);
CREATE TABLE IF NOT EXISTS test.Addresses (
  SITEID INT PRIMARY KEY,
  STATEID INT,
  COUNTYID INT,
  ADDRESSNAME VARCHAR(255),
  LATITUDE DECIMAL(10, 8) NOT NULL,
  LONGITUDE DECIMAL(11, 8) NOT NULL
);
CREATE TABLE IF NOT EXISTS test.Pollutions (
  POLLUTIONDATE DATE PRIMARY KEY,
  SITEID INT,
  NO2MEAN FLOAT(10, 4),
  NO2MAXVALUE INT,
  NO2MAXHOUR INT,
  NO2AQI INT,
  O3MEAN FLOAT(10, 4),
  O3MAXVALUE INT,
  O3MAXHOUR INT,
  O3AQI INT,
  SO2MEAN FLOAT(10, 4),
  SO2MAXVALUE INT,
  SO2MAXHOUR INT,
  SO2AQI INT,
  COMEAN FLOAT(10, 4),
  COMAXVALUE INT,
  COMAXHOUR INT,
  COAQI INT,
  FOREIGN KEY (SITEID) REFERENCES test.Addresses (SITEID)
);