from logging import DEBUG , INFO , WARNING , ERROR , CRITICAL
from datetime import datetime

logfile_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")

#Postgres接続情報
set_host = 'localhost'
set_database = 'onsite'
set_user = 'postgres'
set_pass = 'oncweb'
#ログファイルのパス
log_path = 'C:/KUXML2DB/logs/xml2db_MODE_yyyymmdd_' + logfile_timestamp + '.log'
loglevel = INFO