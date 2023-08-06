# fxapi Python Client #

Fxapi Python Client is the official Python Wrapper around the fxapi [API](https://fxapi.com/).

## Installation

Install from pip:
````sh
pip install fxapi
````

Install from code:
````sh
pip install git+https://github.com/everapihq/fxapi-python.git
````

## Usage

All curencyapi API requests are made using the `Client` class. This class must be initialized with your API access key string. [Where is my API access key?](https://app.fxapi.com/dashboard)

In your Python application, import `fxapi` and pass authentication information to initialize it:

````python
import fxapi
client = fxapi.Client('API_KEY')
````

### Retrieve Status

```python

print(client.status())

```

### Retrieve Currencies
[https://fxapi.com/docs/currencies](https://fxapi.com/docs/currencies)
```python

result = client.currencies(currencies=['EUR', 'CAD'])
print(result)

```

### Retrieve Latest Exchange Rates
[https://fxapi.com/docs/latest](https://fxapi.com/docs/latest)

```python

result = client.latest()
print(result)

```

### Retrieve Historical Exchange Rates
[https://fxapi.com/docs/historical](https://fxapi.com/docs/historical)

```python

result = client.historical('2022-02-02')
print(result)

```

### Retrieve Historical Range Exchange Rates
[https://fxapi.com/docs/range](https://fxapi.com/docs/range)

```python

result = client.range('2022-02-02', '2022-02-04')
print(result)

```

### Retrieve Converted Exchange Rates
[https://fxapi.com/docs/convert](https://fxapi.com/docs/convert)

```python

result = client.convert(1234)
print(result)

```


### Contact us
Any feedback? Please feel free to [contact our team](mailto:office@everapi.com).
