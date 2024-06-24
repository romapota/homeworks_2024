class Layer:
    def __init__(self, next_layer=None):
        self.next_layer = next_layer
    def __call__(self, next_layer):
        self.next_layer = next_layer
        return self.next_layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name= 'Input'

class Dense(Layer):
    name= 'Dense'
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, layer):
        self.next_layer = layer
    def __iter__(self):
        return self
    def __next__(self):
        layer = self.next_layer
        if self.next_layer==None:
            raise StopIteration
        self.next_layer=self.next_layer.next_layer
        return layer