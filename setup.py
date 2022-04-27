import setuptools

setuptools.setup(
    name="pomo_segment",
    version="0.0.1",
    author="Jose Schafer",
    author_email="joseignacio.schafer@gmail.com",
    description="Powerline segment with Pomodor functionality",
    long_description="Powerline segment that with " + \
    "help of a bash command can be use as a Pomodor utility where you can especify a timer. Written in python and inspired in https://github.com/rwxrob/pomo",
    long_description_content_type="text/plain",
    packages=setuptools.find_packages(),
)
