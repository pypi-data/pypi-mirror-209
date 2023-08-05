class YawController():
    def __init__(self, drone, thresh):
        self.drone = drone
        self.d = 360 - self._get_yaw()
        self.thresh = thresh

    def _get_yaw(self):
        yaw = self.drone.get_yaw()
        if yaw < 0:
            yaw = yaw + 360
        return yaw

    def update_yaw(self):
        yaw = (self._get_yaw() + self.d) % 360
        return yaw

    def control(self, cmd):
        assert cmd >= 0 and cmd <= 360

        def cal_dist_cw(cur, cmd):
            if cur >= cmd:
                dist_cw = (360 - cur) + cmd
            else:
                dist_cw = cmd - cur
            assert dist_cw >= 0
            return dist_cw

        def cal_dist_ccw(cur, cmd):
            if cur >= cmd:
                dist_ccw = cur - cmd
            else:
                dist_ccw = cur + (360 - cmd)
            assert dist_ccw >= 0
            return dist_ccw

        dist_cw = cal_dist_cw(cur=self.update_yaw(), cmd=cmd)
        dist_ccw = cal_dist_ccw(cur=self.update_yaw(), cmd=cmd)
        dist = min(dist_cw, dist_ccw)
        while dist > self.thresh:
            if dist_cw < dist_ccw:
                self.drone.rotate_clockwise(dist_cw)
            else:
                self.drone.rotate_counter_clockwise(dist_ccw)
            dist_cw = cal_dist_cw(cur=self.update_yaw(), cmd=cmd)
            dist_ccw = cal_dist_ccw(cur=self.update_yaw(), cmd=cmd)
            dist = min(dist_cw, dist_ccw)
        return self.update_yaw()


class HeightController():
    def __init__(self, drone, thresh):
        self.drone = drone
        self.thresh = thresh
        
    def control(self, cmd):
        dist_h = abs(cmd - self.drone.get_height())
        while dist_h > self.thresh:
            if cmd > self.drone.get_height():
                self.drone.move_up(20)
            else:
                self.drone.move_down(20)
            dist_h = abs(cmd - self.drone.get_height())
        return self.drone.get_height()