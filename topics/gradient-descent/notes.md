## Gradient Descent

### Motivation
- Grid search is a brute force optimization algorithm that loops through all rows and columns: $O(n^2)$

### What is Gradient Descent?
- gradient = version of multi-dimensional derivative
- a gradient in any point points towards that smallest value (local minimum)
- gradient descent = lots of little steps towards the lowest point (the process of creating that path)
    - need the gradient to tell us which direction to move on the $(m, b)$ parameter space to descent on the evaluation matrix the quickest

### Formulas

$$\text{MSE} = \frac{1}{D}\sum_{i}\big(p_i - (m n_i + b)\big)^2$$

$$d_m(\text{MSE}) = -2 \cdot \text{avg}\big(\text{input values} \cdot (\text{truth} - \text{guess})\big)$$

- partial derivative of MSE with respect to $m$
    - resulting value tells us how far to move in thge $m$ direction

$$d_b(\text{MSE}) = -2 \cdot \text{avg}(\text{truth} - \text{guess})$$

- the partial derivatives tell us the steepest direction to move in from our current point.
- since we want to move towards the minimum, we choose to move in the direction of the negative gradient

$m_{\text{new}} = m - L \cdot d_m(\text{MSE})$
$b_{\text{new}} = b - L \cdot d_b(\text{MSE})$

- $L$ = learning rate (how big our steps should be)