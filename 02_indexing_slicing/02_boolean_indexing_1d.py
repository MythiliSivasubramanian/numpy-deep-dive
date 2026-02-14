import numpy as np


def scenario_thresholds(a: np.ndarray) -> None:
    gt_4 = a[a > 4]
    lt_5 = a[a < 5]
    print("Scenario: thresholds")
    print("a:", a)
    print("> 4:", gt_4)
    print("< 5:", lt_5)


def scenario_properties(a: np.ndarray) -> None:
    evens = a[a % 2 == 0]
    odds = a[a % 2 != 0]
    print("Scenario: properties")
    print("a:", a)
    print("even:", evens)
    print("odd:", odds)


def scenario_replace_with_mask(a: np.ndarray) -> None:
    b = a.copy()
    b[b < 0] = 0
    b[b > 10] = 10
    print("Scenario: replace with mask (clip-like)")
    print("a:", a)
    print("b:", b)


def main() -> None:
    a = np.array([3, 8, 2, 9, 5, 1, 12, 7])
    scenario_thresholds(a)

    a2 = np.array([10, 11, 12, 13, 14, 15, 16])
    scenario_properties(a2)

    a3 = np.array([-5, 2, 7, 11, 25, 0, -1])
    scenario_replace_with_mask(a3)


if __name__ == "__main__":
    main()
