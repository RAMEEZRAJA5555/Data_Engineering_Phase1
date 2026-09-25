# Figure

## Definition

In Matplotlib, a **Figure** is the complete canvas or window where the visualization is created.

It is the outer container that holds the graph and other elements.

## Simple Example

```python
import matplotlib.pyplot as plt

plt.figure()

plt.plot([1, 2, 3, 4], [10, 20, 15, 25])

plt.show()
```

Here, `plt.figure()` creates a new Figure.

## Important

* Figure = complete canvas or window or blank sheet of paper
* A Figure can contain one or more Axes.
* For simple plots, Matplotlib can create a Figure automatically.

## Remember

> **Figure = the complete canvas that contains the visualization.**
