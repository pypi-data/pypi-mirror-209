import gc
import random
import sys

import jax
import jax.config
import jax.random as jrandom
import psutil
import pytest


jax.config.update("jax_enable_x64", True)


@pytest.fixture()
def getkey():
    def _getkey():
        # Not sure what the maximum actually is but this will do
        return jrandom.PRNGKey(random.randint(0, 2**31 - 1))

    return _getkey


# Hugely hacky way of reducing memory usage in tests.
# JAX can be a little over-happy with its caching; this is especially noticable when
# performing tests and therefore doing an unusual amount of compilation etc.
# This can be enough to exceed the 8GB RAM available to Ubuntu instances on GitHub
# Actions.
@pytest.fixture(autouse=True)
def clear_caches():
    process = psutil.Process()
    if process.memory_info().vms > 4 * 2**30:  # >4GB memory usage
        jax.clear_backends()
        for module_name, module in sys.modules.copy().items():
            if module_name.startswith("jax"):
                if module_name not in ["jax.interpreters.partial_eval"]:
                    for obj_name in dir(module):
                        obj = getattr(module, obj_name)
                        if hasattr(obj, "cache_clear"):
                            try:
                                print(f"Clearing {obj}")
                                if "Weakref" not in type(obj).__name__:
                                    obj.cache_clear()
                            except Exception:
                                pass
        gc.collect()
