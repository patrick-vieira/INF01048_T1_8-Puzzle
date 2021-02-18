import sys

# import resource as resource


class RecursionLimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_recursion_limit = sys.getrecursionlimit()
        # self.old_rlimit_limit = resource.getrlimit(resource.RLIMIT_STACK)

    def __enter__(self):
        sys.setrecursionlimit(self.limit)
        # resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_recursion_limit)
        #resource.setrlimit(resource.RLIMIT_STACK, self.old_rlimit_limit)
