from setuptools import setup

APP = ['WeeNu.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['rumps', 'datetime', 'webbrowser'],
    'iconfile': 'resources/WeeNu.icns',
    'plist': {
        'CFBundleShortVersionString': '0.1',
        'NSHumanReadableCopyright': u"Copyright © 2024, William Wijk, MIT License",
    },
}

setup(
    app=APP,
    name="WeeNu",
    version="0.1",
    description="WeeNu: Week number in your menubar",
    long_description="""WeeNu is a minimalist macOS menu bar application designed for simplicity and efficiency. With a clean and unobtrusive interface, it serves one purpose: to show the current week number at a glance. Perfect for professionals, students, and anyone who plans their tasks and events on a weekly basis, this app integrates seamlessly into your daily workflow, ensuring you always know the current week number without needing to open a calendar. Its lightweight design means it runs smoothly in the background, providing you with instant access to the week number with just a glance at your menu bar.""",  # Long description
    author="William Wijk (QVL)",
    author_email="hello@qvl.se",
    license="MIT",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    url="https://github.com/mullweisser/mac-weenu",
    project_urls={
        "Bug Tracker": "https://github.com/mullweisser/mac-weenu/issues",
        "Documentation": "https://github.com/mullweisser/mac-weenu",
        "Source Code": "https://github.com/mullweisser/mac-weenu",
    },
)