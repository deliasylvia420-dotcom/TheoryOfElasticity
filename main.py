#%%
import managers.create_material_body
import managers.fields
import managers.move_material_body
import managers.move_though_space
import managers.plot_trajectory
import matplotlib as plt

# Квадрат, 3-я четверть 
QUADRANT = 3 

h = 0.1
time = 1.5
grid_axis = 4

#создание тела
body = managers.create_material_body.create_material_body(h, quadrant=QUADRANT)

#расчет траекторий
trajectory = managers.move_material_body.move_material_body(time, h, body)

#построение траекторий
managers.plot_trajectory.plot_trajectory(body, trajectory)

#расчет полей
velocity_fields = managers.move_though_space.move_through_space(time, h, grid_axis)

#построение полей
managers.fields.plot_velocity_fields(velocity_fields, grid_axis, h)
# %%
