![BeterMaths Banner](https://github.com/Dhaiven/BetterMaths/blob/main/images/banner.png)

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
> [!WARNING]
> This module is in beta phase


## Little documentation
This module add ```Expression``` class that allow resolve expression in string
```python
# Create an expression
expression = Expression("2+7*8cos(3)")
# Resolve this expression
expression.result() # 57.92325394625613
```

### Why use ```Expression``` and not ```eval``` ?
- ```Expression``` is faster than ```eval``` (See [tests/main.py](https://github.com/Dhaiven/BetterMaths/blob/main/tests/main.py))
- ```Expression``` support parenthese, mathematical formulas like ```cos``` and magics numbers like ```π```


### See the [Wiki](https://github.com/Dhaiven/BetterMaths/wiki) for more documentations

## Instalation
Open your terminal and put ```pip install BetterMaths```
<br> For upgrade the version, put ```pip install --upgrade BetterMaths```

## Contribution
BetterMaths accepts community contributions! <br>
This contributions must case no error tests folder.
Launch __init__ file, put ```y``` for take your changes and checks if there are error.

## Authors
  - <img src="https://www.github.com/Dhaiven.png" width="3%" height="3%"/> [@Dhaiven](https://www.github.com/Dhaiven) for code, optimisation and tests
  - <img src="https://www.github.com/algorythmTTV.png" width="3%" height="3%"/> [@algorythmTTV](https://www.github.com/algorythmTTV) for images, site ans code
