from invoke import Collection
from . import meta_tasks

# Create namespaces
ns = Collection()
ns.add_collection(Collection.from_module(meta_tasks, 'meta'))