def calculate_continuous_energy(signal):
    from scipy.integrate import quad, IntegrationWarning
    import numpy as np
    import warnings
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always", IntegrationWarning)
        result, error = quad(lambda t: np.abs(signal(t))**2, -np.inf, np.inf)

        # Check if any integration warnings were issued
        if any(issubclass(warning.category, IntegrationWarning) for warning in w):
            return np.inf, error

        return result, error


def calculate_continuous_power(signal):
    # Import necessary modules inside the function
    from scipy.integrate import quad, IntegrationWarning
    import numpy as np
    import warnings

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always", IntegrationWarning)
        # Calculate the integral of the square of the signal over the interval [-T, T]
        T = 10000 # Hardcoded
        result, error = quad(lambda t: np.abs(signal(t))**2, -T, T)

        # Check if any integration warnings were issued
        if any(issubclass(warning.category, IntegrationWarning) for warning in w):
            return np.inf, error

        # Calculate the power as the integral divided by 2T
        power = result / (2 * T)

        return power, error

def calculate_continuous_average(signal):
    # Import necessary modules inside the function
    from scipy.integrate import quad, IntegrationWarning
    import numpy as np
    import warnings

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always", IntegrationWarning)
        # Calculate the integral of the square of the signal over the interval [-T, T]
        T = 10000 # Hardcoded
        result, error = quad(lambda t: signal(t), -T, T)

        # Check if any integration warnings were issued
        if any(issubclass(warning.category, IntegrationWarning) for warning in w):
            return np.inf, error

        # Calculate the power as the integral divided by 2T
        power = result / (2 * T)

        return power, error