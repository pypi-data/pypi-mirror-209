import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="RecruitPlotEasy",
	version="3.2.2",
	author="Kenji Gerhardt",
	author_email="kenji.gerhardt@gmail.com",
	description="A tool for visualizing short read mapping efforts",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	include_package_data=True,
	python_requires='>=3.9',
	install_requires=[
		'numpy',
		'pyrodigal>=2.0',
		'plotly',
	],
	entry_points={
		"console_scripts": [
			"rpe=rpe2_code.rpe2_main:main",
			"recruitploteasy=rpe2_code.rpe2_main:main"
		]
	}
)

