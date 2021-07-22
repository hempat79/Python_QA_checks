import utils

sql_create_tests_table = """ CREATE TABLE IF NOT EXISTS qa_tests(code text PRIMARY KEY, description text NOT NULL, enabled text NOT NULL, parameter text, test_sql text NOT NULL, exp_result integer); """
sql_insert_test_data = """ INSERT INTO qa_tests (code, description, enabled, parameter, test_sql, exp_result) 
                                VALUES ('qa_ch_01', 'Runs the SQL against the Channel table to count duplicates.Duplicates count must be 0', 'Y', 'ENV', 
                                        'select count(*) from (select channel_code, count(*) from channel_table_ENV group by channel_code having count(*) > 1)', 0), 
                                       ('qa_ch_02', 'Check the FK between channel_code and its child table channel_transaction to identify orphans at a given date', 'Y', 'ENV, DATE',
                                        'select count(*) from channel_transaction_ENV A left join channel_table_ENV B on (A.channel_code = B.channel_code) where B.channel_code is null and transaction_date = DATE ', 0), 
                                       ('qa_Ch_03', 'Counts the records in channel_transaction table at a given date that have amount null', 'N', 'ENV, DATE', 
                                        'select count(*) from channel_transaction_ENV where transaction_date = DATE and transaction_amount is null', 0); """
sql_create_channel_table = """  CREATE TABLE IF NOT EXISTS channel_table_ENV (channel_code text NOT NULL); """
sql_create_channel_transaction_table = """  CREATE TABLE IF NOT EXISTS channel_transaction_ENV (channel_code text NOT NULL, transaction_date text NOT NULL, transaction_amount REAL); """
sql_insert_channel_data = """ INSERT INTO channel_table_ENV (channel_code) VALUES ('SKY'),('BBC'), ('ITV'), ('BBC'); """
sql_insert_channel_transaction_data = """ INSERT INTO channel_transaction_ENV (channel_code, transaction_date, transaction_amount) VALUES ('SKY', '01/01/2001', 100),('BBC1', '30/03/2021', 200);  """

def replace_ENV_parameters(sql, environment):
        
        run_sql = sql.replace('ENV', environment)
        return run_sql    

def main():
    
    # create a database connection
    db = utils.utils()
    db.create_connection()
    print(db.cursor)

    # create tables
    if db.cursor is not None:
        # create test table and insert data
        db.run_create_insert_query(sql_create_tests_table)  
        db.run_create_insert_query(sql_insert_test_data) 

        # create db tables channel_table and channel_transaction
        channel_sql = replace_ENV_parameters(sql_create_channel_table, 'dev')
        db.run_create_insert_query(channel_sql)
        channel_trans_sql = replace_ENV_parameters(sql_create_channel_transaction_table, 'dev')
        db.run_create_insert_query(channel_trans_sql) 
        # Insert test data to db tables
        channel_insert_sql = replace_ENV_parameters(sql_insert_channel_data, 'dev')
        db.run_create_insert_query(channel_insert_sql)
        channel_trans_insert_sql = replace_ENV_parameters(sql_insert_channel_transaction_data, 'dev')
        db.run_create_insert_query(channel_trans_insert_sql)
        db.close_connection()
       
        
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()