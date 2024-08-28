from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Declare the 'model' argument
    model_arg = DeclareLaunchArgument(
        'model',
        default_value=os.path.join(
            get_package_share_directory('mycobot_description'),
            'urdf',
            'mycobot_280_urdf.xacro'
        ),
        description='Path to the URDF/Xacro model file'
    )

    # Use the model argument
    model = LaunchConfiguration('model')


    # Get the path to the sub launch file
    sub_launch_file_path = os.path.join(
        get_package_share_directory('urdf_tutorial'),
        'launch',
        'display.launch.py'
    )

    # Include the sub launch file
    sub_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(sub_launch_file_path),
        launch_arguments={'model': model}.items()
    )

    return LaunchDescription([
        model_arg,
        sub_launch,
    ])
