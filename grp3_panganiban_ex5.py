import math

# Absolute value
x_absolute = -8.7
absolute_value = abs(x_absolute)
print(absolute_value)  # Output: 8.7

# Minimum and maximum
numbers_min_max = [4, 12, 7, 2, 15]
minimum = min(numbers_min_max)
maximum = max(numbers_min_max)
print(f"Minimum: {minimum}, Maximum: {maximum}")  # Output: Minimum: 2, Maximum: 15

# Rounding
number_rounding = 7.896
rounded_up = round(number_rounding)
rounded_down = round(number_rounding, 0)
rounded_to_two_decimals = round(number_rounding, 2)
print(f"Rounded up: {rounded_up}, Rounded down: {rounded_down}, Rounded to two decimals: {rounded_to_two_decimals}")
# Output: Rounded up: 8, Rounded down: 8, Rounded to two decimals: 7.9
import math

# Power function
base_power = 3
exponent_power = 4
result_power = pow(base_power, exponent_power)  # 3 raised to the power of 4
print(result_power)  # Output: 81

# Logarithm with base 10
number_log10 = 1000
logarithm_log10 = math.log10(number_log10)  # logarithm of 1000 with base 10
print(logarithm_log10)  # Output: 3.0

# Natural logarithm (base e)
number_ln = 7.389056
natural_logarithm_ln = math.log(number_ln)  # natural logarithm of 7.389056 (approximately equal to e)
print(natural_logarithm_ln)  # Output: 2.0
import math

# Convert degrees to radians
degrees_to_radians = 30
radians_result = math.radians(degrees_to_radians)
print(radians_result)  # Output: 0.5235987755982988

# Convert radians to degrees
radians_to_degrees = math.pi / 4
degrees_result = math.degrees(radians_to_degrees)
print(degrees_result)  # Output: 45.0
import math

# Hyperbolic sine function
x_sinh = 2
sinh_value = math.sinh(x_sinh)
print(sinh_value)  # Output: 3.6268604078470186

# Hyperbolic cosine function
x_cosh = 1.5
cosh_value = math.cosh(x_cosh)
print(cosh_value)  # Output: 2.3524096152432476

# Hyperbolic tangent function
x_tanh = 0.8
tanh_value = math.tanh(x_tanh)
print(tanh_value)  # Output: 0.6640367702678489
