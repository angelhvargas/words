Words
--------------
Author: Angel Vargas

Requirements:
-------------
1. Python 3.7

Install:
--------

1. decompress the file word_frequency.zip 
2. navigate to the directory
3. within the project directory, create a virtual python environment and activate it

    run `python3 -m venv venv`
    
    To activate the virtual environment on Windows: 
    
    run `\env\Scripts\activate.bat`
    
    To activate the virtual environment on Linux:
    
    run `source ./python_env/bin/activate`
    
4. Install dependencies
 
    `pip install -r requirements.txt`
    

Testing:
--------

Test can be run from the base dir using `pytest`

    run `pytest -v`

Test Coverage:
--------------

To run and view the test coverage:

    run `pytest --cov=WordsProcessor --cov=WikiClient --cov=WikiAPIClient tests/`
    
once the process finish, open the directory created: `htmlcov`

and open in your preferred browser `index.html` and inspect current test coverage