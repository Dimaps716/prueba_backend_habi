import logging
import os

import sqlalchemy
from dotenv import load_dotenv
from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool

Base = declarative_base()

load_dotenv()


def create_session(return_engine=False) -> Session:
    method = create_session.__name__
    try:
        db_name = os.getenv("DB_NAME")
        username = os.getenv("DB_USERNAME")
        password = os.getenv("DB_PASS")
        db_port = os.getenv("DB_PORT")
        db_host = os.getenv("DB_HOST")

        if os.getenv("MACHINE") == "DEV":
            # SQL Instance for Local machine
            engine = create_engine(
                # Equivalent URL:
                # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
                sqlalchemy.engine.url.URL(
                    drivername="mysql+pymysql",
                    username=username,  # e.g. "my-database-user"
                    password=password,  # e.g. "my-database-password"
                    host=db_host,  # e.g. "127.0.0.1"
                    port=db_port,  # e.g. 3306
                    database=db_name,  # e.g. "my-database-name",
                    # connect_args={"timeout": 30},
                ),
                poolclass=NullPool,
            )

        # Connect and create session
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        return session
    except Exception as ex:
        logging.error(f"{method}: {ex}")
        raise HTTPException(status.HTTP_424_FAILED_DEPENDENCY, detail=f"error {method}")
