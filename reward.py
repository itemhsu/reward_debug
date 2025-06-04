def reward_function(params):
    '''
    范例代码：赛道分区策略
    '''
   
    # 分别设置鼓励靠左行驶的区域和鼓励靠右行驶的区域
    left = [*range(22,40),*range(76,92),*range(100,112)]
    right = [*range(48,56)]

    # 调用内置参数
    is_left_of_center = params['is_left_of_center']
    closest_waypoints = params['closest_waypoints']

    # 给予一个很低的起始奖励分数
    reward = 1e-3

    # 当赛车处于靠左行驶区且正在靠赛道左侧，或处于靠右行驶区且正在靠赛道右侧时，给予奖励
    if closest_waypoints[0] in left and is_left_of_center:
        reward = 1.0
    if closest_waypoints[0] in right and not is_left_of_center:
        reward = 1.0

    return float(reward)