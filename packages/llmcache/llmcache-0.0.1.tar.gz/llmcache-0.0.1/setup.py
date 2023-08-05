from setuptools import find_packages, setup
from llmcache import __version__

core_reqs = [
    "redis"
]

setup(
    name="llmcache",
    version=__version__,
    url="https://redis.com/",
    author="Redis",
    author_email="sam.partee@redis.com",
    # long_description=open("README.md", "r", encoding="utf-8").read(),
    # long_description_content_type="text/markdown",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=core_reqs,
    package_data={"": ["*.ini"]},
    extras_require=dict(),
)
