import numpy as np

LEV_FALSE_ALARM_RATIO_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 66.67},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [2.1, 5, 6, 0], "fct": [2.4, 10, 0, 0], "result": 0},
            {"obs": [2.1, 10, 6, 0], "fct": [2.4, 2.2, 0, 0], "result": 50},
            {"obs": [2.4, 10, 0, 0], "fct": [2.1, 2.2, 2.3, 0], "result": 66.67},
            {"obs": [2.4, 10, 0, 0], "fct": [2.1, 2.2, 2.3, 2.1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [2.1, 2.2, 2.3, 2.1], "result": 100},
        ],
        3: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [5.1, 5, 6, 0], "fct": [5.4, 10, 0, 0], "result": 0},
            {"obs": [5.1, 10, 6, 0], "fct": [5.4, 5.2, 0, 0], "result": 50},
            {"obs": [5.4, 10, 0, 0], "fct": [5.1, 5.2, 5.3, 0], "result": 66.67},
            {"obs": [5.4, 10, 0, 0], "fct": [5.1, 5.2, 5.3, 5.1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [5.1, 5.2, 5.3, 5.1], "result": 100},
        ],
        4: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 30, 0, 0], "result": np.nan},
            {"obs": [10.1, 5, 6, 0], "fct": [10.4, 30, 0, 0], "result": 0},
            {"obs": [10.1, 30, 6, 0], "fct": [10.4, 10.2, 0, 0], "result": 50},
            {"obs": [10.4, 30, 0, 0], "fct": [10.1, 10.2, 10.3, 0], "result": 66.67},
            {"obs": [10.4, 30, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 75},
            {"obs": [0, 30, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 100},
        ],
        5: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [20.1, 5, 6, 0], "fct": [20.4, 10, 0, 0], "result": 0},
            {"obs": [20.1, 10, 6, 0], "fct": [20.4, 20.2, 0, 0], "result": 50},
            {"obs": [20.4, 10, 0, 0], "fct": [20.1, 20.2, 20.3, 0], "result": 66.67},
            {"obs": [20.4, 10, 0, 0], "fct": [20.1, 20.2, 20.3, 20.1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [20.1, 20.2, 20.3, 20.1], "result": 100},
        ],
    },
    "3h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 66.67},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [3.1, 5, 6, 0], "fct": [3.4, 10, 0, 0], "result": 0},
            {"obs": [3.1, 10, 6, 0], "fct": [3.4, 3.2, 0, 0], "result": 50},
            {"obs": [3.4, 10, 0, 0], "fct": [3.1, 3.2, 3.3, 0], "result": 66.67},
            {"obs": [3.4, 10, 0, 0], "fct": [3.1, 3.2, 3.3, 3.1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [3.1, 3.2, 3.3, 3.1], "result": 100},
        ],
        3: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [10.1, 5, 6, 0], "fct": [10.4, 80, 0, 0], "result": 0},
            {"obs": [10.1, 80, 6, 0], "fct": [10.4, 10.2, 0, 0], "result": 50},
            {"obs": [10.4, 80, 0, 0], "fct": [10.1, 10.2, 10.3, 0], "result": 66.67},
            {"obs": [10.4, 80, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 100},
        ],
        4: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [20.1, 5, 6, 0], "fct": [20.4, 80, 0, 0], "result": 0},
            {"obs": [20.1, 80, 6, 0], "fct": [20.4, 20.2, 0, 0], "result": 50},
            {"obs": [20.4, 80, 0, 0], "fct": [20.1, 20.2, 20.3, 0], "result": 66.67},
            {"obs": [20.4, 80, 0, 0], "fct": [20.1, 20.2, 20.3, 20.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [20.1, 20.2, 20.3, 20.1], "result": 100},
        ],
        5: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [50.1, 5, 6, 0], "fct": [50.4, 80, 0, 0], "result": 0},
            {"obs": [50.1, 80, 6, 0], "fct": [50.4, 50.2, 0, 0], "result": 50},
            {"obs": [50.4, 80, 0, 0], "fct": [50.1, 50.2, 50.3, 0], "result": 66.67},
            {"obs": [50.4, 80, 0, 0], "fct": [50.1, 50.2, 50.3, 50.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [50.1, 50.2, 50.3, 50.1], "result": 100},
        ],
        6: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [70.1, 5, 6, 0], "fct": [70.4, 10, 0, 0], "result": 0},
            {"obs": [70.1, 10, 6, 0], "fct": [70.4, 70.2, 0, 0], "result": 50},
            {"obs": [70.4, 10, 0, 0], "fct": [70.1, 70.2, 70.3, 0], "result": 66.67},
            {"obs": [70.4, 10, 0, 0], "fct": [70.1, 70.2, 70.3, 70.1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [70.1, 70.2, 70.3, 70.1], "result": 100},
        ],
    },
    "12h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 66.67},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 150, 0, 0], "result": np.nan},
            {"obs": [5.1, 5, 6, 0], "fct": [5.4, 150, 0, 0], "result": 0},
            {"obs": [5.1, 150, 6, 0], "fct": [5.4, 5.2, 0, 0], "result": 50},
            {"obs": [5.4, 150, 0, 0], "fct": [5.1, 5.2, 5.3, 0], "result": 66.67},
            {"obs": [5.4, 150, 0, 0], "fct": [5.1, 5.2, 5.3, 5.1], "result": 75},
            {"obs": [0, 150, 0, 0], "fct": [5.1, 5.2, 5.3, 5.1], "result": 100},
        ],
        3: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [15.1, 5, 6, 0], "fct": [15.4, 80, 0, 0], "result": 0},
            {"obs": [15.1, 80, 6, 0], "fct": [15.4, 15.2, 0, 0], "result": 50},
            {"obs": [15.4, 80, 0, 0], "fct": [15.1, 15.2, 15.3, 0], "result": 66.67},
            {"obs": [15.4, 80, 0, 0], "fct": [15.1, 15.2, 15.3, 15.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [15.1, 15.2, 15.3, 15.1], "result": 100},
        ],
        4: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [30.1, 5, 6, 0], "fct": [30.4, 80, 0, 0], "result": 0},
            {"obs": [30.1, 80, 6, 0], "fct": [30.4, 30.2, 0, 0], "result": 50},
            {"obs": [30.4, 80, 0, 0], "fct": [30.1, 30.2, 30.3, 0], "result": 66.67},
            {"obs": [30.4, 80, 0, 0], "fct": [30.1, 30.2, 30.3, 30.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [30.1, 30.2, 30.3, 30.1], "result": 100},
        ],
        5: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 160, 0, 0], "result": np.nan},
            {"obs": [70.1, 5, 6, 0], "fct": [70.4, 160, 0, 0], "result": 0},
            {"obs": [70.1, 160, 6, 0], "fct": [70.4, 70.2, 0, 0], "result": 50},
            {"obs": [70.4, 160, 0, 0], "fct": [70.1, 70.2, 70.3, 0], "result": 66.67},
            {"obs": [70.4, 160, 0, 0], "fct": [70.1, 70.2, 70.3, 70.1], "result": 75},
            {"obs": [0, 160, 0, 0], "fct": [70.1, 70.2, 70.3, 70.1], "result": 100},
        ],
        6: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [140.1, 5, 6, 0], "fct": [140.4, 10, 0, 0], "result": 0},
            {"obs": [140.1, 10, 6, 0], "fct": [140.4, 140.2, 0, 0], "result": 50},
            {
                "obs": [140.4, 10, 0, 0],
                "fct": [140.1, 140.2, 140.3, 0],
                "result": 66.67,
            },
            {
                "obs": [140.4, 10, 0, 0],
                "fct": [140.1, 140.2, 140.3, 140.1],
                "result": 75,
            },
            {"obs": [0, 10, 0, 0], "fct": [140.1, 140.2, 140.3, 140.1], "result": 100},
        ],
    },
    "24h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 66.67},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 150, 0, 0], "result": np.nan},
            {"obs": [10.1, 5, 6, 0], "fct": [10.4, 150, 0, 0], "result": 0},
            {"obs": [10.1, 150, 6, 0], "fct": [10.4, 10.2, 0, 0], "result": 50},
            {"obs": [10.4, 150, 0, 0], "fct": [10.1, 10.2, 10.3, 0], "result": 66.67},
            {"obs": [10.4, 150, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 75},
            {"obs": [0, 150, 0, 0], "fct": [10.1, 10.2, 10.3, 10.1], "result": 100},
        ],
        3: [
            {"obs": [1.1, 50, 60, 0], "fct": [1.4, 80, 0, 0], "result": np.nan},
            {"obs": [25.1, 5, 6, 0], "fct": [25.4, 80, 0, 0], "result": 0},
            {"obs": [25.1, 80, 6, 0], "fct": [25.4, 25.2, 0, 0], "result": 50},
            {"obs": [25.4, 80, 0, 0], "fct": [25.1, 25.2, 25.3, 0], "result": 66.67},
            {"obs": [25.4, 80, 0, 0], "fct": [25.1, 25.2, 25.3, 25.1], "result": 75},
            {"obs": [0, 80, 0, 0], "fct": [25.1, 25.2, 25.3, 25.1], "result": 100},
        ],
        4: [
            {"obs": [1.1, 60, 60, 0], "fct": [1.4, 260, 0, 0], "result": np.nan},
            {"obs": [50.1, 5, 6, 0], "fct": [50.4, 260, 0, 0], "result": 0},
            {"obs": [50.1, 260, 6, 0], "fct": [50.4, 50.2, 0, 0], "result": 50},
            {"obs": [50.4, 260, 0, 0], "fct": [50.1, 50.2, 50.3, 0], "result": 66.67},
            {"obs": [50.4, 260, 0, 0], "fct": [50.1, 50.2, 50.3, 50.1], "result": 75},
            {"obs": [0, 260, 0, 0], "fct": [50.1, 50.2, 50.3, 50.1], "result": 100},
        ],
        5: [
            {"obs": [1.1, 250, 260, 0], "fct": [1.4, 260, 0, 0], "result": np.nan},
            {"obs": [100.1, 5, 6, 0], "fct": [100.4, 260, 0, 0], "result": 0},
            {"obs": [100.1, 260, 6, 0], "fct": [100.4, 100.2, 0, 0], "result": 50},
            {
                "obs": [100.4, 260, 0, 0],
                "fct": [100.1, 100.2, 100.3, 0],
                "result": 66.67,
            },
            {
                "obs": [100.4, 260, 0, 0],
                "fct": [100.1, 100.2, 100.3, 100.1],
                "result": 75,
            },
            {"obs": [0, 260, 0, 0], "fct": [100.1, 100.2, 100.3, 100.1], "result": 100},
        ],
        6: [
            {"obs": [1.1, 250, 260, 0], "fct": [1.4, 10, 0, 0], "result": np.nan},
            {"obs": [250.1, 5, 6, 0], "fct": [250.4, 10, 0, 0], "result": 0},
            {"obs": [250.1, 10, 6, 0], "fct": [250.4, 250.2, 0, 0], "result": 50},
            {
                "obs": [250.4, 10, 0, 0],
                "fct": [250.1, 250.2, 250.3, 0],
                "result": 66.67,
            },
            {
                "obs": [250.4, 10, 0, 0],
                "fct": [250.1, 250.2, 250.3, 250.1],
                "result": 75,
            },
            {"obs": [0, 10, 0, 0], "fct": [250.1, 250.2, 250.3, 250.1], "result": 100},
        ],
    },
}

LEV_FALSE_ALARM_RATE_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 25},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 0},
            {"obs": [2.1, 0, 0, 0], "fct": [2.2, 2.4, 10, 0], "result": 25},
            {"obs": [2.1, 0, 10, 0], "fct": [2.2, 2.4, 2.2, 0], "result": 50},
            {"obs": [2.2, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 75},
            {"obs": [0, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 100},
        ],
    }
}
