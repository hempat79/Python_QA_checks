CREATE TABLE IF NOT EXISTS qa_tests(code text PRIMARY KEY, description text NOT NULL, enabled text NOT NULL, parameter text, test_sql text NOT NULL, exp_result integer); 

INSERT INTO qa_tests (code, description, enabled, parameter, test_sql, exp_result) 
VALUES 
('qa_ch_01', 'Runs the SQL against the Channel table to count duplicates.Duplicates count must be 0', 'Y', 'ENV', 
 'select count(*) from (select channel_code, count(*) from channel_table_ENV group by channel_code having count(*) > 1)', 0), 
('qa_ch_02', 'Check the FK between channel_code and its child table channel_transaction to identify orphans at a given date', 'Y', 'ENV, DATE',
'select count(*) from channel_transaction_ENV A left join channel_table_ENV B on (A.channel_code = B.channel_code) where B.channel_code is null and transaction_date = DATE ', 0), 
('qa_Ch_03', 'Counts the records in channel_transaction table at a given date that have amount null', 'N', 'ENV, DATE', 
'select count(*) from channel_transaction_ENV where transaction_date = DATE and transaction_amount is null', 0);

CREATE TABLE IF NOT EXISTS channel_table_ENV (channel_code text NOT NULL);
CREATE TABLE IF NOT EXISTS channel_transaction_ENV (channel_code text NOT NULL, transaction_date text NOT NULL, transaction_amount REAL); 
INSERT INTO channel_table_ENV (channel_code) VALUES ('SKY'),('BBC'), ('ITV'), ('BBC'); 
INSERT INTO channel_transaction_ENV (channel_code, transaction_date, transaction_amount) VALUES ('SKY', '01/01/2001', 100),('BBC1', '30/03/2021', 200);
