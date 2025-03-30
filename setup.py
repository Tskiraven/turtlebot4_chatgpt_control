from setuptools import setup

package_name = 'turtlebot4_chatgpt_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'openai'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='ChatGPT-controlled TurtleBot4 using natural language',
    license='MIT',
    entry_points={
        'console_scripts': [
            'controller = turtlebot4_chatgpt_control.turtlebot_controller:main',
            'terminal_control = turtlebot4_chatgpt_control.main_terminal_control:main'
        ],
    },
)
