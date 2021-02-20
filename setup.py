from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='AOB',
      version='0.0.1',
      description='Sat0ri!',
      executables=executables)