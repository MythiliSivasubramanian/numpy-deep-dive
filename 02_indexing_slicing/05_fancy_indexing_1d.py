import numpy as np


def scenario_basic_picks(a: np.ndarray) -> None:
    picks = a[[0, 3, 4]]
    print("Scenario: basic picks [0,3,4]")
    print("a:", a)
    print("picks:", picks)


def scenario_order_and_duplicates(a: np.ndarray) -> None:
    order_change = a[[4, 0, 3]]
    duplicates = a[[1, 1, 3, 3]]
    print("Scenario: order + duplicates")
    print("a:", a)
    print("order [4,0,3]:", order_change)
    print("duplicates [1,1,3,3]:", duplicates)


def scenario_assign_with_fancy(a: np.ndarray) -> None:
    b = a.copy()
    idx = np.array([1, 3, 5])
    b[idx] = -1
    print("Scenario: assign with fancy indices")
    print("a:", a)
    print("idx:", idx)
    print("b:", b)


def main() -> None:
    a = np.array([3, 8, 2, 9, 5, 1, 12])
    scenario_basic_picks(a)
    scenario_order_and_duplicates(a)
    scenario_assign_with_fancy(a)


if __name__ == "__main__":
    main()
