**Goal of this folder :**

Understand how NumPy arrays share or own memory.

**Key ideas :**

- Views share memory with the original array
- Copies own their own memory
- reshape and slicing usually return views
- .copy() always creates a new array

**Why this matters:** 

Silent memory sharing can cause unintended data mutation and bugs.
