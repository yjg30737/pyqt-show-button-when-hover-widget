from setuptools import setup, find_packages

setup(
    name='pyqt-show-button-when-hover-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_show_button_when_hover_widget.style': ['button.css'],
                  'pyqt_show_button_when_hover_widget.ico': ['add.png', 'delete.png']},
    description='PyQt show the button to the bottom right of the widget when mouse cursor hover',
    url='https://github.com/yjg30737/pyqt-show-button-when-hover-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)