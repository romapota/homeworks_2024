class Callback:
    def __init__(self, path, router_cls):
        self.path = path
        
        self.router_cls = router_cls
    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)
