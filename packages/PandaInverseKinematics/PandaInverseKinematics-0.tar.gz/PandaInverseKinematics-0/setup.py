import setuptools
from pathlib import Path

setuptools.setup(
    name='PandaInverseKinematics',
    version='0',
    description="A OpenAI Gym Env for Panda Inverse Kinematics",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=["gym_panda_inverse_kinematics", "gym_panda_inverse_kinematics.envs"]),
    install_requires=['gym', 'numpy', 'pybullet'],
    python_requires='>=3.6',
)