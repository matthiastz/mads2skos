# encoding=utf-8
from .skosify import skosify
from .config import Config

__version__ = '1.0.0'  # Use bumpversion to update
__all__ = ['skosify', 'config']


def config(filename=None):
    """Get default configuration and optional settings from config file."""
    return vars(Config(filename))
