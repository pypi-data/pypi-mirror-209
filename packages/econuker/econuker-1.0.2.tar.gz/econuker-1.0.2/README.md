# EcoNuker-API

EcoNuker-API is a Python library for interacting with the EcoNuker API, which provides tools for managing and controlling Eco servers.

## Installation

You can install the EcoNuker-API library using pip:

`pip install econuker`

## Usage

WARNING: The MAIN API is not available for use until June 1, 2023.

Please use the BETA version. Beta=True.

### Example

```python
# Python Example
from econuker import Client
beta = True # False
authtoken = None # "your auth token here"

if __name__ == "__main__":
    client = Client(auth_token=authtoken, beta=beta)
    status = client.status()
    print(status.name)
```

### Async Example
```python
# Python Async Example
from econuker import AsyncClient
beta = True # False
authtoken = None # "your auth token here"

if __name__ == "__main__":
    client = AsyncClient(auth_token=authtoken, beta=beta)
    async def asyncfunction():
        status = await client.status()
        print(status.name)
        return status
    asyncio.run(asyncfunction())
```


Documentation
For detailed documentation on the EcoNuker API, read https://docs.econuker.xyz/

For detailed documentation on how to use the EcoNuker-API library, please wait while we write it lol.

License
This project is licensed under the MIT License. See the LICENSE file for details.