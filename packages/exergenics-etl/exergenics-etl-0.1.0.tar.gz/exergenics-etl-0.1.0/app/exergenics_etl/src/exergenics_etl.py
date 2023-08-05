import os
import sqlalchemy
import pandas as pd
from pytz import timezone
from datetime import datetime
from typing import Union, Dict
from exergenics import exergenics
from urllib.parse import quote_plus
from sqlalchemy import create_engine

def hello(name: str) -> None:
    """Says hello to someone.

    Args:
        name (str): The name of the person to greet.
    
    Returns:
        None
    """

    print(f"Hello {name}!")

    return


def create_api(environment: str, component_name: str = "") -> exergenics.ExergenicsApi:
    """Creates an authenticated Exergenics API object. Environment variables, EXERGENICS_API_USERNAME
    and EXERGENICS_API_PASSWORD, are required.

    Args:
        environment (str): The environment where the API will be used. Must be either 'staging' or 'production'.
        component_name (str, optional): The name of the component that will be using the API.

    Raises:
        ValueError: If the input environment is not ‘staging’ or ‘production’.
        RuntimeError: If the username or password for API authentication is not found in environment variables.

    Returns:
        exergenics.ExergenicsApi: An authenticated Exergenics API object.
    """

    # Validate input environment
    try:
        assert (environment == 'staging') or (environment == 'production')
    except AssertionError:
        raise ValueError(f"Invalid input argument: environment = {environment}")
    
    # Get credentials from environment variables
    api_username = os.getenv('EXERGENICS_API_USERNAME')
    api_password = os.getenv('EXERGENICS_API_PASSWORD')
    try:
        assert api_username is not None, "EXERGENICS_API_USERNAME not found in environment variables!"
        assert api_password is not None, "EXERGENICS_API_PASSWORD not found in environment variables!"
    except AssertionError as e:
        raise RuntimeError(e)

    if environment == "staging":
        production = False
    elif environment == 'production':
        production = True

    api = exergenics.ExergenicsApi(
        username=api_username, password=api_password, useProductionApi=production)
    if component_name:
        api.setComponentName(component_name)

    if not api.authenticate():
        exit(0)

    return api


def create_sql_engine(databaseName: str, host: str, user: str, password: str) -> sqlalchemy.engine.base.Engine:
    """Formats a URL using the provided credentials
    and creates a connectable MySQL database engine object based on the URL.

    Args:
        databaseName (str): The name of the MySQL database to connect to.
        host (str): The hostname of the MySQL server.
        user (str): The MySQL user to authenticate as.
        password (str): The password for the MySQL user.
    
    Raises:
        RuntimeError: If the password is missing

    Returns:
        sqlalchemy.engine.base.Engine: A connectable MySQL engine object.
    """
    
    try:
        url = f"mysql+pymysql://{user}:{quote_plus(password)}@{host}:3306/{databaseName}"
    except TypeError:
        raise TypeError(
            f"Input password is not a string: password = {password}")
    engine = create_engine(url)

    return engine


def get_time_now() -> str:
    """Returns the current date and time in Melbourne the format 'YYYY_MM_DD_HHMM'.

    Returns:
        str: A string representing the current date and time in Melbourne.
    """
    now = datetime.now().astimezone(tz=timezone('Australia/Melbourne'))
    dt_string = now.strftime("%Y_%m_%d_%H%M")
    return dt_string


def structure_slack_message(bCode: str = "", jobId: Union[int, str] = "", message: str = "") -> str:
    """Creates a formatted Slack message string.

    Args:
        bCode (str, optional): The building code associated with the job. Defaults to "".
        jobId (Union[int, str], optional): The job ID. Defaults to "".
        message (str, optional): The message to be sent to a Slack channel. Defaults to "".

    Returns:
        str: A formatted Slack message.
    """

    return f'Time: {get_time_now()}\nBcode: {bCode}\nJob: {jobId}\n{message}'


def create_tmp_folder(tmpFolderName: str = "temp") -> None:
    """Creates a temporary folder with the given name if it does not already exist.

    Args:
        tmpFolderName (str, optional): The name of the temporary folder to create. Defaults to "temp".

    Raises:
        Exception: If the temporary folder was not successfully created.
    """

    if not os.path.exists(tmpFolderName):
        os.makedirs(tmpFolderName)

    try:
        assert os.path.exists(tmpFolderName)
    except AssertionError as e:
        raise Exception(f"temp folder doesn't not existing after attempting to make the directory: {e}")

    return


def generate_CSV_name(pointName: str) -> str:
    """Generates a CSV name for the trend log of a given data point name.

    Args:
        pointName (str): The name of a data point 

    Returns:
        str: The CSV name for the data point
    """

    # Follow logic from portal-php code to rename file names
    pointName = pointName.replace(" ", "_").replace(
        "/", "-").replace("~", "-").replace("&", "and").replace("%", "-")
    return f'{pointName}.csv'


def strftime_for_NaT(timestamp: Union[pd.Timestamp, pd._libs.tslibs.nattype.NaTType], log_time_format: str = "%d/%m/%Y %H:%M") -> str:
    """Formats a pandas Timestamp object as a string in the specified format. 
    Returns an empty string if the type of the timestamp is pandas.NaT.

    Args:
        timestamp (Union[pd.Timestamp, pd._libs.tslibs.nattype.NaTType]: A pandas Timestamp object to format.
        log_time_format (str, optional): the format of the output timestamp string. Defaults to "%d/%m/%Y %H:%M".

    Returns:
        str: A formatted string representing the provided timestamp or an empty string if the timestamp is pandas.NaT.
    """

    if timestamp is pd.NaT:
        return ""
    else:
        try:    
            return timestamp.strftime(log_time_format)
        except AttributeError as e:
            raise AttributeError(f'Cannot convert this timestamp to its equivalent string: timestamp = {timestamp}, {e}')


def generate_one_manifest_row(pointName: str, dfLog: pd.DataFrame, timestampColumnHeader: str = "timepretty") -> Dict:
    """Generates manifest data for a data point from its trend log.
    
    Args:
        pointName (str): The name of the data point.
        dfLog (pd.DataFrame): A pandas DataFrame containing the trend log for the data point.
        timestampColumnHeader (str, optional): The timestamp's column name. Defaults to "timepretty".

    Returns:
        Dict: A dictionary of manifest data for the data point.
    """

    # Get start/end time for the trend log of the point
    startTime = dfLog[timestampColumnHeader].min()
    endTime = dfLog[timestampColumnHeader].max()

    # Remove all dulicated rows
    dfLogCopy = dfLog.drop_duplicates()

    # Get metadata for the data point for manifest
    rowLength = len(dfLogCopy)
    interval = (endTime-startTime)/rowLength
    interval = str(round(interval.seconds/60, 4))
    metadataDict = {"point": pointName,
                    "file": generate_CSV_name(pointName),
                "rows": rowLength,
                "from": strftime_for_NaT(startTime),
                "to": strftime_for_NaT(endTime),
                "dataFrom": strftime_for_NaT(startTime),
                "dataTo": strftime_for_NaT(endTime),
                "interval": interval}

    return metadataDict


def generate_output_file_path(module: str, extension: str, bCode: str = "", pCode: str = "", category: str = "", jobId: Union[int, str] = "", path: str = "") -> str:
    """Generates a local file path for an output file.

    Args:
        module (str): The name of the module generating the output file, such as, transformation or preheader.
        extension (str): The file extension of the output file.
        bCode (str, optional): The building code associated with the file. Defaults to "".
        pCode (str, optional): The plant code associated with the file. Defaults to "".
        category (str, optional): The category of the output file, such as, zipfile or manifest. Defaults to "".
        jobId (Union[int, str], optional): The job ID associated with the output file. Defaults to "".
        path (str, optional): The directory path where the output file should be saved. Defaults to "".

    Returns:
        str: The file path for the output file.
    """

    # Format individual parts of the output file path string
    timeNow = get_time_now()
    if category:
        category = "_" + category
    if bCode:
        bCode = "_" + bCode
    if pCode:
        pCode = "_" + pCode
    if jobId:
        jobId = "_job" + str(jobId)

    outputFilePath = f"{timeNow}{bCode}{pCode}{jobId}_{module}{category}.{extension}"

    # Append the file path to the end of the directory path if the directory path is provided
    if path:
        if path.endswith('/'):
            outputFilePath = f"{path}{outputFilePath}"
        else:
            outputFilePath = f"{path}/{outputFilePath}"

    return outputFilePath

