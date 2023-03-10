import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commonroad-search",
    version="2022.1",
    author="Cyber-Physical Systems Group, Technical University of Munich",
    author_email="commonroad@lists.lrz.de",
    license="BSD License",
    description="Search-based motion planners with motion primitives",
    long_description=long_description,
    url="https://gitlab.lrz.de/tum-cps/commonroad-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    
    # Requirements
    python_requires='>3.7',
    install_requires=['commonroad-io>=2022.3',
                      'commonroad-drivability-checker>=2022.2.1',
                      'commonroad-route-planner>=2022.3',
                      'tqdm~=4.64',
                      'networkx>=2.4',
                      'ipywidgets~=7.5.1',
                      'ipython-autotime~=0.1',
                      'matplotlib~=3.3.2',
                      'numpy~=1.21.6',
                      'ipython~=7.18.1',
                      'pyyaml~=5.3.1',
                      'imageio~=2.9.0',
                      'shapely>=1.6.4.post2',
                      'setuptools>=42.0.1',
                      'triangle>=20200424',
                    ],

)

