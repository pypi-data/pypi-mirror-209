from setuptools import setup

with open('README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()
setup(
    name='pytest_sequence_markers',
    version='0.0.2',
    author="Siddhesh Sathe",
    author_email="siddheshsathe@rediffmail.com",
    description="Pytest plugin for sequencing markers for execution of tests",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="GNU",
    url="https://github.com/siddheshsathe/pytest-plugins",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Source": "https://github.com/siddheshsathe/pytest-plugins"
    },
    py_modules=['pytest_sequence_markers'],
    requires=['pytest'],
    entry_points={"pytest11": ["pytest_sequence_markers=pytest_sequence_markers",]}
)
