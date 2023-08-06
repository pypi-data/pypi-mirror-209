from setuptools import setup, Extension
import numpy as np

# Configuración de la extensión de C++
UCmoduleC = Extension('UCmoduleC',
                      sources=['Cpp/pythonETS.cpp', 'Cpp/pythonUComp.cpp'],
                      include_dirs=['Cpp',
                                    'D:\Program Files\python311\include',
                                    'D:\armadillo-12.2.0\include',
                                    'D:\Archivos de Programa\python\pybind11\include'],
                      libraries=['armadillo'],
                      library_dirs=['D:\Program Files\python311\libs',
                                    'D:\armadillo-12.2.0\examples\lib_win64'],
                      extra_link_args=['-L/D:\armadillo-12.2.0\examples\lib_win64'],
                      language='c++')

# Configuración del paquete de Python
setup(name='UComp',
      version='4.0.1',
      description='Modelling and forecasting univariate time series',
      author='Diego J. Pedregal',
      author_email='diego.pedregal@uclm.es',
      ext_modules=[UCmoduleC],
      include_dirs=[np.get_include()])


