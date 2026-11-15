# Student Performance Factors – Data Analysis

## Project Overview

This project focuses on analyzing student performance factors using Python. The main objective is to explore student data, identify patterns, understand relationships between different factors, and examine how these factors are associated with students' exam scores.

## Dataset

The project uses the `StudentPerformanceFactors.csv` dataset.

- **Original dataset:** `StudentPerformanceFactors.csv`
- **Cleaned dataset:** `cleaned_StudentPerformanceFactors.csv`
- **Rows in original dataset:** 6,607
- **Rows after cleaning:** 6,378
- **Columns:** 20

## Technologies and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Parts

1. Import Libraries and Load Dataset
2. Data Inspection
3. Data Cleaning
4. Numerical Analysis Using NumPy
5. Exploratory Data Analysis (EDA)
6. Relationship Analysis
7. Data Visualization
8. Key Insights and Conclusion

## Data Cleaning

The following cleaning steps were performed:

- Checked for duplicate records.
- Identified missing values.
- Removed rows containing missing values.
- Checked categorical and numerical values.
- Corrected an exam score of 101 to 100, assuming the maximum possible score is 100.
- Saved the cleaned dataset separately.

## Analysis and Visualization

The project explores relationships between student performance factors and exam scores.

Visualizations include:

- Scatter plots
- Bar plots
- Histograms
- Box plots
- Count plots
- Correlation heatmap

## Key Findings

- Most exam scores were concentrated around the 60–70 range.
- Study hours showed a moderate positive correlation with exam scores.
- Sleep hours showed almost no linear correlation with exam scores.
- Attendance showed an upward trend with exam scores.
- Categorical group averages generally showed small differences.

## Project Structure

```text
Student-Performance-Analysis/
│
├── StudentPerformanceFactors.csv
├── cleaned_StudentPerformanceFactors.csv
├── Student_performance_data_analysis.ipynb
├── Report_Student_Performance_analysis.docx
└── README.md
```

## How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

3. Clone or download this repository.
4. Open the project folder in Jupyter Notebook.
5. Run the notebook cells in order.

## Project Goal

This project demonstrates beginner-level practical skills in data analysis, data cleaning, exploratory data analysis, and data visualization using Python.