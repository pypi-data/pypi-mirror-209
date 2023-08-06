"""
This module provides a database engine connection for the Postgres database. It reads the username, password, and host
from AWS Parameter Store for better security.
This connection provides READ ONLY access to the Postgres database.
"""
from sqlalchemy import create_engine
from database_connector.utils import get_parameters
from database_connector.constants import (
    AWS_REGION,
    SAGEMAKER_PG_USERNAME_PARAMETER,
    SAGEMAKER_PG_PASSWORD_PARAMETER,
    SAGEMAKER_PG_HOST_PARAMETER,
    SAGEMAKER_PG_DB_NAME_PARAMETER,
)

parameter_to_value_map = get_parameters([
    SAGEMAKER_PG_USERNAME_PARAMETER,
    SAGEMAKER_PG_PASSWORD_PARAMETER,
    SAGEMAKER_PG_HOST_PARAMETER,
    SAGEMAKER_PG_DB_NAME_PARAMETER,
], AWS_REGION)

user = parameter_to_value_map[SAGEMAKER_PG_USERNAME_PARAMETER]
password = parameter_to_value_map[SAGEMAKER_PG_PASSWORD_PARAMETER]
host = parameter_to_value_map[SAGEMAKER_PG_HOST_PARAMETER]
db_name = parameter_to_value_map[SAGEMAKER_PG_DB_NAME_PARAMETER]

engine = create_engine(
    "postgresql://{user}:{password}@{host}/{db_name}".format(user=user, password=password, host=host, db_name=db_name),
    connect_args={"options": "-c statement_timeout=30000"},
)
