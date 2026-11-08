import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):

    m = len(y)

    if method == 'batch':
        for i in range(n_epochs):
            dldw = (2/m) * np.dot(X.T, (np.dot(X, weights)-y))
            weights = weights - learning_rate*dldw

    elif method == 'stochastic':
        for i in range(n_epochs):
            for j in range(m):
                dldw = 2 * X[j] * (np.dot(X[j], weights)-y[j])
                weights = weights - learning_rate*dldw

    elif method == 'mini_batch':
        for i in range(n_epochs):
            for j in range(0, m, batch_size):
                X_temp = X[j:j+batch_size]
                y_temp = y[j:j+batch_size]

                b = len(y_temp)

                dldw = (2/b) * np.dot(
                    X_temp.T,
                    (np.dot(X_temp, weights)-y_temp)
                )

                weights = weights - learning_rate*dldw

    else:
        raise ValueError("Invalid method")

    final_weights = weights
    return final_weights
