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

### Get Services status

```python
from TaqnyatSms import Client

bearer = "**************************0adc2b"
taqnyt = Client(bearer)
status = taqnyt.sendStatus()

print(status)
```

### Get the account balance and status

```python
from TaqnyatSms import Client

bearer = "**************************0adc2b"
taqnyt = Client(bearer)
balance = taqnyt.balance()

print(balance)
```

### Get the account senders

```python
from TaqnyatSms import Client

bearer = "**************************0adc2b"
taqnyt = Client(bearer)
senders = taqnyt.senders()

print(senders)
```

### Send an SMS

```python
# Sending a SMS using Taqnyat API and Python is easy as the following:

from TaqnyatSms import Client

bearer = "**************************0adc2b"
body = "message Content"
recipients = ["966********"]
sender = "Sender Name"

client = Client(bearer)
message = client.sendMsg(body, recipients, sender)

print(message)
```

### Send a scheduled SMS

```python
# Sending a scheduled SMS using Taqnyat API and Python is equally simple:

from TaqnyatSms import Client

bearer = "**************************0adc2b"
body = "message Content"
recipients = ["966********"]
sender = "Sender Name"
scheduled = "2020-09-30T14:26"

taqnyt = Client(bearer)
message = taqnyt.sendMsg(body, recipients, sender, scheduled=scheduled)

print(message)
```


## Getting help

If you need help installing or using the library, please send us email to [Taqnyat Team](mailto:dev@taqnyat.sa) .

If you've instead found a bug in the library or would like new features added, go ahead and send us email , we are welcoming to any suggestion any time

[apidocs]: http://dev.taqnyat.sa
[libdocs]: https://github.com/taqnyat/python/README.md

[![Run on Repl.it](https://repl.it/badge/github/taqnyat/python)]
