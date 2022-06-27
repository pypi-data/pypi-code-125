import numpy as np

ACC_ACCURACY_RATE_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 75},
            {"obs": [1.1, 1.2, 6, 0], "fct": [1.4, 10, 0, 0], "result": 75},
            {"obs": [1.1, 1.2, 1.3, 0], "fct": [1.4, 10, 0, 0], "result": 75},
            {"obs": [1.1, 1.2, 1.3, 1], "fct": [1.4, 10, 0, 0], "result": 50},
            {"obs": [1.1, 1.2, 1.3, 1], "fct": [0, 10, 0, 0], "result": 25},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 75},
            {"obs": [2.1, 2.4, 0, 0], "fct": [2.2, 0, 10, 0], "result": 50},
            {"obs": [2.1, 2.4, 2.2, 0], "fct": [2.2, 0, 10, 0], "result": 75},
            {"obs": [2.1, 2.4, 2.2, 3], "fct": [2.2, 0, 10, 0], "result": 50},
            {"obs": [2.1, 2.4, 2.2, 3], "fct": [0, 0, 10, 0], "result": 25},
        ],
    }
}
