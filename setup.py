import setuptools

setuptools.setup(
    name="icanhazmodel",
    version="0.0.3",
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        icanhazmodel=icanhazmodel.commands:cli
    '''
)
