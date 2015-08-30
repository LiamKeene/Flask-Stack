# Flask Stack (WSGI)
Flask Stack is the base Flask application template I use with mod_wsgi, and 
contains all the elements to create a simple Flask app with tests and 
deployment scripts built-in.

## Packages 
* Flask
* pytest
* pytest-flask

Also assumes you already have [pyenv](https://github.com/yyuu/pyenv.git) and 
the [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) plugin installed.

## Installation

1. Checkout Flask-Stack where you want it installed.
    ```bash
    $ git clone https://github.com/LiamKeene/Flask-Stack ~/projects/my-project
    ```

2. Rename instances of `appname` to `my_project`.
    In future I hope to have this templated or similar.
    ```bash
    $ find . -type f -name "*.py*" -exec sed -i 's/appname/my_project/g' {} +
    ```
    **Note** the underscore in `my_project`.  The hyphen looks better as a filename
    (personal preference), but Python will need underscores for imports, etc.

3. Create the virtual environment for your project and activate it.
    This assumes you have already installed Python 2.7.10 via pyenv.  See 
    [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) for detailed
    instructions.
    ```bash
    $ pyenv virtualenv 2.7.10 my-project-env
    $ pyenv activate my-project-env
    ``` 

4. Install required packages.
    ```bash
    $ pip install -r requirements.txt
    ```

5. Check all tests pass.
    ```bash
    $ cd ~/projects/my-project
    $ py.test -v
    ```

6. Hack away!

7. (Optional) Configuration of Apache/mod_wsgi server.
    Will update this for more detailed information for pushing to a git 
    server, checking out code to a work-tree for live/dev/testing purposes.  
    If all that is done, the Apache httpd.conf will need these lines.

    ```apache
    WSGIDaemonProcess project processes=2 threads=12 python-path=/home/username/.pyenv/versions/my-project-env/lib/python2.7/site-packages
    WSGIScriptAlias / /path/to/app/wsgi.py
    ```