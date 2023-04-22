-- Script that creates the table unique_id on your MySQL server.

REATE TABLE IF NOT EXISTS unique_id
(
  id INT DEFAULT 1 AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL
);
