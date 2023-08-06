from .refractio import get_dataframe, get_local_dataframe
from .snowflake import Snowflake
from .mysql import Mysql
from .hive import Hive
from .sftp import Sftp

snowflake = Snowflake()
mysql = Mysql()
hive = Hive()
sftp = Sftp()
