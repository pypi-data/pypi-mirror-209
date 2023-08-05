import setuptools
from cmake_build_extension import BuildExtension, CMakeExtension


setuptools.setup(
    name="AIBoost",
    version="0.0.3",
    author="Musa Sina Ertuğrul",
    author_email="m.s.ertugrul@gmail.com",
    description="AIBoost",
    long_description="",
    ext_modules=[
           CMakeExtension(name="AIBoost", source_dir="/home/musasina/Desktop/AI_Boost/AiLib")
       ],
    cmdclass=dict(build_ext=BuildExtension),
    zip_safe=False,
    extras_require={"test": ["pytest>=6.0"]},
    python_requires=">=3.10",
    options={"bdist_wheel": {"universal": True}}
)
