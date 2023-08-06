import setuptools


install_requires = [
    'pyqt5'
]
setuptools.setup(
	name="pysbapi", 
	version="0.1.1",
	author="NH 선물",
	author_email="nhretail@futures.co.kr",
	description="써핑보드 파이썬 API 라이브러리",
	packages=setuptools.find_packages(),
    install_requires=install_requires,
    keywords="NH, python, API, 써핑보드"
)
	