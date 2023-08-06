# Emailvalidation Python Client #

Emailvalidation Python Client is the official Python Wrapper around the Emailvalidation [API](https://emailvalidation.io/).

## Installation

Install from pip:
````sh
pip install emailvalidation
````

Install from code:
````sh
pip install git+https://github.com/everapihq/emailvalidation-python.git
````

## Usage

All emailvalidation API requests are made using the `Client` class. This class must be initialized with your API access key string. [Where is my API access key?](https://app.emailvalidation.io/dashboard)

In your Python application, import `emailvalidation` and pass authentication information to initialize it:

````python
import emailvalidation
client = emailvalidation.Client('API_KEY')
````

### Retrieve Status

```python

print(client.status())

```

### Validate Email Address
[https://emailvalidation.io/docs/info](https://emailvalidation.io/docs/info)
```python

result = client.info('john@doe.com')
# result = client.info('john@doe.com', catch_all=1)
print(result)

```


### Contact us
Any feedback? Please feel free to [contact our team](mailto:office@everapi.com).
