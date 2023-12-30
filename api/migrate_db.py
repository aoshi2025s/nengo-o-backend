from sqlalchemy import create_engine

from api.models.question import Base

DB_URL = "mysql+pymysql://root@db:3306/backend?charset=utf8"
engine = create_engine(DB_URL, echo=True)

# DockerコンテナのMySQLに対して、テーブルを作成する
# すでにテーブルが存在している場合は、一度削除してから作成する

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()

