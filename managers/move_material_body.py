import models.point_trajectory
import models.body_trajectory
import models.butcher_table
import managers.v1_x
import managers.v2_y
import numpy as np

#лагранжево описание (каждая точка в момент времени)

def move_material_body(time, h, moved_body):
    point_trajectories = []
    butcher = models.butcher_table.butcher_table
    
    steps_count = int(np.round(time / h))
    
    for point in moved_body.material_points:
        t = 0.0
        x_t = [point.x_0]
        y_t = [point.y_0]
        
        for _ in range(steps_count):
            x_k = x_t[-1]
            y_k = y_t[-1]
            
            #k1
            f_1x = managers.v1_x.v1_x(t, x_k)
            f_1y = managers.v2_y.v2_y(t, y_k)
            
            #k2
            f_2x = managers.v1_x.v1_x(t + butcher.c[1]*h, x_k + h*butcher.a[1][0]*f_1x)
            f_2y = managers.v2_y.v2_y(t + butcher.c[1]*h, y_k + h*butcher.a[1][0]*f_1y)
            
            #k3
            f_3x = managers.v1_x.v1_x(t + butcher.c[2]*h, x_k + h*butcher.a[2][1]*f_2x)
            f_3y = managers.v2_y.v2_y(t + butcher.c[2]*h, y_k + h*butcher.a[2][1]*f_2y)
            
            #сумма
            x_new = x_k + h * (butcher.b[0]*f_1x + butcher.b[1]*f_2x + butcher.b[2]*f_3x)
            y_new = y_k + h * (butcher.b[0]*f_1y + butcher.b[1]*f_2y + butcher.b[2]*f_3y)
            
            x_t.append(x_new)
            y_t.append(y_new)
            t += h
        
        point_trajectories.append(models.point_trajectory.PointTrajectory(point, x_t, y_t))
    
    return models.body_trajectory.BodyTrajectory(point_trajectories, moved_body)