import json
import sys
import os
from importlib import import_module

def split_class_path(class_path: str) -> tuple[str, str]:

    package_name = '.'.join(class_path.split('.')[:-1])
    class_name = class_path.split('.')[-1]

    return package_name, class_name

def jsonFile2Dict(jsonFile: str) -> tuple[int, dict]:

    try:
        f = open(jsonFile)
        data = json.load(f)
    except FileNotFoundError as e:
        return -1, dict(error="JsonFile is not found : {}".format(jsonFile))
    except json.decoder.JSONDecodeError as e:
        return -2, dict(error="JSONDecodeError occured : {}".format(sys.exc_info()[1]))
    
    return 1, data

def get_class_object(class_path: str) -> object:
        
    package_name, class_name = split_class_path(class_path)

    if package_name is None:
        raise RuntimeError("There is no package name in [{}].",format(class_path))

    try:
      package_module = sys.modules[package_name]\
                    if package_name in sys.modules else import_module(package_name)

    except ImportError:
        raise RuntimeError("Package [{}] of class [{}] isn't able to be imported."\
                        .format(package_name, class_path))

    if not hasattr(package_module, class_name):
        raise RuntimeError("Package [{}] has no attribute [{}]."\
                        .format(package_name, class_name))

    class_obj = getattr(package_module, class_name)

    return class_obj

class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance
