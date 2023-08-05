from setuptools import setup

PLUGIN_NAME = "envd"

microlib_name = f"flytekitplugins-{PLUGIN_NAME}"

plugin_requires = ["flytekit", "envd"]

__version__ = "1.2.12"

setup(
    name=microlib_name,
    version=__version__,
    author="flyteorg",
    author_email="admin@flyte.org",
    description="This package enables users to easily build a Docker image for tasks or workflows.",
    namespace_packages=["flytekitplugins"],
    packages=[f"flytekitplugins.{PLUGIN_NAME}"],
    install_requires=plugin_requires,
    license="apache2",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"flytekit.plugins": [f"{PLUGIN_NAME}=flytekitplugins.{PLUGIN_NAME}"]},
)
