import models.material_point
import models.material_body
import numpy as np
import managers.v1_x
import managers.v2_y

def create_material_body(h, quadrant=3):
    t_start = 0.0

    if quadrant == 3:
        x_min, x_max = -1.0, 0.0
        y_min, y_max = -1.0, 0.0
    elif quadrant == 2:
        x_min, x_max = -1.0, 0.0
        y_min, y_max = 1.0, 0.0
    elif quadrant == 1:
        x_min, x_max = 1.0, 0.0
        y_min, y_max = 1.0, 0.0
    elif quadrant == 4:
        x_min, x_max = 1.0, 0.0
        y_min, y_max = -1.0, 0.0
    else:
        x_min, x_max = -1.0, 0.0
        y_min, y_max = -1.0, 0.0


    steps = int(1.0 / h) + 1
    x_coords = np.linspace(x_min, x_max, steps)
    y_coords = np.linspace(y_min, y_max, steps)
        
    m = 0
    material_points = []
    
    for x in x_coords:
        for y in y_coords:
            vx = managers.v1_x.v1_x(t_start, x)
            vy = managers.v2_y.v2_y(t_start, y)
            material_points.append(
                models.material_point.MaterialPoint(m, x, y, vx, vy, x, y, t_start)
            )
            m += 1
            
    return models.material_body.MaterialBody(material_points)
