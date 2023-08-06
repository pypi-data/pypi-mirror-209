import Signal8

env = Signal8.env(dynamic_obstacles=True, render_mode="human")
env.reset(options={"problem_name": "v_cluster"})