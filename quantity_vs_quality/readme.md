# Building Intuition: More Data vs Noise in Linear Regression

## Overview

This project demonstrates a simple but important idea in machine learning:

> **All else being equal, more rows of data leads to more reliable estimates.**

We begin with the familiar case of estimating a mean, and then extend this intuition to **simple linear regression**, where we estimate the slope of a relationship between variables.

---

## Key Insight

In regression, the quality of your estimate depends on a trade-off between:

* **Noise in the data** (random variability)
* **Number of data points** (sample size)

A precise formulation:

> **Low noise can substitute for small data; large data can compensate for high noise.**

---

## Mathematical Insight

For simple linear regression, the standard error of the slope estimate behaves approximately as:

$${SE}(\hat{\beta}_1) \propto \frac{\sigma}{\sqrt{n}}$$

Where:

* $\sigma$: noise level (standard deviation of residuals)
* $n$: number of data points

This tells us:

* Increasing **noise** makes estimation harder
* Increasing **sample size** improves precision (via $1/\sqrt{n}$)

---

## Interpretation

### Small Data Regime

* With only a few data points (e.g. n = 10):

  * You can estimate the true slope accurately **only if noise is low**
  * High noise will dominate the signal → unreliable estimates

### Large Data Regime

* With many data points (e.g. n = 100,000+):

  * Even with high noise, averaging effects dominate
  * The estimated slope converges to the true value

---

## Important Assumption

This demonstration isolates the effect of sample size by holding other factors fixed:

* Same true data-generating process
* Same noise level
* Same distribution (spread) of input values

Without these controls, increasing data alone does not guarantee improvement.

---

## What the Plots Show

1. **Slope vs Sample Size**

   * Estimates stabilise around the true slope as $n$ increases
   * Error bars (±1 SEM) shrink with more data

2. **Standard Error vs Sample Size (log-log)**

   * Clear ($1/\sqrt{n}$) scaling
   * Appears as a straight line with slope -1/2

3. **Reference Scaling Line**

   * Confirms theoretical behaviour against empirical results

---

## Takeaway

> **More data improves estimation by reducing uncertainty through averaging.**

This trade-off is central to real-world machine learning system design.

---
