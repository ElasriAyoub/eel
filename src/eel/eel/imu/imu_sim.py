from time import time
from std_msgs.msg import Float32
from ..utils.sim import ANGULAR_VELOCITY
from ..utils.topics import RUDDER_STATUS, MOTOR_CMD


def calculate_angle_delta(angular_velocity, time_in_s):
    return angular_velocity * time_in_s


class ImuSimulator:
    def __init__(self, parent_node=None) -> None:
        self.current_rudder_status = float(0)
        self.current_heading = float(0)
        self.speed = 0
        self.last_updated_at = time()
        self.rudder_subscription = parent_node.create_subscription(
            Float32, RUDDER_STATUS, self._handle_rudder_msg, 10
        )
        self.motor_subscription = parent_node.create_subscription(
            Float32, MOTOR_CMD, self._handle_motor_msg, 10
        )

        self.imu_updater = parent_node.create_timer(
            1.0 / (parent_node.update_frequency * 2), self._update_imu
        )

    def _handle_rudder_msg(self, msg):
        self.current_rudder_status = msg.data

    def _handle_motor_msg(self, msg):
        self.speed = msg.data

    def _update_imu(self):
        if self.speed > 0:
            now = time()
            time_delta = now - self.last_updated_at
            angle_delta = calculate_angle_delta(ANGULAR_VELOCITY, time_delta)
            to_add = self.current_rudder_status * angle_delta
            self.current_heading = (self.current_heading + to_add) % 360

        self.last_updated_at = time()

    def get_calibration_status(self):
        sys = 3
        gyro = 3
        accel = 3
        mag = 3

        return sys, gyro, accel, mag

    def get_heading(self):
        return self.current_heading

    def get_is_calibrated(self):
        return True
