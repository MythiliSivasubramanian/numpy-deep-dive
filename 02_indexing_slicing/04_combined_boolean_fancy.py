import numpy as np


def scenario_filter_then_pick(a: np.ndarray) -> None:
    filtered = a[a > 3]
    result = filtered[[0, 2]]
    print("Scenario: filter > 3 then pick [0,2]")
    print("a:", a)
    print("filtered:", filtered)
    print("result:", result)


def scenario_pick_positions_then_filter(a: np.ndarray) -> None:
    picked = a[[0, 2, 3, 6]]
    result = picked[picked % 2 == 0]
    print("Scenario: pick [0,2,3,6] then keep even")
    print("a:", a)
    print("picked:", picked)
    print("result:", result)


def scenario_stable_pipeline(a: np.ndarray) -> None:
    filtered = a[(a >= 5) & (a <= 20)]
    if filtered.size >= 3:
        result = filtered[[0, 1, -1]]
    else:
        result = filtered
    print("Scenario: safe pipeline (range then pick edges)")
    print("a:", a)
    print("filtered:", filtered)
    print("result:", result)


def main() -> None:
    a = np.array([15, 3, 22, 8, 7, 30, 11, 2, 18])
    scenario_filter_then_pick(a)
    scenario_pick_positions_then_filter(a)
    scenario_stable_pipeline(a)


if __name__ == "__main__":
    main()
