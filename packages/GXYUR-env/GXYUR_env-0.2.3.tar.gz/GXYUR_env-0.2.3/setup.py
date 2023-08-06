import setuptools


setuptools.setup(
    name='GXYUR_env',
    author="GXY",
    version='0.2.3',
    description="An OpenAI Gym Env for dual UR5",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="GXYUR_env*"),
    install_requires=['gym', 'pybullet', 'numpy'],
    python_requires='>=3.6'
)
