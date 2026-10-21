## Gradient Descent

### Motivation
- Grid search is a brute force optimization algorithm that loops through all rows and columns: $O(n^2)$

### What is Gradient Descent?
- gradient = version of multi-dimensional derivative
- a gradient in any point points towards that smallest value (local minimum)
- gradient descent = lots of little steps towards the lowest point (the process of creating that path)
    - need the gradient to tell us which direction to move on the $(m, b)$ parameter space to descent on the evaluation matrix the quickest

### Formulas

\begin{equation}
MSE = \dfrac{1}{D}\Sigma_{i}(p_i - (m*n_i + b))^2
\end{equation}

\begin{equation}
d_m(MSE) = -2*avg((input\_values)*(truth - (guess)))
\end{equation}

- partial derivative of MSE with respect to $m$
    - resulting value tells us how far to move in thge $m$ direction

\begin{equation}
d_b(MSE) = -2*avg((truth - (guess)))
\end{equation}

- the partial derivatives tell us the steepest direction to move in from our current point.
- since we want to move towards the minimum, we choose to move in the direction of the negative gradient

\begin{equation}
m_{new} = m - L*d_m(MSE)
\end{equation}

\begin{equation}
b_{new} = b - L*d_b(MSE)
\end{equation}

- $L$ = learning rate (how big our steps should be)