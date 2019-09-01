# foreground
Choose black or white foreground color of text based on background color to get better contrast.
W3C compliant.

![example](https://raw.githubusercontent.com/azaitsev/foreground/master/example.png)

## Installation
```bash
pip install foreground
```

## Usage

### Pass background color to get black or white foreground color

```python
from foreground import get_foreground

get_foreground('#85C1E9')
# '#000000'

get_foreground('#85C1E9', output='RGB') # output as RGB tuple
# (0, 0, 0)

get_foreground((133, 193, 233)) # working with RGB
# '#000000'

get_foreground((133, 193, 233), output='RGB') # RGB input and output
# '#000000'
```