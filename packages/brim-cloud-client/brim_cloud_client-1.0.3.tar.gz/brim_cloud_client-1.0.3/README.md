# brim-cloud-client

[![PyPI version](https://badge.fury.io/py/brim-cloud-client.svg)](https://badge.fury.io/py/brim-cloud-client)

BRIM Cloud Client is a minimal implementation of the REST interface used
to communicate with BRIM servers.

## Quick start

### Installation

```bash
pip install brim-cloud-client
```

### Usage - Solve a CNF file

```python
from brim_cloud_client.BRIM import TMB

# Set parameters
tmb_client = TMB(cm=0.9, cb=0.6, p='tmb', Rc=31000, C=49e-15, anneal=0.00011, seed=0)

# Submit cnf file to the server and wait for the results
state, status, results = tmb_client.solve('cust-u500-01.cnf')
print(state, status, results)
```
