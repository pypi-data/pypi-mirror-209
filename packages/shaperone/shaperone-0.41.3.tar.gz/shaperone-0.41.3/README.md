
SHAPerone is a patched fork of [SHAP](https://pypi.org/project/shap)

Current patches:

* patched an [issue](https://github.com/slundberg/shap/issues/2721) with `beeswarmplot` that 
broke compatibility with `matplotlib>3.5.3`
* removed usage of np.int, bp.bool and np.float [see pull](https://github.com/slundberg/shap/pull/1890). 
The use of np.int has been depreciated since numpy 1.20.0 and removed in `numpy>=1.24.0`.

## Install

SHAP can be installed from either [PyPI](https://pypi.org/project/shaperone) or [conda-forge](https://anaconda.org/conda-forge/shap):

<pre>
pip install shaperone
</pre>
