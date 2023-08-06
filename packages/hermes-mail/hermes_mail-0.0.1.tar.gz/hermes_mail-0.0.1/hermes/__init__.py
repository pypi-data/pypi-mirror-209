from ._src.hermes import Client

# Make the functions accessible with from rsrch import *
__all__ = ["Client"]

# Make the functions directly accessible under the package namespace
Client = Client
