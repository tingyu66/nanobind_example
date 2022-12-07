import torch
import math
from nanobind_example import *

# example adapted from https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html
class LegendrePolynomial3(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input, foo):
        ctx.foo = foo
        ctx.save_for_backward(input)
        return 0.5 * (5 * input ** 3 - 3 * input)

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        return grad_output * 1.5 * (5 * input ** 2 - 1), None

input_tensor = torch.rand(3,3)
input_tensor.requires_grad_()
foo = make_foo(1, 0.5)

output = LegendrePolynomial3.apply(input_tensor, foo)
grad_output = torch.rand_like(output)
output.backward(grad_output)
