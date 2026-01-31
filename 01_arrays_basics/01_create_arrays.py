import numpy as np


def demo_array_creation():
    # 1D array
    a = np.array([1, 2, 3])

    # 2D array
    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    # Arrays from creation helpers
    c = np.zeros((3, 4))
    d = np.ones((2, 3))
    e = np.arange(0, 10, 2)

    arrays = {
        "a (1D)": a,
        "b (2D)": b,
        "c (zeros)": c,
        "d (ones)": d,
        "e (arange)": e,
    }

    for name, arr in arrays.items():
        print(f"\n{name}")
        print(arr)
        print(f"shape={arr.shape}, ndim={arr.ndim}, dtype={arr.dtype}")


if __name__ == "__main__":
    demo_array_creation()
