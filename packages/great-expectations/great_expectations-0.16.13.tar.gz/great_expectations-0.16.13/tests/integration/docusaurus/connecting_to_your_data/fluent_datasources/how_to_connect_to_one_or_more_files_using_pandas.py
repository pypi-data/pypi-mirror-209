"""
To run this code as a local test, use the following console command:
```
pytest -v --docs-tests -m integration -k "how_to_connect_to_one_or_more_files_using_pandas" tests/integration/test_script_runner.py
```
"""
import pathlib


# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/how_to_connect_to_one_or_more_files_using_pandas.py get_context">
import great_expectations as gx

context = gx.get_context()
# </snippet>

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/how_to_connect_to_one_or_more_files_using_pandas.py define_add_pandas_filesystem_args">
datasource_name = "my_new_datasource"
path_to_folder_containing_csv_files = "<INSERT_PATH_TO_FILES_HERE>"
# </snippet>

path_to_folder_containing_csv_files = str(
    pathlib.Path(
        gx.__file__,
        "..",
        "..",
        "tests",
        "test_sets",
        "taxi_yellow_tripdata_samples",
    ).resolve(strict=True)
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/how_to_connect_to_one_or_more_files_using_pandas.py create_datasource">
datasource = context.sources.add_pandas_filesystem(
    name=datasource_name, base_directory=path_to_folder_containing_csv_files
)
# </snippet>

assert datasource_name in context.datasources

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/how_to_connect_to_one_or_more_files_using_pandas.py define_add_csv_asset_args">
asset_name = "my_taxi_data_asset"
batching_regex = r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv"
# </snippet>

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/how_to_connect_to_one_or_more_files_using_pandas.py add_asset">
datasource.add_csv_asset(name=asset_name, batching_regex=batching_regex)
# </snippet>

assert datasource.get_asset_names() == {"my_taxi_data_asset"}
assert datasource.get_asset(asset_name).name == "my_taxi_data_asset"
