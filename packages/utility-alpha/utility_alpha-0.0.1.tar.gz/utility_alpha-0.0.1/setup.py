from setuptools import setup

# Setting up
setup(
    name="utility_alpha",
    version="0.0.1",
    description="Short descript utility alpha",
    author="Dappomatics",
    packages=["utility_alpha"],
    zip_safe=False,
    package_data={'utility_alpha': ['apis/*']}
)