import math

# Define physical constants
mu = float(4 * math.pi * 1e-7)  # Permeability of free space (T·m/A)

# Define the parameters for the traces
trace_spacing = float(0.6)
trace_count = int(16)         # Number of traces
y_trace_position = int(0)      # Assume all traces are along y=0 for simplicity

# Define the Biot-Savart Law for a straight trace (without current)
def BiotSavart_relative(radius):
    if radius == 0:
        return 0  # Avoid division by zero
    return mu / (2 * math.pi * radius)
