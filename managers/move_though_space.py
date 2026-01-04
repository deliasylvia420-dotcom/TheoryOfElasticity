import models.space_point
import models.space_grid
import managers.v1_x
import managers.v2_y
import numpy

#эйлерово описание

def move_through_space(time, h, grid_axis):
    grid_length = grid_axis * 2 + 1
    a = numpy.linspace(-grid_axis, grid_axis, grid_length)
    x_s, y_s = numpy.meshgrid(a, a)
    
    velocity_fields = []
    steps_count = int(time / h) + 1

    for n in range(steps_count):
        t = n * h
        space_points = []
        m = 0
        for i in range(grid_length):
            for j in range(grid_length):
                x = x_s[i, j]
                y = y_s[i, j]
                vx = managers.v1_x.v1_x(t, x)
                vy = managers.v2_y.v2_y(t, y)
                space_points.append(
                    models.space_point.SpacePoint(m, x, y, vx, vy, t)
                )
                m += 1
        velocity_fields.append(models.space_grid.SpaceGrid(space_points))
    
    return velocity_fields 