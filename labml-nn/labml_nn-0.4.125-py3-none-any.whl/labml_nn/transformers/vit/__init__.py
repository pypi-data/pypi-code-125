"""
---
title: Vision Transformer (ViT)
summary: >
 A PyTorch implementation/tutorial of the paper
 "An Image Is Worth 16x16 Words: Transformers For Image Recognition At Scale"
---

#  Vision Transformer (ViT)

This is a [PyTorch](https://pytorch.org) implementation of the paper
[An Image Is Worth 16x16 Words: Transformers For Image Recognition At Scale](https://papers.labml.ai/paper/2010.11929).

Vision transformer applies a pure transformer to images
without any convolution layers.
They split the image into patches and apply a transformer on patch embeddings.
[Patch embeddings](#PathEmbeddings) are generated by applying a simple linear transformation
to the flattened pixel values of the patch.
Then a standard transformer encoder is fed with the patch embeddings, along with a
classification token `[CLS]`.
The encoding on the `[CLS]` token is used to classify the image with an MLP.

When feeding the transformer with the patches, learned positional embeddings are
added to the patch embeddings, because the patch embeddings do not have any information
about where that patch is from.
The positional embeddings are a set of vectors for each patch location that get trained
with gradient descent along with other parameters.

ViTs perform well when they are pre-trained on large datasets.
The paper suggests pre-training them with an MLP classification head and
then using a single linear layer when fine-tuning.
The paper beats SOTA with a ViT pre-trained on a 300 million image dataset.
They also use higher resolution images during inference while keeping the
patch size the same.
The positional embeddings for new patch locations are calculated by interpolating
learning positional embeddings.

Here's [an experiment](experiment.html) that trains ViT on CIFAR-10.
This doesn't do very well because it's trained on a small dataset.
It's a simple experiment that anyone can run and play with ViTs.

[![View Run](https://img.shields.io/badge/labml-experiment-brightgreen)](https://app.labml.ai/run/8b531d9ce3dc11eb84fc87df6756eb8f)
"""

import torch
from torch import nn

from labml_helpers.module import Module
from labml_nn.transformers import TransformerLayer
from labml_nn.utils import clone_module_list


class PatchEmbeddings(Module):
    """
    <a id="PatchEmbeddings"></a>

    ## Get patch embeddings

    The paper splits the image into patches of equal size and do a linear transformation
    on the flattened pixels for each patch.

    We implement the same thing through a convolution layer, because it's simpler to implement.
    """

    def __init__(self, d_model: int, patch_size: int, in_channels: int):
        """
        * `d_model` is the transformer embeddings size
        * `patch_size` is the size of the patch
        * `in_channels` is the number of channels in the input image (3 for rgb)
        """
        super().__init__()

        # We create a convolution layer with a kernel size and and stride length equal to patch size.
        # This is equivalent to splitting the image into patches and doing a linear
        # transformation on each patch.
        self.conv = nn.Conv2d(in_channels, d_model, patch_size, stride=patch_size)

    def forward(self, x: torch.Tensor):
        """
        * `x` is the input image of shape `[batch_size, channels, height, width]`
        """
        # Apply convolution layer
        x = self.conv(x)
        # Get the shape.
        bs, c, h, w = x.shape
        # Rearrange to shape `[patches, batch_size, d_model]`
        x = x.permute(2, 3, 0, 1)
        x = x.view(h * w, bs, c)

        # Return the patch embeddings
        return x


class LearnedPositionalEmbeddings(Module):
    """
    <a id="LearnedPositionalEmbeddings"></a>

    ## Add parameterized positional encodings

    This adds learned positional embeddings to patch embeddings.
    """

    def __init__(self, d_model: int, max_len: int = 5_000):
        """
        * `d_model` is the transformer embeddings size
        * `max_len` is the maximum number of patches
        """
        super().__init__()
        # Positional embeddings for each location
        self.positional_encodings = nn.Parameter(torch.zeros(max_len, 1, d_model), requires_grad=True)

    def forward(self, x: torch.Tensor):
        """
        * `x` is the patch embeddings of shape `[patches, batch_size, d_model]`
        """
        # Get the positional embeddings for the given patches
        pe = self.positional_encodings[x.shape[0]]
        # Add to patch embeddings and return
        return x + pe


class ClassificationHead(Module):
    """
    <a id="ClassificationHead"></a>

    ## MLP Classification Head

    This is the two layer MLP head to classify the image based on `[CLS]` token embedding.
    """
    def __init__(self, d_model: int, n_hidden: int, n_classes: int):
        """
        * `d_model` is the transformer embedding size
        * `n_hidden` is the size of the hidden layer
        * `n_classes` is the number of classes in the classification task
        """
        super().__init__()
        # First layer
        self.linear1 = nn.Linear(d_model, n_hidden)
        # Activation
        self.act = nn.ReLU()
        # Second layer
        self.linear2 = nn.Linear(n_hidden, n_classes)

    def forward(self, x: torch.Tensor):
        """
        * `x` is the transformer encoding for `[CLS]` token
        """
        # First layer and activation
        x = self.act(self.linear1(x))
        # Second layer
        x = self.linear2(x)

        #
        return x


class VisionTransformer(Module):
    """
    ## Vision Transformer

    This combines the [patch embeddings](#PatchEmbeddings),
    [positional embeddings](#LearnedPositionalEmbeddings),
    transformer and the [classification head](#ClassificationHead).
    """
    def __init__(self, transformer_layer: TransformerLayer, n_layers: int,
                 patch_emb: PatchEmbeddings, pos_emb: LearnedPositionalEmbeddings,
                 classification: ClassificationHead):
        """
        * `transformer_layer` is a copy of a single [transformer layer](../models.html#TransformerLayer).
         We make copies of it to make the transformer with `n_layers`.
        * `n_layers` is the number of [transformer layers](../models.html#TransformerLayer).
        * `patch_emb` is the [patch embeddings layer](#PatchEmbeddings).
        * `pos_emb` is the [positional embeddings layer](#LearnedPositionalEmbeddings).
        * `classification` is the [classification head](#ClassificationHead).
        """
        super().__init__()
        # Patch embeddings
        self.patch_emb = patch_emb
        self.pos_emb = pos_emb
        # Classification head
        self.classification = classification
        # Make copies of the transformer layer
        self.transformer_layers = clone_module_list(transformer_layer, n_layers)

        # `[CLS]` token embedding
        self.cls_token_emb = nn.Parameter(torch.randn(1, 1, transformer_layer.size), requires_grad=True)
        # Final normalization layer
        self.ln = nn.LayerNorm([transformer_layer.size])

    def forward(self, x: torch.Tensor):
        """
        * `x` is the input image of shape `[batch_size, channels, height, width]`
        """
        # Get patch embeddings. This gives a tensor of shape `[patches, batch_size, d_model]`
        x = self.patch_emb(x)
        # Add positional embeddings
        x = self.pos_emb(x)
        # Concatenate the `[CLS]` token embeddings before feeding the transformer
        cls_token_emb = self.cls_token_emb.expand(-1, x.shape[1], -1)
        x = torch.cat([cls_token_emb, x])

        # Pass through transformer layers with no attention masking
        for layer in self.transformer_layers:
            x = layer(x=x, mask=None)

        # Get the transformer output of the `[CLS]` token (which is the first in the sequence).
        x = x[0]

        # Layer normalization
        x = self.ln(x)

        # Classification head, to get logits
        x = self.classification(x)

        #
        return x
