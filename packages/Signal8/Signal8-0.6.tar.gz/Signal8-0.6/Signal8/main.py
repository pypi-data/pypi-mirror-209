import Signal8

env = Signal8.env(has_dynamic_adversaries=True)
env.reset(options={"problem_name": "v_cluster"})
