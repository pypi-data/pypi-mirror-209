from datetime import datetime, timedelta


class Calculate:
    # 游戏等级所需经验值列表
    total_exp_list = [450, 500, 550, 610, 670, 720, 780, 840, 900, 960, 1020, 1070, 1130, 1190, 1250, 1310, 1370,
                      1430, 1500, 1600, 1710, 1830, 1950, 2080, 2210, 2350, 2480, 2620, 2750, 2850, 2960, 3080, 3200,
                      3330, 3460, 3600, 3730, 3870, 4000, 4140, 4280, 4430, 4570, 4710, 4860, 5000, 5150, 5300, 5440,
                      5700, 6150, 6630, 7130, 7640, 8170, 8700, 9230, 9780, 10330, 20300, 21780, 23350, 24970, 26630,
                      65070, 68810, 72490, 76120, 79710]
    # 等级奖励中是否包含体力药水
    reward_stamina_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1,
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1,
                           1, 1, 1, 1, 1]
    # 到目标等级需要的经验值
    remaining_exp = 0
    # 等级奖励中能够获得的体力药水
    reward_potions = 0
    # 计算升级时间点
    designated_time = None

    def __init__(self, _current_level: int, _target_level: int, _current_exp: int, _num_potions: int,
                 _current_stamina: int):
        """当前等级,目标等级,当前等级已获得的经验值,当前拥有的体力药水,当前拥有的体力"""
        self._current_stamina = _current_stamina
        self._num_potions = _num_potions
        self._current_exp = _current_exp
        self._target_level = _target_level
        self._current_level = _current_level
        if self._target_level <= self._current_level:
            raise ValueError("目标等级不能小于当前等级")
        elif self._current_level == 0 or self._target_level == 0:
            raise ValueError("等级不能为0")
        # 计算从当前等级到目标等级需要的经验值
        for i in range(self._target_level - self._current_level):
            self.remaining_exp += self.total_exp_list[self._current_level + i - 1]
        self.remaining_exp -= self._current_exp
        # 计算升级所需的体力值
        self.required_stamina = self.remaining_exp // 5
        # 计算从当前体力药水数和当前体力值以及等级奖励中能够获得的体力值
        for i in range(self._target_level - self._current_level):
            self.reward_potions += self.reward_stamina_list[self._current_level - 1 + i]
        self.available_stamina = self._current_stamina + 60 * (self._num_potions + self.reward_potions)
        # 计算从当前状态需要多少分钟才能够升级
        if self.required_stamina > self.available_stamina:
            self.required_time = (self.required_stamina - self.available_stamina) * 6
        else:
            self.required_time = 0
        # 计算升级时间点
        self.designated_time = (datetime.now() + timedelta(minutes=self.required_time)).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    current_level = 47
    target_level = 60
    current_exp = 2470
    num_potions = 33
    current_stamina = 39

    # 当前等级,目标等级,当前等级已获得的经验值,当前拥有的体力药水,当前拥有的体力
    result = Calculate(current_level, target_level, current_exp, num_potions, current_stamina)
    # 获取当前时间
    now = datetime.now()
    # 计算指定的时间
    new_time = now + timedelta(minutes=result.required_time)
    print(f"需要{result.required_time}分钟才能升到第{target_level}级")
    print(f"将在{new_time.strftime('%Y-%m-%d %H:%M:%S')}升到第{target_level}级")
