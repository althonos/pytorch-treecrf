import unittest

import torch
from torch_treecrf import TreeCRF, TreeMatrix



class TestTreeCRF(unittest.TestCase):

    def test_partition_function(self):
        """Check that `TreeCRF` properly computes the partition function.
        """
        matrix = TreeMatrix([[ 0, 0, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ]])
        crf = TreeCRF(30, matrix)
        features = torch.rand(100, 30)
        probas = crf(features)
        for i in range(features.shape[0]):
            self.assertAlmostEqual(probas[i].sum().item(), 1.0, places=3)


  

