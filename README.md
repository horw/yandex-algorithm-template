# Template structure
```
my_project/
├── src/
│   └── algorithm.py
└── tests/
    ├── data/
    │   ├── expect/
    │   │   ├── new_expect_file.txt
    │   ├── input/
    │   │   ├── new_input_file.txt
    └── test_main.py
```

1. You should update your [algorithm.py](src%2Falgorithm.py) script.
2. Put the necessary files there [expect](tests%2Fdata%2Fexpect) and [input](tests%2Fdata%2Finput).
3. Run pytest
```bash
pytest
```