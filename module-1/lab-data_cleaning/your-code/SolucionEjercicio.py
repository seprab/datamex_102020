import pandas as pd
import pymysql
import sqlalchemy

# Create a mysql engine to set the connection to the server. Check the connection details in this link
# https://relational.fit.cvut.cz/search?tableCount%5B%5D=0-10&tableCount%5B%5D=10-30&dataType%5B%5D=Numeric
# &databaseSize%5B%5D=KB&databaseSize%5B%5D=MB

db = "stats"
hostname = "relational.fit.cvut.cz"
port = "3306"
username = "guest"
password = "relational"

# sample read.setConnection("mysql://relational.fit.cvut.cz:3306/mutagenesis","guest","relational");
'''# default
engine = create_engine('mysql://scott:tiger@localhost/foo')

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')'''

# dialect+driver://username:password@host:port/database

con_string = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{db}"
engine = sqlalchemy.create_engine(con_string)

# with engine.connect() as connection:
# users_table = pd.read_sql(connection.execute("SELECT * FROM users"))
users_table = pd.read_sql("SELECT * FROM users", engine)
users_table.rename(columns={'Id': 'userId'}, inplace=True)

# post_table = pd.read_sql(connection.execute("SELECT * FROM posts"))
post_table = pd.read_sql("SELECT * FROM posts", engine)
post_table.rename(columns={'Id': 'postId', 'OwnerUserId': 'userId'}, inplace=True)

# **users columns** userId, Reputation,Views,UpVotes,DownVotes
users_columns = users_table[['userId', 'Reputation', 'Views', 'UpVotes', 'DownVotes']]

# **posts columns** postId, Score,userID,ViewCount,CommentCount
posts_columns = post_table[['postId', 'Score', 'userId', 'ViewCount', 'CommentCount']]
# print(f"Número de datos NaN en la tabla post: \n", posts_columns.isna().sum())

merge_tables = pd.merge(users_columns, posts_columns)

print(merge_tables.head())
print(f"Número de datos NaN en la tabla merge: \n", merge_tables.isna().sum())

'''ViewCount tania 49055 values null, al haber indices no relacionados con indices del usuario quedaron en 48369'
 Analizando la tabla encontre casos donde se podría promediar por las vistas del usuario en general..... pero otros usuarios tienen todo en NaN. Pienso lo mejor es eliminar la columna o los usuarios que tengan todo en NaN'''


print(merge_tables.dtypes)
#En vista de que los tipos de datos se ajustan a la necesidad del cliente, me parece que es conveniente seguir tratando el mismo tipo de datos.