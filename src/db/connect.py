from urllib import parse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import configs

if type(configs.DATABASE.PWD) == str: 
    password = parse.quote_plus(configs.DATABASE.PWD)
else: password = configs.DATABASE.PWD

engine = create_engine(f"postgresql://"
                       f"{configs.DATABASE.USER}:{password}"
                       f"@{configs.DATABASE.HOST}:{int(configs.DATABASE.PORT)}"
                       f"/{configs.DATABASE.DB}")
Session = sessionmaker(bind=engine)
