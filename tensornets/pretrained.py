"""Collection of pretrained models.

This module provides loading functions for pre-trained weights.
All the weight files are converted as a Keras-like format that
serializes every single tensor from the following repositories:

[1]: https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet
     "BAIR Caffe Model Zoo"
[2]: https://github.com/fchollet/keras/tree/master/keras/applications
     "Keras"
[3]: https://github.com/KaimingHe/deep-residual-networks
     "Caffe ResNets"
[4]: https://github.com/facebook/fb.resnet.torch
     "Torch ResNets"
"""
from __future__ import absolute_import

from .utils import get_file
from .utils import init
from .utils import load_keras_weights
from .utils import load_torch_weights


__keras_url__ = 'https://github.com/fchollet/deep-learning-models/' \
                'releases/download/v0.2/'
__model_url__ = 'https://github.com/taehoonlee/deep-learning-models/' \
                'releases/download/'


def load_inception1(scopes):
    """Converted from the [BAIR Caffe Model Zoo][1]."""
    filename = 'inception1.h5'
    weights_path = get_file(
        filename, __model_url__ + 'inception/' + filename,
        cache_subdir='models',
        md5_hash='6a212e3cb60b33f49c372906f18ae4a8')
    return load_keras_weights(scopes, weights_path)


def load_inception3(scopes):
    """Copied from [keras][2] with modifications on the order of weights."""
    filename = 'inception3.h5'
    weights_path = get_file(
        filename, __model_url__ + 'inception/' + filename,
        cache_subdir='models',
        md5_hash='7c4556613c348da3b99b633e1c430fff')
    return load_keras_weights(scopes, weights_path)


def load_resnet50(scopes):
    """Converted from the original [Caffe ResNets][3]."""
    filename = 'resnet50.h5'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='9df0843bdadb58ed24d360564c45b119')
    return load_keras_weights(scopes, weights_path)


def load_resnet101(scopes):
    """Converted from the original [Caffe ResNets][3]."""
    filename = 'resnet101.h5'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='e2434bec605870fb4747e1b93f9f0e47')
    return load_keras_weights(scopes, weights_path)


def load_resnet152(scopes):
    """Converted from the original [Caffe ResNets][3]."""
    filename = 'resnet152.h5'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='e588285d1f919e538515c1f1b1c07b5b')
    return load_keras_weights(scopes, weights_path)


def load_keras_resnet50(scopes):
    """Copied from [keras][2]."""
    filename = 'resnet50_weights_tf_dim_ordering_tf_kernels.h5'
    weights_path = get_file(
        filename, __keras_url__ + filename,
        cache_subdir='models',
        md5_hash='a7b3fe01876f51b976af0dea6bc144eb')
    move_rules = []
    for i in range(2, 6):
        move_rules.append(("bn%da_branch2c" % i, -1))
        move_rules.append(("res%da_branch1" % i, -6))
        move_rules.append(("bn%da_branch1" % i, -6))
    return load_keras_weights(scopes, weights_path, move_rules)


move_rules_fb_resnet_torch = []
for i in range(4, 8):
    move_rules_fb_resnet_torch.append(("%d.0.0.1.0.weight" % i, -18))
    move_rules_fb_resnet_torch.append(("%d.0.0.1.0.bias" % i, -18))
    move_rules_fb_resnet_torch.append(("%d.0.0.1.1.weight" % i, -18))
    move_rules_fb_resnet_torch.append(("%d.0.0.1.1.bias" % i, -18))
    move_rules_fb_resnet_torch.append(("%d.0.0.1.1.running_mean" % i, -18))
    move_rules_fb_resnet_torch.append(("%d.0.0.1.1.running_var" % i, -18))


def load_torch_resnet50(scopes):
    """Converted from the [Torch ResNets][4]."""
    filename = 'resnet_50_cpu.pth'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='5b38c39802c94de00b55596145d304aa')
    return load_torch_weights(scopes, weights_path, move_rules_fb_resnet_torch)


def load_torch_resnet101(scopes):
    """Converted from the [Torch ResNets][4]."""
    filename = 'resnet_101_cpu.pth'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='cb3f0ac4687cb63d5f0861d651da844b')
    return load_torch_weights(scopes, weights_path, move_rules_fb_resnet_torch)


def load_torch_resnet152(scopes):
    """Converted from the [Torch ResNets][4]."""
    filename = 'resnet_152_cpu.pth'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='3339f6aca7f746f8ae7f6ce577efc0c0')
    return load_torch_weights(scopes, weights_path, move_rules_fb_resnet_torch)


def load_torch_resnet200v2(scopes):
    """Converted from the [Torch ResNets][4]."""
    filename = 'resnet_200_cpu.pth'
    weights_path = get_file(
        filename, __model_url__ + 'resnet/' + filename,
        cache_subdir='models',
        md5_hash='220df3970701d3e0608eed887fb95d82')
    return load_torch_weights(scopes, weights_path, move_rules_fb_resnet_torch)


# Simple alias.
load_inception2 = init  # TODO
load_inception4 = init  # TODO

load_resnet50v2 = init  # TODO
load_resnet101v2 = init  # TODO
load_resnet152v2 = init  # TODO
load_resnet200v2 = load_torch_resnet200v2
load_resnext50 = init  # TODO
load_resnext101 = init  # TODO
