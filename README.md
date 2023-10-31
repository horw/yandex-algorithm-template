# Template structure
```
my_project/
├── algorithm.py
└── tests/
    ├── data/
    │   ├── expect/
    │   │   └─── new_expect_file.txt
    │   └─── input/
    │       └─── new_input_file.txt
    └── test_main.py
```

1. You should update your [algorithm.py](algorithm.py) script.
2. Put your input in [input.txt](input.txt)

**Enjoy**

Not necessary:
1. Put the tests files there [expect](tests%2Fdata%2Fexpect) and [input](tests%2Fdata%2Finput).
2. Run pytest
```bash
pytest
```