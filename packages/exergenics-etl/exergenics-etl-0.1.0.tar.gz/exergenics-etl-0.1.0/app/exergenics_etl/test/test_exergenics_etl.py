import pytest
import os
import pandas as pd
import numpy as np
import shutil
from dotenv import load_dotenv

from ..src.exergenics_etl import (
    create_api,
    create_sql_engine,
    get_time_now,
    create_tmp_folder,
    generate_CSV_name,
    strftime_for_NaT,
    generate_one_manifest_row,
    generate_output_file_path
)

load_dotenv()


class TestCreateApiClass:

    @pytest.fixture(scope='class', params=['staging', 'production'])
    def my_valid_environment(self, request):
        return request.param

    @pytest.fixture(scope='class')
    def my_invalid_environment(self):
        return 'environment'

    def test_create_api_for_valid_environment(self, my_valid_environment):
        api = create_api(my_valid_environment)
        assert api.authenticate()

    def test_create_api_for_invalid_environment(self, my_invalid_environment):
        with pytest.raises(ValueError):
            api = create_api(my_invalid_environment)

class TestCreateSQLEngineClass:

    @pytest.fixture(scope='class', params=['datastore', 'header-repo'])
    def my_test_database_name(self, request):
        return request.param

    def test_create_sql_engine(self, my_test_database_name):
        """Test if the engine created is connectable."""
        engine = create_sql_engine(databaseName=my_test_database_name,
                                   host="ex-database.mysql.database.azure.com", user="exergenics", password=os.getenv('MYSQL_PASSWORD'))
        engine.connect()
    
    def test_none_password(self, my_test_database_name):
        """Test raising TypeError when the password is not found in environment variables 
        and is None."""
        myMissingMysqlPassword = os.getenv('MISSING_PASSWORD')
        with pytest.raises(TypeError):
            engine = create_sql_engine(databaseName=my_test_database_name,
                                    host="ex-database.mysql.database.azure.com", user="exergenics", password=myMissingMysqlPassword)


class TestGetTimeNow:

    @pytest.fixture(scope='class')
    def my_expected_output_datetime_length(self):
        return 15
    
    @pytest.fixture(scope='class')
    def my_expected_output_datetime_type(self):
        return str

    def test_output_datetime_length(self, my_expected_output_datetime_length):
        """Test the length of the output datetime in string."""
        assert len(get_time_now()) == my_expected_output_datetime_length

    def test_output_datetime_type(self, my_expected_output_datetime_type):
        """Test the type of the output datetime in string."""
        assert type(get_time_now()) == my_expected_output_datetime_type


class TestCreateTmpFolderClass:

    @pytest.fixture(scope='class')
    def my_test_folder(self):
        return "test_tmp_folder"

    def test_create_tmp_folder_when_not_exist(self, my_test_folder):
        """Test if the function creates a temporary folder when the folder does not exist."""
        assert not os.path.exists(my_test_folder)

        create_tmp_folder(my_test_folder)
        assert os.path.exists(my_test_folder)

        shutil.rmtree(my_test_folder)
    
    def test_create_tmp_folder_when_exists(self, my_test_folder):
        """Test if the function will not overwrite when the temporary folder 
        we want to create already exists."""
        os.makedirs(my_test_folder+"/sub_folder")
        assert os.path.exists(my_test_folder)
        assert os.path.exists(my_test_folder+"/sub_folder")

        create_tmp_folder(my_test_folder)
        assert os.path.exists(my_test_folder+"/sub_folder")

        shutil.rmtree(my_test_folder)


class TestGenerateCSVNameClass:

    @pytest.fixture(scope='class')
    def my_test_point_name(self):
        return "CM-01 VSD INPUT POWER Trend - Present Value () (kW)"

    def test_generate_CSV_name_without_certain_characters(self, my_test_point_name):
        """Test if the following special characterare not in the output CSV name:
        spaces, '/', '~', '&', '%'.
        """
        csvName = generate_CSV_name(my_test_point_name)
        for c in [' ', '/', '~', '&', '%']:
            assert c not in csvName


class TestStrftimeForNaTClass:

    @pytest.fixture(scope='class')
    def my_NaT(self):
        return pd.to_datetime([np.nan]).min()
    
    @pytest.fixture(scope='class')
    def my_datetime_object_and_string(self):
        return pd.to_datetime(['2023-03-17', '2023-03-18']).min(), "17/03/2023 00:00"

    def test_strftime_for_NaT(self, my_NaT):
        assert strftime_for_NaT(my_NaT) == ""

    def test_strftime_for_datetime_object(self, my_datetime_object_and_string):
        myDatetimeObject = my_datetime_object_and_string[0]
        myDatetimeString = my_datetime_object_and_string[1]
        assert strftime_for_NaT(
            myDatetimeObject) == myDatetimeString


class TestGenerateOneManifestRowClass:

    @pytest.fixture(scope='class')
    def my_test_point_name(self):
        return "CM-01 CH-LOAD TRD1 _ (TRD1) (%)"

    @pytest.fixture(scope='class')
    def my_test_trend_log_dataframe(self, my_test_point_name):
        return pd.DataFrame({"timepretty": pd.to_datetime(['2023-03-18', '']),
                             'observation': [my_test_point_name, my_test_point_name],
                             'datapoint': [1, 2]})

    def test_generate_one_manifest_row(self, my_test_point_name, my_test_trend_log_dataframe):
        """Test the type of the output manifest data for a test point."""
        manifestRow = generate_one_manifest_row(my_test_point_name, my_test_trend_log_dataframe)
        assert type(manifestRow) == dict


class TestGenerateOutputFilePathClass:

    @pytest.fixture(scope='class', params=['', '/temp/', 'temp'])
    def my_test_path(self, request):
        return request.param
    
    @pytest.fixture(scope='class')
    def my_test_inputs(self):
        return {'module': 'preheader', 'extension': 'zip', 'bCode': 'CROWN-METROPOL', 
                'pCode': 'PLANT-117', 'category': 'zipfile', 'jobId': 101}

    def test_generate_output_file_path(self, my_test_path, my_test_inputs):
        """Test generating output file path with different path prefixes."""
        outputFilePath = generate_output_file_path(
            module=my_test_inputs['module'], extension=my_test_inputs['extension'], 
            bCode=my_test_inputs['bCode'], pCode=my_test_inputs['pCode'],
            category=my_test_inputs['category'], jobId=my_test_inputs['jobId'],
            path=my_test_path)
        assert '//' not in outputFilePath
