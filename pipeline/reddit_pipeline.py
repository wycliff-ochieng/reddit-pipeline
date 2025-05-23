from utils.constants import CLIENT_ID,SECRET


def reddit_pipeline(file_name:str,subredit:str,time_filter='day',limit=None):

    #connect to reddit
    instance = connect_reddit(SECRET,CLIENT_ID,'Mastering airflow')
    #extraction
    #transformation
    #loading to csv