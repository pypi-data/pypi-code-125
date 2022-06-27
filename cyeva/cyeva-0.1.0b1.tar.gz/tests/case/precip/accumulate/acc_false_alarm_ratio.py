import numpy as np

ACC_FALSE_ALARM_RATIO_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 50},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
        ],
        2: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [2.1, 1, 0.4, 0], "fct": [2.2, 0, 10, 0], "result": 50},
            {"obs": [2.1, 0.5, 0, 0], "fct": [2.2, 2.4, 10, 0], "result": 66.67},
            {"obs": [2.1, 0, 10, 0], "fct": [2.2, 2.4, 2.2, 0], "result": 33.33},
            {"obs": [2.2, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 50},
            {"obs": [0, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 75},
        ],
        3: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [5.1, 1, 0.4, 0], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 0.5, 0, 0], "fct": [5.2, 5.4, 10, 0], "result": 66.67},
            {"obs": [5.1, 0, 10, 0], "fct": [5.2, 5.4, 5.2, 0], "result": 33.33},
            {"obs": [5.2, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.1], "result": 50},
            {"obs": [0, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.1], "result": 75},
        ],
        4: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 20, 0], "result": 50},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 20, 0], "result": 66.67},
            {"obs": [10.1, 0, 20, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 33.33},
            {"obs": [10.2, 0, 20, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 50},
            {"obs": [0, 0, 20, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 75},
        ],
        5: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [20.1, 1, 0.4, 0], "fct": [20.2, 0, 30, 0], "result": 50},
            {"obs": [20.1, 0.5, 0, 0], "fct": [20.2, 20.4, 30, 0], "result": 66.67},
            {"obs": [20.1, 0, 30, 0], "fct": [20.2, 20.4, 20.2, 0], "result": 33.33},
            {"obs": [20.2, 0, 30, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 50},
            {"obs": [0, 0, 30, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 75},
        ],
    },
    "3h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 50},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
        ],
        2: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [3.1, 1, 0.4, 0], "fct": [3.2, 0, 10, 0], "result": 50},
            {"obs": [3.1, 0.5, 0, 0], "fct": [3.2, 3.4, 10, 0], "result": 66.67},
            {"obs": [3.1, 0, 10, 0], "fct": [3.2, 3.4, 3.2, 0], "result": 33.33},
            {"obs": [3.2, 0, 10, 0], "fct": [3.1, 3.4, 3.2, 3], "result": 50},
            {"obs": [0, 0, 10, 0], "fct": [3.1, 3.4, 3.2, 3], "result": 75},
        ],
        3: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 20, 0], "result": 50},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 20, 0], "result": 66.67},
            {"obs": [10.1, 0, 20, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 33.33},
            {"obs": [10.2, 0, 20, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 50},
            {"obs": [0, 0, 20, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 75},
        ],
        4: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [20.1, 1, 0.4, 0], "fct": [20.2, 0, 50, 0], "result": 50},
            {"obs": [20.1, 0.5, 0, 0], "fct": [20.2, 20.4, 50, 0], "result": 66.67},
            {"obs": [20.1, 0, 50, 0], "fct": [20.2, 20.4, 20.2, 0], "result": 33.33},
            {"obs": [20.2, 0, 50, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 50},
            {"obs": [0, 0, 50, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 75},
        ],
        5: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [50.1, 1, 0.4, 0], "fct": [50.2, 0, 70, 0], "result": 50},
            {"obs": [50.1, 0.5, 0, 0], "fct": [50.2, 50.4, 70, 0], "result": 66.67},
            {"obs": [50.1, 0, 70, 0], "fct": [50.2, 50.4, 50.2, 0], "result": 33.33},
            {"obs": [50.2, 0, 70, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 50},
            {"obs": [0, 0, 70, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 75},
        ],
        6: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [70.1, 1, 0.4, 0], "fct": [70.2, 0, 90, 0], "result": 50},
            {"obs": [70.1, 0.5, 0, 0], "fct": [70.2, 70.4, 90, 0], "result": 66.67},
            {"obs": [70.1, 0, 90, 0], "fct": [70.2, 70.4, 70.2, 0], "result": 33.33},
            {"obs": [70.2, 0, 90, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 50},
            {"obs": [0, 0, 90, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 75},
        ],
    },
    "12h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 50},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
        ],
        2: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [5.1, 1, 0.4, 0], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 0.5, 0, 0], "fct": [5.2, 5.4, 10, 0], "result": 66.67},
            {"obs": [5.1, 0, 10, 0], "fct": [5.2, 5.4, 5.2, 0], "result": 33.33},
            {"obs": [5.2, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5], "result": 50},
            {"obs": [0, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5], "result": 75},
        ],
        3: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [15.1, 1, 0.4, 0], "fct": [15.2, 0, 20, 0], "result": 50},
            {"obs": [15.1, 0.5, 0, 0], "fct": [15.2, 15.4, 20, 0], "result": 66.67},
            {"obs": [15.1, 0, 20, 0], "fct": [15.2, 15.4, 15.2, 0], "result": 33.33},
            {"obs": [15.2, 0, 20, 0], "fct": [15.1, 15.4, 15.2, 15.1], "result": 50},
            {"obs": [0, 0, 20, 0], "fct": [15.1, 15.4, 15.2, 15.1], "result": 75},
        ],
        4: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [30.1, 1, 0.4, 0], "fct": [30.2, 0, 50, 0], "result": 50},
            {"obs": [30.1, 0.5, 0, 0], "fct": [30.2, 30.4, 50, 0], "result": 66.67},
            {"obs": [30.1, 0, 50, 0], "fct": [30.2, 30.4, 30.2, 0], "result": 33.33},
            {"obs": [30.2, 0, 50, 0], "fct": [30.1, 30.4, 30.2, 30.1], "result": 50},
            {"obs": [0, 0, 50, 0], "fct": [30.1, 30.4, 30.2, 30.1], "result": 75},
        ],
        5: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [70.1, 1, 0.4, 0], "fct": [70.2, 0, 70, 0], "result": 50},
            {"obs": [70.1, 0.5, 0, 0], "fct": [70.2, 70.4, 70, 0], "result": 66.67},
            {"obs": [70.1, 0, 70, 0], "fct": [70.2, 70.4, 70.2, 0], "result": 33.33},
            {"obs": [70.2, 0, 70, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 50},
            {"obs": [0, 0, 70, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 75},
        ],
        6: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [140.1, 1, 0.4, 0], "fct": [140.2, 0, 160, 0], "result": 50},
            {"obs": [140.1, 0.5, 0, 0], "fct": [140.2, 140.4, 160, 0], "result": 66.67},
            {
                "obs": [140.1, 0, 160, 0],
                "fct": [140.2, 140.4, 140.2, 0],
                "result": 33.33,
            },
            {
                "obs": [140.2, 0, 160, 0],
                "fct": [140.1, 140.4, 140.2, 140.1],
                "result": 50,
            },
            {"obs": [0, 0, 160, 0], "fct": [140.1, 140.4, 140.2, 140.1], "result": 75},
        ],
    },
    "12h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 33.33},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 50},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
        ],
        2: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 10, 0], "result": 66.67},
            {"obs": [10.1, 0, 10, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 33.33},
            {"obs": [10.2, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.0], "result": 50},
            {"obs": [0, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.0], "result": 75},
        ],
        3: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [25.1, 1, 0.4, 0], "fct": [25.2, 0, 20, 0], "result": 50},
            {"obs": [25.1, 0.5, 0, 0], "fct": [25.2, 25.4, 20, 0], "result": 66.67},
            {"obs": [25.1, 0, 20, 0], "fct": [25.2, 25.4, 25.2, 0], "result": 33.33},
            {"obs": [25.2, 0, 20, 0], "fct": [25.1, 25.4, 25.2, 25.1], "result": 50},
            {"obs": [0, 0, 20, 0], "fct": [25.1, 25.4, 25.2, 25.1], "result": 75},
        ],
        4: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [50.1, 1, 0.4, 0], "fct": [50.2, 0, 50, 0], "result": 50},
            {"obs": [50.1, 0.5, 0, 0], "fct": [50.2, 50.4, 50, 0], "result": 66.67},
            {"obs": [50.1, 0, 50, 0], "fct": [50.2, 50.4, 50.2, 0], "result": 33.33},
            {"obs": [50.2, 0, 50, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 50},
            {"obs": [0, 0, 50, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 75},
        ],
        5: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [100.1, 1, 0.4, 0], "fct": [100.2, 0, 100, 0], "result": 50},
            {"obs": [100.1, 0.5, 0, 0], "fct": [100.2, 100.4, 100, 0], "result": 66.67},
            {
                "obs": [100.1, 0, 100, 0],
                "fct": [100.2, 100.4, 100.2, 0],
                "result": 33.33,
            },
            {
                "obs": [100.2, 0, 100, 0],
                "fct": [100.1, 100.4, 100.2, 100.1],
                "result": 50,
            },
            {"obs": [0, 0, 100, 0], "fct": [100.1, 100.4, 100.2, 100.1], "result": 75},
        ],
        6: [
            {"obs": [1.1, 1, 0.4, 0], "fct": [1.2, 0, 0, 0], "result": np.nan},
            {"obs": [250.1, 1, 0.4, 0], "fct": [250.2, 0, 260, 0], "result": 50},
            {"obs": [250.1, 0.5, 0, 0], "fct": [250.2, 250.4, 260, 0], "result": 66.67},
            {
                "obs": [250.1, 0, 260, 0],
                "fct": [250.2, 250.4, 250.2, 0],
                "result": 33.33,
            },
            {
                "obs": [250.2, 0, 260, 0],
                "fct": [250.1, 250.4, 250.2, 250.1],
                "result": 50,
            },
            {"obs": [0, 0, 260, 0], "fct": [250.1, 250.4, 250.2, 250.1], "result": 75},
        ],
    },
}

ACC_FALSE_ALARM_RATE_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 100},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [2.1, 1, 0.4, 0], "fct": [2.2, 0, 10, 0], "result": 33.33},
            {"obs": [2.1, 0.5, 0, 0], "fct": [2.2, 2.4, 10, 0], "result": 66.67},
            {"obs": [2.1, 0, 10, 0], "fct": [2.2, 2.4, 2.2, 0], "result": 50},
            {"obs": [2.2, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 100},
        ],
        3: [
            {"obs": [5.1, 1, 0.4, 0], "fct": [5.2, 0, 10, 0], "result": 33.33},
            {"obs": [5.1, 0.5, 0, 0], "fct": [5.2, 5.4, 10, 0], "result": 66.67},
            {"obs": [5.1, 0, 10, 0], "fct": [5.2, 5.4, 5.2, 0], "result": 50},
            {"obs": [5.2, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.1], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.1], "result": 100},
        ],
        4: [
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 10, 0], "result": 66.67},
            {"obs": [10.1, 0, 10, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 50},
            {"obs": [10.2, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 100},
        ],
        5: [
            {"obs": [20.1, 1, 0.4, 0], "fct": [20.2, 0, 20, 0], "result": 33.33},
            {"obs": [20.1, 0.5, 0, 0], "fct": [20.2, 20.4, 20, 0], "result": 66.67},
            {"obs": [20.1, 0, 20, 0], "fct": [20.2, 20.4, 20.2, 0], "result": 50},
            {"obs": [20.2, 0, 20, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 100},
            {"obs": [0, 0, 20, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 100},
        ],
    },
    "3h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 100},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [3.1, 1, 0.4, 0], "fct": [3.2, 0, 10, 0], "result": 33.33},
            {"obs": [3.1, 0.5, 0, 0], "fct": [3.2, 3.4, 10, 0], "result": 66.67},
            {"obs": [3.1, 0, 10, 0], "fct": [3.2, 3.4, 3.2, 0], "result": 50},
            {"obs": [3.2, 0, 10, 0], "fct": [3.1, 3.4, 3.2, 3], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [3.1, 3.4, 3.2, 3], "result": 100},
        ],
        3: [
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 10, 0], "result": 66.67},
            {"obs": [10.1, 0, 10, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 50},
            {"obs": [10.2, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.1], "result": 100},
        ],
        4: [
            {"obs": [20.1, 1, 0.4, 0], "fct": [20.2, 0, 20, 0], "result": 33.33},
            {"obs": [20.1, 0.5, 0, 0], "fct": [20.2, 20.4, 20, 0], "result": 66.67},
            {"obs": [20.1, 0, 20, 0], "fct": [20.2, 20.4, 20.2, 0], "result": 50},
            {"obs": [20.2, 0, 20, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 100},
            {"obs": [0, 0, 20, 0], "fct": [20.1, 20.4, 20.2, 20.1], "result": 100},
        ],
        5: [
            {"obs": [50.1, 1, 0.4, 0], "fct": [50.2, 0, 50, 0], "result": 33.33},
            {"obs": [50.1, 0.5, 0, 0], "fct": [50.2, 50.4, 50, 0], "result": 66.67},
            {"obs": [50.1, 0, 50, 0], "fct": [50.2, 50.4, 50.2, 0], "result": 50},
            {"obs": [50.2, 0, 50, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 100},
            {"obs": [0, 0, 50, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 100},
        ],
        6: [
            {"obs": [70.1, 1, 0.4, 0], "fct": [70.2, 0, 80, 0], "result": 33.33},
            {"obs": [70.1, 0.5, 0, 0], "fct": [70.2, 70.4, 80, 0], "result": 66.67},
            {"obs": [70.1, 0, 80, 0], "fct": [70.2, 70.4, 70.2, 0], "result": 50},
            {"obs": [70.2, 0, 80, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 100},
            {"obs": [0, 0, 80, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 100},
        ],
    },
    "12h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 100},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [5.1, 1, 0.4, 0], "fct": [5.2, 0, 10, 0], "result": 33.33},
            {"obs": [5.1, 0.5, 0, 0], "fct": [5.2, 5.4, 10, 0], "result": 66.67},
            {"obs": [5.1, 0, 10, 0], "fct": [5.2, 5.4, 5.2, 0], "result": 50},
            {"obs": [5.2, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.3], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [5.1, 5.4, 5.2, 5.3], "result": 100},
        ],
        3: [
            {"obs": [15.1, 1, 0.4, 0], "fct": [15.2, 0, 20, 0], "result": 33.33},
            {"obs": [15.1, 0.5, 0, 0], "fct": [15.2, 15.4, 20, 0], "result": 66.67},
            {"obs": [15.1, 0, 20, 0], "fct": [15.2, 15.4, 15.2, 0], "result": 50},
            {"obs": [15.2, 0, 20, 0], "fct": [15.1, 15.4, 15.2, 15.1], "result": 100},
            {"obs": [0, 0, 20, 0], "fct": [15.1, 15.4, 15.2, 15.1], "result": 100},
        ],
        4: [
            {"obs": [30.1, 1, 0.4, 0], "fct": [30.2, 0, 40, 0], "result": 33.33},
            {"obs": [30.1, 0.5, 0, 0], "fct": [30.2, 30.4, 40, 0], "result": 66.67},
            {"obs": [30.1, 0, 40, 0], "fct": [30.2, 30.4, 30.2, 0], "result": 50},
            {"obs": [30.2, 0, 40, 0], "fct": [30.1, 30.4, 30.2, 30.1], "result": 100},
            {"obs": [0, 0, 40, 0], "fct": [30.1, 30.4, 30.2, 30.1], "result": 100},
        ],
        5: [
            {"obs": [70.1, 1, 0.4, 0], "fct": [70.2, 0, 70, 0], "result": 33.33},
            {"obs": [70.1, 0.5, 0, 0], "fct": [70.2, 70.4, 70, 0], "result": 66.67},
            {"obs": [70.1, 0, 70, 0], "fct": [70.2, 70.4, 70.2, 0], "result": 50},
            {"obs": [70.2, 0, 70, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 100},
            {"obs": [0, 0, 70, 0], "fct": [70.1, 70.4, 70.2, 70.1], "result": 100},
        ],
        6: [
            {"obs": [140.1, 1, 0.4, 0], "fct": [140.2, 0, 160, 0], "result": 33.33},
            {"obs": [140.1, 0.5, 0, 0], "fct": [140.2, 140.4, 160, 0], "result": 66.67},
            {"obs": [140.1, 0, 160, 0], "fct": [140.2, 140.4, 140.2, 0], "result": 50},
            {
                "obs": [140.2, 0, 160, 0],
                "fct": [140.1, 140.4, 140.2, 140.1],
                "result": 100,
            },
            {"obs": [0, 0, 160, 0], "fct": [140.1, 140.4, 140.2, 140.1], "result": 100},
        ],
    },
    "24h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 2], "result": 100},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [10.1, 1, 0.4, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 0.5, 0, 0], "fct": [10.2, 10.4, 10, 0], "result": 66.67},
            {"obs": [10.1, 0, 10, 0], "fct": [10.2, 10.4, 10.2, 0], "result": 50},
            {"obs": [10.2, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.3], "result": 100},
            {"obs": [0, 0, 10, 0], "fct": [10.1, 10.4, 10.2, 10.3], "result": 100},
        ],
        3: [
            {"obs": [25.1, 1, 0.4, 0], "fct": [25.2, 0, 30, 0], "result": 33.33},
            {"obs": [25.1, 0.5, 0, 0], "fct": [25.2, 25.4, 30, 0], "result": 66.67},
            {"obs": [25.1, 0, 30, 0], "fct": [25.2, 25.4, 25.2, 0], "result": 50},
            {"obs": [25.2, 0, 30, 0], "fct": [25.1, 25.4, 25.2, 25.1], "result": 100},
            {"obs": [0, 0, 30, 0], "fct": [25.1, 25.4, 25.2, 25.1], "result": 100},
        ],
        4: [
            {"obs": [50.1, 1, 0.4, 0], "fct": [50.2, 0, 55, 0], "result": 33.33},
            {"obs": [50.1, 0.5, 0, 0], "fct": [50.2, 50.4, 55, 0], "result": 66.67},
            {"obs": [50.1, 0, 55, 0], "fct": [50.2, 50.4, 50.2, 0], "result": 50},
            {"obs": [50.2, 0, 55, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 100},
            {"obs": [0, 0, 55, 0], "fct": [50.1, 50.4, 50.2, 50.1], "result": 100},
        ],
        5: [
            {"obs": [100.1, 1, 0.4, 0], "fct": [100.2, 0, 100, 0], "result": 33.33},
            {"obs": [100.1, 0.5, 0, 0], "fct": [100.2, 100.4, 100, 0], "result": 66.67},
            {"obs": [100.1, 0, 100, 0], "fct": [100.2, 100.4, 100.2, 0], "result": 50},
            {"obs": [100.2, 0, 100, 0], "fct": [100.1, 100.4, 100.2, 100.1], "result": 100},
            {"obs": [0, 0, 100, 0], "fct": [100.1, 100.4, 100.2, 100.1], "result": 100},
        ],
        6: [
            {"obs": [250.1, 1, 0.4, 0], "fct": [250.2, 0, 260, 0], "result": 33.33},
            {"obs": [250.1, 0.5, 0, 0], "fct": [250.2, 250.4, 260, 0], "result": 66.67},
            {"obs": [250.1, 0, 260, 0], "fct": [250.2, 250.4, 250.2, 0], "result": 50},
            {
                "obs": [250.2, 0, 260, 0],
                "fct": [250.1, 250.4, 250.2, 250.1],
                "result": 100,
            },
            {"obs": [0, 0, 260, 0], "fct": [250.1, 250.4, 250.2, 250.1], "result": 100},
        ],
    },
}
