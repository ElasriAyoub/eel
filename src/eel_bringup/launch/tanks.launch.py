from launch import LaunchDescription
from launch_ros.actions import Node

SIMULATE_PARAM = "simulate"
MOTOR_PIN_PARAM = "motor_pin"
DIRECTION_PIN_PARAM = "direction_pin"
DISTANCE_SENSOR_ADDRESS_PARAM = "distance_sensor_address"
CMD_TOPIC_PARAM = "cmd_topic"
STATUS_TOPIC_PARAM = "status_topic"

FRONT_TANK_CMD = "tank_front/cmd"
FRONT_TANK_STATUS = "tank_front/status"
REAR_TANK_CMD = "tank_rear/cmd"
REAR_TANK_STATUS = "tank_rear/status"

TANK_FLOOR_MM_PARAM = "tank_floor_mm"
TANK_CEILING_MM_PARAM = "tank_ceiling_mm"
XSHUT_PIN_PARAM = "xshut_pin_param"


def generate_launch_description():
    ld = LaunchDescription()

    front_tank_node = Node(
        package="eel",
        executable="tank",
        name="tank_node",
        parameters=[
            {SIMULATE_PARAM: False},
            {CMD_TOPIC_PARAM: FRONT_TANK_CMD},
            {STATUS_TOPIC_PARAM: FRONT_TANK_STATUS},
            {MOTOR_PIN_PARAM: "23"},
            {DIRECTION_PIN_PARAM: "18"},
            {DISTANCE_SENSOR_ADDRESS_PARAM: "22"},
            {
                TANK_FLOOR_MM_PARAM: "15"
            },  # 11 is meausured floor. should possibly be 30 (or david says 20)
            {TANK_CEILING_MM_PARAM: "72"},  # 72 is measured ceiling
            {XSHUT_PIN_PARAM: "0"},
        ],
    )

    # rear_tank_node = Node(
    #     package="eel",
    #     executable="tank",
    #     name="tank_node",
    #     parameters=[
    #         {SIMULATE_PARAM: True},
    #         {CMD_TOPIC_PARAM: REAR_TANK_CMD},
    #         {STATUS_TOPIC_PARAM: REAR_TANK_STATUS},
    #         {MOTOR_PIN_PARAM: "24"},
    #         {DIRECTION_PIN_PARAM: "25"},
    #         {DISTANCE_SENSOR_ADDRESS_PARAM: "29"},
    #         {TANK_FLOOR_MM_PARAM: "25"},  # 12 is measured floor
    #         {TANK_CEILING_MM_PARAM: "63"},  # 63 is measured ceiling
    #         {XSHUT_PIN_PARAM: "21"},
    #     ],
    # )

    ld.add_action(front_tank_node)
    # ld.add_action(rear_tank_node)

    return ld