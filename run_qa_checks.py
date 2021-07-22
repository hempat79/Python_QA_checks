import utils
from sqlite3 import Error
import pandas as pd
from pandasgui import show


def replace_table_parameters(rows, environment, date):
    run_sql_list = []
    for row in rows:
        run_sql = row[1].replace('ENV', environment).replace('DATE', date)
        print("\n Replaced SQL: {0}".format(run_sql))
        run_sql_list.append(run_sql)  
    print(run_sql_list)
    return run_sql_list    




def run_test_sql(conn, run_sql):
    try:
        results = []
        c = conn.cursor()
        print("\n Connection obtained: {0}".format(c))
        for sql in run_sql:
            
            test_sql = (str(sql).strip('[]').strip('\'\''))
            print("\n Running test sql: {0}".format(test_sql))
            c.execute(test_sql)
            results.append(c.fetchone())
        return results   
    except Error as e:
        print(e)
    
    
def generate_output_frame(qa_tests_rows, sql_output):
    try:
        if qa_tests_rows and sql_output: 
            #print("\n QA Tests Run: {0}".format(qa_tests_rows))
            #print("Query Result returned: {0}".format(sql_output))
            df = pd.DataFrame( qa_tests_rows )
            df.columns = ['code', 'sql']
            df.insert(2, "result", sql_output)
            print("\n Printing Data Frame: \n {0}".format(df))
        
            return df

    except Error as e:
        print(e)
        

def main():
   

# create a database connection
    db = utils.utils()
    db.create_connection()
    #print(db.cursor)

   
    if db.cursor is not None:
        # Run QA Checks and replace parameters
        print("Starting QA Checks!")
        sql_query = "SELECT code, test_sql FROM qa_tests where enabled = 'Y'"
        sqlrows = db.select_all_rows(sql_query)
        test_sql= replace_table_parameters(sqlrows, 'dev', '\'30/03/2021\'')               
        test_result = run_test_sql(db.connection, test_sql)
        
        db.close_connection()
    else:
        print("Error! cannot create the database connection.")

    qa_output = generate_output_frame(sqlrows, test_result)
    show(qa_output)

if __name__ == '__main__':
    main()    
