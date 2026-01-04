import matplotlib.pyplot as plt
import numpy
import math

def plot_velocity_fields(velocity_fields, grid_axis, h):
    for n in range(1, len(velocity_fields)):
        t = velocity_fields[n].space_points[0].time

        plt.figure(figsize=(10, 5))
        plt.suptitle(f't = {t:.2f}')
        
        # Данные для Quiver
        coord_x = [p.coord_x for p in velocity_fields[n].space_points]
        coord_y = [p.coord_y for p in velocity_fields[n].space_points]
        v_x = [p.velocity_x for p in velocity_fields[n].space_points]
        v_y = [p.velocity_y for p in velocity_fields[n].space_points]

        plt.subplot(1, 2, 1)
        plt.title("Поле скоростей")
        plt.quiver(coord_x, coord_y, v_x, v_y)
        plt.axis('equal')

        # Линии тока
        Y, X = numpy.mgrid[-grid_axis:grid_axis:0.05, -grid_axis:grid_axis:0.05]
        U = - numpy.sin(t) * X
        V = t * Y
        
        plt.subplot(1, 2, 2)
        plt.title("Линии тока")
        plt.axis([-grid_axis, grid_axis, -grid_axis, grid_axis])
        plt.streamplot(X, Y, U, V, density=1.5, color='g')
        
        plt.show()