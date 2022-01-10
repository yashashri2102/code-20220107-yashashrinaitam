import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bmi_Calculator",
    extras_require=dict(tests=['pytest']),
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    author="yashashri2102",
    author_email="naitamyashashri@gmail.com",
    description="Give count of overweight person from a data of height and weight",
    long_description=long_description,
    long_description_content_type="text/markdown",
)