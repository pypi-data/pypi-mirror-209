from setuptools import setup, find_packages
import subprocess

def get_git_version():
    try:
        version = subprocess.check_output(["git", "describe", "--always"]).strip().decode()
    except Exception:
        version = "0.1.9-beta"
    return version

def get_git_description():
    try:
        description = subprocess.check_output(["git", "describe", "--all"]).strip().decode()
    except Exception:
        description = "好爸爸的每个类都是被用来继承的。作为顶层设计，它为通用行为实现了最基础的标准实践。比如自动埋点、权限控制、性能分析、任务流转、异常处理、单元测试等。"
    return description

setup(
    name="baba",
    version=get_git_version(),
    packages=find_packages(),
    author="jie.kim",
    author_email="ubbs@163.com",
    license='Apache',
    description=get_git_description(),
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://pypi.org/project/baba/",
)

#  语义化版本  https://semver.org/lang/zh-CN/
