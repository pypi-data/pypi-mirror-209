# cinipy

cinipy is an app for custom logging.

## Installation

You can install the app using pip:
  
`pip install cinipy`

## Usage

```python
from cinipy import log_info, log_warning, log_error

log_info("This is an info message.")
log_warning({"key": "value", "key2": [1, 2, 3]})
log_error(["error", {"key": "value"}])
```

### Future features

- [ ] Custom Formatting
- [ ] Log handlers
  - [ ] Write logs to a file
  - [ ] Send logs to remote server
  - [ ] Stream to Elasticsearch, logstash, ...
- [ ] More configure options
- [ ] Filtering