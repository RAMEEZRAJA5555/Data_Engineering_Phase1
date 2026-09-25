# Axes

## Definition

In Matplotlib, **Axes** is the actual area where the data is plotted.

It contains the x-axis, y-axis, title, labels, ticks, and the plotted data.

## Simple Example

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4], [10, 20, 15, 25])

plt.show()
```

Here, `ax` represents the Axes.

## Figure vs Axes

* **Figure** = complete canvas
* **Axes** = actual graph area inside the Figure

## Remember

> **Axes = the area where the actual graph is drawn.**
