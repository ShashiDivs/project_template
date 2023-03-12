from collection import namedtuple


DataIngestionConfig:namedtuple("DataIngestionConfig",
                               ['dataset_downloaded_url','raw_data_dir','ingested_train_dir','ingested_test_dir'])

DataValidationConfig: namedtuple('DataValidationConfig',['schema_file_dir'])