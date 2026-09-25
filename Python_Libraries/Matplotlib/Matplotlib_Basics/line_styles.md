# Line Styles

## Definition

**Line style** controls the appearance of a line in a graph.

A line can be solid, dashed, dotted, or made using other styles.

## Common Line Styles

| Style | Meaning       |
| ----- | ------------- |
| `-`   | Solid line    |
| `--`  | Dashed line   |
| `:`   | Dotted line   |
| `-.`  | Dash-dot line |

## Example

```python
plt.plot([1, 2, 3], [10, 20, 15], linestyle="--")
```

This creates a dashed line.

## Purpose

Different line styles can help distinguish between multiple datasets.

## Remember

> **Line style = controls how a line appears.**
