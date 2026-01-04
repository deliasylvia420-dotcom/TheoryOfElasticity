import matplotlib.pyplot as plt

def plot_trajectory(mb, tr):
    plt.figure(figsize=(8, 8))
    
    #красные точки (начало)
    init_x = [p.x_0 for p in mb.material_points]
    init_y = [p.y_0 for p in mb.material_points]
    plt.plot(init_x, init_y, 'r.', markersize=4, label='t=0')
    
    final_x = []
    final_y = []
    
    #синие линии (траектории)
    for traj in tr.point_trajectories:
        plt.plot(traj.x, traj.y, 'b-', linewidth=0.5, alpha=0.6)
        final_x.append(traj.x[-1])
        final_y.append(traj.y[-1])
        
    #зеленые точки (конец)
    plt.plot(final_x, final_y, 'g.', markersize=5, label='t=end')
        
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.title('Траектории (3-я четверть)')
    plt.show()