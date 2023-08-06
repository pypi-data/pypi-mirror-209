import pytest  # noqa:F401
import numpy as np

from numba import cuda

from mumott.data_handling import DataContainer
from mumott.core import john_transform_cuda, john_transform_adjoint_cuda

dc = DataContainer('tests/test_half_circle.h5')
gm = dc.geometry
fields = [np.arange(192, dtype=np.float32).reshape(4, 4, 4, 3)]
outs = [np.array([[[[174., 178., 182.],
                   [186., 190., 194.],
                   [198., 202., 206.],
                   [204., 208., 212.]],
                  [[366., 370., 374.],
                   [378., 382., 386.],
                   [390., 394., 398.],
                   [396., 400., 404.]],
                  [[558., 562., 566.],
                   [570., 574., 578.],
                   [582., 586., 590.],
                   [588., 592., 596.]],
                  [[654., 658., 662.],
                   [666., 670., 674.],
                   [678., 682., 686.],
                   [684., 688., 692.]]]])]

out_fields = [np.arange(48)]
projs = [np.arange(48, dtype=np.float32).reshape(1, 4, 4, 3)]


@pytest.mark.parametrize('field,out', [t for t in zip(fields, outs)])
def test_john_transform_cuda(field, out):
    vector_p = np.array([[0, 1., 0.]])
    vector_j = np.array([[1, 0., 0.]])
    vector_k = np.array([[0, 0., 1.]])
    offsets_j = np.zeros((len(gm)))
    offsets_k = np.zeros((len(gm)))
    projections = np.zeros_like(out).astype(np.float32)
    john_transform_cuda(field, projections, vector_p, vector_j, vector_k, offsets_j, offsets_k)
    print(projections)
    assert np.allclose(projections, out)


@pytest.mark.parametrize('proj,out', [t for t in zip(projs, out_fields)])
def test_john_transform_adjoint_cuda(proj, out):
    vector_p = np.array([[0, 1., 0.]])
    vector_j = np.array([[1, 0., 0.]])
    vector_k = np.array([[0, 0., 1.]])
    offsets_j = np.zeros((len(gm)))
    offsets_k = np.zeros((len(gm)))
    field = np.zeros((4, 4, 4, 3,), dtype=np.float32)
    john_transform_adjoint_cuda(field, proj, vector_p, vector_j, vector_k, offsets_j, offsets_k)
    print(field)
    assert np.allclose(field[:, 0].ravel(), out)


@pytest.mark.parametrize('field,out', [t for t in zip(fields, outs)])
def test_device_john_transform_cuda(field, out):
    vector_p = np.array([[0, 1., 0.]])
    vector_j = np.array([[1, 0., 0.]])
    vector_k = np.array([[0, 0., 1.]])
    offsets_j = np.zeros((len(gm)))
    offsets_k = np.zeros((len(gm)))
    projections = cuda.to_device(np.zeros_like(out).astype(np.float32))
    john_transform_cuda(cuda.to_device(field), projections,
                        vector_p, vector_j, vector_k, offsets_j, offsets_k)
    assert np.allclose(projections.copy_to_host(), out)


@pytest.mark.parametrize('proj,out', [t for t in zip(projs, out_fields)])
def test_device_john_transform_adjoint_cuda(proj, out):
    vector_p = np.array([[0, 1., 0.]])
    vector_j = np.array([[1, 0., 0.]])
    vector_k = np.array([[0, 0., 1.]])
    offsets_j = np.zeros((len(gm)))
    offsets_k = np.zeros((len(gm)))
    field = cuda.to_device(np.zeros((4, 4, 4, 3,), dtype=np.float32))
    john_transform_adjoint_cuda(field, cuda.to_device(proj),
                                vector_p, vector_j, vector_k, offsets_j, offsets_k)
    assert np.allclose(field.copy_to_host()[:, 0].ravel(), out)
