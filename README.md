# Taqnyat Python

[![Packagist](https://img.shields.io/badge/Python-v1.0.0-blue)](https://pypi.org/project/Taqnyat/)
[![Packagist](https://img.shields.io/badge/Download-12.4KB-Green)](https://pypi.org/project/Taqnyat/)

## Documentation

The documentation for Taqnyat API can be found [here][apidocs].

## Versions

`Taqnyat` this is a beta version of Taqnyat to support the Python technology , and we will continue adding more features to support the Python community.
### Supported Python Versions

Taqnyat library supports Python 3.0+.

## Installation

You can install **Taqnyat-Python** via pip CLI or by downloading the source.

### Via PIP CLI:

**Taqnyat-Python** is available on Packagist as the
[taqnyat]([![Packagist](https://img.shields.io/badge/repl-White)](https://pypi.org/project/Taqnyat/)
) package:

```
pip install taqnyat
```

## Quickstart
## Usage

First, you need to import the `Client` class from the `taqnyat` package:

```python
from taqnyat import Client

#Then, create a Client object by providing your API key:
client = Client(api_key='YOUR_API_KEY')

```

### Error Handling
If an HTTP request fails, the client will raise an exception by default. To disable this behavior and get the error response as a JSON object, set the raise_exception parameter to False when initializing the client:
```python
from taqnyat import Client

#Then, create a Client object by providing your API key:
client = Client(api_key='YOUR_API_KEY', raise_exception=False)

```
If an HTTP request fails and raise_exception is set to False, you can access the error response as a JSON object by checking the error attribute of the client object:

```python
if client.error:
    print(client.error)
```

### Getting the system status
#### To get the system status, call the send_status method:
```Python
status = client.send_status()
print(status)

```

### Get the account balance and status
#### To get the account balance and status, call the balance method:
```Python
balance = client.balance()
print(balance)

```

### Getting the list of senders
#### To get the list of senders, call the senders method:
```Python
senders = client.senders()
print(senders)

```

### Send an SMS
#### To send an SMS, use the send_msg() method:
```Python
body = 'message Content'
recipients = ['966********']
sender = 'Sender Name'
scheduled=''
delete_id =''
message = client.send_msg(body, recipients, sender,delete_id,scheduled)
print(message)

```
The send_msg() method takes four arguments:
    body (str): the message to send
    recipients (list): a list of phone numbers to send the message to
    sender (str): the sender ID to show on the recipient's phone
    scheduled (str): the date and time to send the message (optional)
    delete_id (int): the ID of a previously sent message to delete (optional)

The send_msg() method returns the JSON object returned by the server.

### Delete a Message
#### To delete a previously sent message, use the delete_msg() method:
```Python
delete_id = 123456789
response = client.delete_msg(delete_id)
print(response)

```


## Getting help

If you need help installing or using the library, please send us email to [Taqnyat Team](mailto:dev@taqnyat.sa) .

If you've instead found a bug in the library or would like new features added, go ahead and send us email , we are welcoming to any suggestion any time

[apidocs]: http://taqnyat.sa/documentation
[libdocs]: https://github.com/taqnyat/python/README.md

## Code Rebuild by Ahmed Elboshi 
### email : ahmedelboshi2@gmail.com