def water_column_height(tower_height, tank_height):
    # h = t + (3w / 4)
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    # P = (ρ * g * h) / 1000
    rho = 998.2     # kg/m^3
    g = 9.80665     # m/s^2
    return (rho * g * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # P = - (f * L * ρ * v^2) / (2000 * d)
    rho = 998.2     # kg/m^3
    return -friction_factor * pipe_length * rho * fluid_velocity**2 / (2000 * pipe_diameter)
