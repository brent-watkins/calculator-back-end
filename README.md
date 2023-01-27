# calculator-back-end

This is the back-end server for the Web Calculator web application.
To run the website locally, follow the Project Setup and Run Development Server commands.

## Project Setup

Create a virtual environment.
[Here](https://docs.python.org/3/library/venv.html) is the documentation on `venv` and how to use it.

Note: You may need to use `py` instead of `python` if you are using a Windows machine

```sh
python -m venv <your-venv-name>
```

Enter the new directory your virtual environment is in

```sh
cd ./<your-venv-name>/
```

Activate your virtual environment using one of the commands found [here](https://docs.python.org/3/library/venv.html#how-venvs-work), depending on your operating system.

Once you have activated your virtual environment, clone the repository.

```sh
git clone https://github.com/brent-watkins/calculator-back-end.git
```

Enter the repository directory and install the necessary packages

```sh
cd ./calculator-back-end/
pip install -r requirements.txt
```

## Run Development Server

```sh
python manage.py runserver
```

After running these commands, the server URL will be http://127.0.0.1:8000/

## API

The API endpoints can be accessed through http://127.0.0.1:8000/api/_endpoint_/

All endpoints accept JSON encoded request bodies.

The supported endpoints are currently:

### Add

http://127.0.0.1:8000/api/add/

Receive the sum of a list of numeric operands.

**POST**

The request body must include the following:

- operands: A List or Array of numeric values or Strings that can be parsed as float values
- username: A String of your username

```javascript
{
  "operands": List<Number | String> | Array<Number | String>,
  "username": String,
}
```

The response will be the sum of all operands, having a type of `Number` or `float`

### Balance

http://127.0.0.1:8000/api/balance/

Receive or set the current balance of a User.

**POST**

Receive the current balance of a User.

The request body must include the following:

- username: A String of your username

```javascript
{
  "username": String,
}
```

The response will be the current balance of the User.

**PUT**

Set the current balance of a User.

The request body must include the following:

- balance: A Decimal value between 0 and 999999.99
- username: A String of your username

```javascript
{
  "balance": Decimal | Number,
  "username": String,
}
```

No data is returned.

### Divide

http://127.0.0.1:8000/api/divide/

Receive the quotient of a list of numeric operands.

**POST**

The request body must include the following:

- operands: A List or Array of numeric values or Strings that can be parsed as float values
- username: A String of your username

```javascript
{
  "operands": List<Number | String> | Array<Number | String>,
  "username": String,
}
```

The response will be the sum of all operands, having a type of `Number` or `float`

### Log In

http://127.0.0.1:8000/api/login/

Authenticate user credentials to access operations.

**POST**

The request body must include the following:

- password: A String of your password
- username: A String of your username

```javascript
{
  "password": String,
  "username": String,
}
```

The response will be the username if the login attempt was successful.

### Log Out

http://127.0.0.1:8000/api/logout/

End authenticated session

**POST**

The request body must include the following:

- username: A String of your username

```javascript
{
  "username": String,
}
```

The response will be the username if the logout attempt was successful.

### Multiply

http://127.0.0.1:8000/api/multiply/

Receive the product of a list of numeric operands.

**POST**

The request body must include the following:

- operands: A List or Array of numeric values or Strings that can be parsed as float values
- username: A String of your username

```javascript
{
  "operands": List<Number | String> | Array<Number | String>,
  "username": String,
}
```

The response will be the sum of all operands, having a type of `Number` or `float`

### Random String

http://127.0.0.1:8000/api/random_string/

Receive a random String comprised of letters and numbers.

**POST**

The request body must include the following:

- username: A String of your username

```javascript
{
  "username": String,
}
```

The response will be a String that is 20 characters long and comprised of letters and numbers.

### Records

http://127.0.0.1:8000/api/records/

Request or soft-delete Records of operations a user has made.

**POST**

Request all Records of operations a user has made.

The request body must include the following:

- username: A String of your username

```javascript
{
  "username": String,
}
```

The response will be a List or Array of dictionaries with Record information.

**PUT**

Soft-delete a specified Record.

The request body must include the following:

- record: An Integer identifying which Record to soft-delete
- username: A String of your username

```javascript
{
  "record": Integer,
  "username": String,
}
```

### Register

http://127.0.0.1:8000/api/register/

Register a new User account.

**PUT**

The request body must include the following:

- balance: A Decimal value between 0.00 and 999999.99
- password: A String of your password
- status: "I". Represents inactive User status.
- username: A String of your username

```javascript
{
  "balance": Decimal | Number,
  "password": String,
  "status": String,
  "username": String,
}
```

The response will be a String indicating whether or not a new account was registered.

### Square Root

http://127.0.0.1:8000/api/square_root/

Receive the square root of a positive numeric operand.

**POST**

The request body must include the following:

- operands: A List or Array of a numeric value or String that can be parsed as a float value
- username: A String of your username

```javascript
{
  "operands": List<Number | String> | Array<Number | String>,
  "username": String,
}
```

The response will be the square root of the first operand in the List or Array.

### Subtract

http://127.0.0.1:8000/api/subtract/

Receive the difference of a list of numeric operands.

**POST**

The request body must include the following:

- operands: A List or Array of numeric values or Strings that can be parsed as float values
- username: A String of your username

```javascript
{
  "operands": List<Number | String> | Array<Number | String>,
  "username": String,
}
```

The response will be the sum of all operands, having a type of `Number` or `float`

## Testing

To run tests, navigate to the directory with `manage.py`.
From this directory enter the following command into a command prompt / bash:

```sh
python manage.py test
```
