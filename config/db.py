
from sqlalchemy import create_engine, MetaData

engine = create_engine("mariadb+pymysql://root:MasterHunter@10.72.0.2:3306/tests?charset=utf8mb4")

meta = MetaData()

## Nota:
## para evitar tener abierta la BD, se pone comentario
## conn = engine.connect()