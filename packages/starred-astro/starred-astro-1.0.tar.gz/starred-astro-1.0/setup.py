import sys
from distutils.core import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='starred-astro',
    version='1.0',
    author='Kevin Michalewicz',
    author_email='kevinmicha@hotmail.com',
    description='A two-channel deconvolution method with Starlet regularization',
    packages=['starred', 'starred.deconvolution', 'starred.plots', 'starred.psf', 'starred.utils'],
    requires=['astropy', 'dill', 'galsim', 'jax', 'jaxlib', 'jaxopt', 'matplotlib', 'numpy', 'scikitimage', 'scipy', 'optax', 'tqdm'],
    cmdclass={'test': PyTest}
)
