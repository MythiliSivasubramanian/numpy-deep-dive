**NumPy Deep Dive**

This repository is my learning journey into NumPy, focused on understanding how it really works, not just how to use it.

Instead of treating NumPy as a black box, I’m exploring its core ideas: arrays, shapes, dtypes, memory layout, vectorization, and performance. Many examples compare NumPy with plain Python to understand why NumPy is faster and more memory-efficient.

The goal is depth and clarity — to think in arrays instead of loops, and to understand the internal ideas that matter in real data and performance-critical work.

This repo grows as I learn. Code is written step by step, with experiments, mistakes, and insights along the way.

| **Folder**                       | **Purpose**                                                      |
| ---------------------------- | ------------------------------------------------------------ |
| `01_arrays_basics`           | Array creation, shape, ndim, and basic dtype concepts        |
| `02_indexing_slicing`        | Basic indexing, slicing behavior, boolean and fancy indexing |
| `03_memory_model`            | Memory layout, itemsize, nbytes, strides, views vs copies    |
| `04_indexing_slicing_advanced`|Advanced indexing, slicing behavior, boolean and  indexing   |
| `05_vectorization`           | Vectorization, broadcasting rules, ufuncs, loops vs NumPy    |
| `06_performance_experiments` | Timing comparisons and memory efficiency experiments         |
| `07_exercises`               | Practice problems and small NumPy experiments                |



**What I’m Focusing On**

- Understanding NumPy arrays as contiguous memory blocks
- How dtype affects speed and memory
- Why views vs copies matter
- How broadcasting really works
- Why vectorization beats loops
- Writing code that is clear, fast, and memory-aware

**How to Use This Repo**

* Each folder focuses on one concept
* Files are small and intentional
* Examples are meant to be run, modified, and broken.
* Comments explain why, not just what

**This is a learning repo**
