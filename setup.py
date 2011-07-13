from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

module = 'spint'

def cext(ext_name):
    return Extension('%s.%s' % (module, ext_name),
                     ['%s/%s.pyx' % (module, ext_name)],
                     include_dirs=[numpy.get_include()])

setup(name=module,
      version='0.0',
      description='Interpolation using sparse matrix operators',
      author='Stefan van der Walt',
      author_email='stefan@sun.ac.za',
      license='BSD',
      url='http://mentat.za.net/supreme',

      # -----

      packages=[module],
      cmdclass = {'build_ext': build_ext},
      ext_modules = [cext('operators')]
)

