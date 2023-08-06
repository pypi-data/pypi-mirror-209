# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spalah', 'spalah.dataframe', 'spalah.dataset', 'spalah.shared']

package_data = \
{'': ['*']}

install_requires = \
['black==22.3.0',
 'bump2version==1.0.1',
 'coverage==6.4.1',
 'delta-spark==2.1.0',
 'flake8==6.0.0',
 'packaging',
 'pip',
 'pre-commit==2.19.0',
 'pyspark==3.3.0',
 'pytest-cov==3.0.0',
 'pytest==7.1.2',
 'ruff',
 'tox==3.25.0',
 'twine==4.0.1',
 'watchdog==2.1.9',
 'wheel']

setup_kwargs = {
    'name': 'spalah',
    'version': '1.0.0',
    'description': 'Spalah is a set of PySpark dataframe helpers',
    'long_description': '# spalah\n\nSpalah is a set of python helpers to deal with PySpark dataframes, transformations, schemas and Delta Tables.\n\nThe word "spalah" means "spark" in Ukrainian 🇺🇦 \n\n# Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install spalah.\n\n```bash\npip install spalah\n```\n\n# Examples of use\nSpalah currently has two different groups of helpers: `dataframe` and `datalake`.\n\n## spalah.dataframe\n\n### slice_dataframe\n\n```python\nfrom spalah.dataframe import slice_dataframe\n\ndf = spark.sql(\n    \'SELECT 1 as ID, "John" AS Name, struct("line1" AS Line1, "line2" AS Line2) AS Address\'\n)\ndf.printSchema()\n\n""" output:\nroot\n |-- ID: integer (nullable = false)\n |-- Name: string (nullable = false)\n |-- Address: struct (nullable = false)\n |    |-- Line1: string (nullable = false)\n |    |-- Line2: string (nullable = false)\n"""\n\n# Create a new dataframe by cutting of root and nested attributes\ndf_result = slice_dataframe(\n    input_dataframe=df,\n    columns_to_include=["Name", "Address"],\n    columns_to_exclude=["Address.Line2"]\n)\ndf_result.printSchema()\n\n""" output:\nroot\n |-- Name: string (nullable = false)\n |-- Address: struct (nullable = false)\n |    |-- Line1: string (nullable = false)\n"""\n```\n\nBeside of nested regular structs it also supported slicing of structs in arrays, including multiple levels of nesting\n\n\n### flatten_schema\n\n```python\nfrom spalah.dataframe import flatten_schema\n\n# Pass the sample dataframe to get the list of all attributes as single dimension list\nflatten_schema(df_complex_schema.schema)\n\n""" output:\n[\'ID\', \'Name\', \'Address.Line1\', \'Address.Line2\']\n"""\n\n\n# Alternatively, the function can return data types of the attributes\nflatten_schema(\n    schema=df_complex_schema.schema,\n    include_datatype=True\n)\n\n""" output:\n[\n    (\'ID\', \'IntegerType\'),\n    (\'Name\', \'StringType\'),\n    (\'Address.Line1\', \'StringType\'),\n    (\'Address.Line2\', \'StringType\')\n]\n"""\n```\n\n### script_dataframe\n\n```python\nfrom spalah.dataframe import script_dataframe\n\nscript = script_dataframe(df)\n\nprint(script)\n\n""" output:\nfrom pyspark.sql import Row\nimport datetime\nfrom decimal import Decimal\nfrom pyspark.sql.types import *\n\n# Scripted data and schema:\n__data = [Row(ID=1, Name=\'John\', Address=Row(Line1=\'line1\', Line2=\'line2\'))]\n\n__schema = {\'type\': \'struct\', \'fields\': [{\'name\': \'ID\', \'type\': \'integer\', \'nullable\': False, \'metadata\': {}}, {\'name\': \'Name\', \'type\': \'string\', \'nullable\': False, \'metadata\': {}}, {\'name\': \'Address\', \'type\': {\'type\': \'struct\', \'fields\': [{\'name\': \'Line1\', \'type\': \'string\', \'nullable\': False, \'metadata\': {}}, {\'name\': \'Line2\', \'type\': \'string\', \'nullable\': False, \'metadata\': {}}]}, \'nullable\': False, \'metadata\': {}}]}\n\noutcome_dataframe = spark.createDataFrame(__data, StructType.fromJson(__schema))\n"""\n```\n\n### SchemaComparer\n\n```python\nfrom spalah.dataframe import SchemaComparer\n\nschema_comparer = SchemaComparer(\n    source_schema = df_source.schema,\n    target_schema = df_target.schema\n)\n\nschema_comparer.compare()\n\n# The comparison results are stored in the class instance properties `matched` and `not_matched`\n\n# Contains a list of matched columns:\nschema_comparer.matched\n\n""" output:\n[MatchedColumn(name=\'Address.Line1\',  data_type=\'StringType\')]\n"""\n\n# Contains a list of all not matched columns with a reason as description of non-match:\nschema_comparer.not_matched\n\n""" output:\n[\n    NotMatchedColumn(\n        name=\'name\', \n        data_type=\'StringType\', \n        reason="The column exists in source and target schemas but it\'s name is case-mismatched"\n    ),\n    NotMatchedColumn(\n        name=\'ID\', \n        data_type=\'IntegerType <=> StringType\', \n        reason=\'The column exists in source and target schemas but it is not matched by a data type\'\n    ),\n    NotMatchedColumn(\n        name=\'Address.Line2\', \n        data_type=\'StringType\', \n        reason=\'The column exists only in the source schema\'\n    )\n]\n"""\n```\n\n## spalah.dataset\n\n### Get delta table properties\n\n```python\nfrom spalah.dataset import DeltaProperty\n\ndp = DeltaProperty(table_path="/path/dataset")\n\nprint(dp.properties) \n\n# output: \n# {\'delta.deletedFileRetentionDuration\': \'interval 15 days\'}\n```\n\n### Set delta table properties\n\n```python\nrom spalah.dataset import DeltaProperty\n\ndp = DeltaProperty(table_path="/path/dataset")\n\ndp.properties = {\n    "delta.logRetentionDuration": "interval 10 days",\n    "delta.deletedFileRetentionDuration": "interval 15 days"\n}\n\n```\nand the standard output is:\n\n```\n2023-05-20 18:27:42,070 INFO      Applying check constraints on \'delta.`/tmp/nested_schema_dataset`\':\n2023-05-20 18:27:42,071 INFO      Checking if constraint \'id_is_not_null\' was already set on delta.`/tmp/nested_schema_dataset`\n2023-05-20 18:27:42,433 INFO      The constraint id_is_not_null has been successfully added to \'delta.`/tmp/nested_schema_dataset`\n```\n\nPlease note that check constraints can be retrieved and set using property: `.check_constraints`\n\nCheck for more information in [examples: dataframe](docs/examples/dataframe.md), [examples: datalake](docs/examples/dataset.md) pages and related [notebook](docs/usage.ipynb)\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Alex Volok',
    'author_email': 'alexandr.volok@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/avolok/spalah',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
