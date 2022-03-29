from importlib import metadata

try:
  __version__ = metadata.version("acme.service.oculus")
except metadata.PackageNotFoundError:
  __version__ = "unknown"
finally:
  del metadata

from .instructions import translate
