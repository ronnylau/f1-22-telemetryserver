from struct import unpack


class CarMotionData:
    def __init__(self, data):
        self.data = data
        self.car_motion_data = unpack('<ffffffHHHHHHffffff', data[24:84])
        self.world_position_x = None
        self.world_position_y = None
        self.world_position_z = None
        self.world_velocity_x = None
        self.world_velocity_y = None
        self.world_velocity_z = None
        self.world_forward_dir_x = None
        self.world_forward_dir_y = None
        self.world_forward_dir_z = None
        self.world_right_dir_x = None
        self.world_right_dir_y = None
        self.world_right_dir_z = None
        self.g_force_lateral = None
        self.g_force_longitudinal = None
        self.g_force_vertical = None
        self.yaw = None
        self.pitch = None
        self.roll = None
