# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_mssql']

package_data = \
{'': ['*']}

install_requires = \
['grai-client>=0.2.0,<0.3.0',
 'grai-schemas>=0.1.8,<0.2.0',
 'multimethod>=1.8,<2.0',
 'pydantic>=1.9.1,<2.0.0',
 'pyodbc>=4.0.35,<5.0.0']

setup_kwargs = {
    'name': 'grai-source-mssql',
    'version': '0.0.10',
    'description': '',
    'long_description': '# Grai SQL Server Integration\n\nThe SQL Server integration synchronizes metadata from your SQL Server database into your Grai data lineage graph.\n\nTests assume you have working installation of pyodbc and a supported\nODBC driver installed on your host machine.\n\n## Installation Notes\n\nInstalling ODBC drivers can be particularly tricky on M1 machines.\nYou\'ll need to install the unixodbc drivers through brew first\n\n```bash\n    brew install unixodbc\n```\n\nYou can attempt installing pyodbc directly at this point though I was forced to\nset LDFLAGS and CPPFlags in my bashrc/zshrc file, i.e.\n\n```bash\nexport LDFLAGS="$LDFLAGS -L$(brew --prefix unixodbc)/lib"\nexport CPPFLAGS="$CPPFLAGS -I$(brew --prefix unixodbc)/include"\n```\n\nAt this point you should be able to `pip install pyodbc` successfully\nand import the package from within python. However, you\'ll still require an\nODBC driver in order to connect with an MS SQL server. There are multiple options\nfor potential drivers but ODBC 18 from Microsoft has worked in testing.\n\n```bash\nbrew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release\nbrew update\nHOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18\n```\n\nIf you continue to experience issues you might try creating these symlinks\nbelow.\n\n```\nsudo ln -s /opt/homebrew/etc/odbcinst.ini /etc/odbcinst.ini\nsudo ln -s /opt/homebrew/etc/odbc.ini /etc/odbc.ini\n```\n\nWhen installing locally, if you get an error like `ImportError: dlopen(/opt/homebrew/lib/python3.11/site-packages/pyodbc.cpython-311-darwin.so, 0x0002): symbol not found in flat namespace (_SQLAllocHandle)`, you can try uninstalling `pip uninstall pyodbc` and then reinstall with build `pip install --no-binary :all: pyodbc`.\n',
    'author': 'Ian Eaves',
    'author_email': 'ian@grai.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.grai.io/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
