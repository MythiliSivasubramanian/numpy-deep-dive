import numpy as np


def scenario_range(a: np.ndarray) -> None:
    between_3_8 = a[(a >= 3) & (a <= 8)]
    print("Scenario: range [3..8]")
    print("a:", a)
    print("between:", between_3_8)


def scenario_and_or(a: np.ndarray) -> None:
    gt_5_and_even = a[(a > 5) & (a % 2 == 0)]
    lt_4_or_gt_10 = a[(a < 4) | (a > 10)]
    print("Scenario: AND / OR")
    print("a:", a)
    print(">5 and even:", gt_5_and_even)
    print("<4 or >10:", lt_4_or_gt_10)


def scenario_not(a: np.ndarray) -> None:
    mask = (a >= 3) & (a <= 10)
    outside = a[~mask]
    print("Scenario: NOT (~mask)")
    print("a:", a)
    print("mask (3..10):", mask)
    print("outside:", outside)


def main() -> None:
    a = np.array([3, 8, 2, 9, 5, 1, 12, 7, 6, 4, 10])
    scenario_range(a)
    scenario_and_or(a)
    scenario_not(a)


if __name__ == "__main__":
    main()
