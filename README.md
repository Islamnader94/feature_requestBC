### Installing Dependencies

```
pip install -r requirements.txt
```
### Entity relationship Diagram

ERD-Diagram:

![Screenshot](ERD.png)

### Running the App

To run the app, first run the `models.py` file directly to create the database tables:

```
$ python models.py
```

### For pep8 checking:

To install autopep8:

```
$ pip install autopep8==0.8
```

run the following command as the example below ending with .py,
then copy & paste the code to check if there where changes:

```
$ autopep8 models.py
```
### Running the app:
To run the app itself:

```
$ python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser to see the results.

### Running the tests:

To run the Database test:

```
$ python test_base.py
```

To run the api test make sure to run the app.py first:

```
$ python test_api.py
```

To run the server test make sure to run the server.py first:

```
$ python test_server.py
```

### Checking the demo:
To access the demo please visit the link below:

Visit [https://insurance-britecore.herokuapp.com/](https://insurance-britecore.herokuapp.com/) in your browser.
