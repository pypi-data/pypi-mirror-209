# Base image
FROM nvidia/cuda:11.7.1-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# Base packages
RUN \
  apt-get update -qy && \
  apt-get upgrade -qy && \
  apt-get clean && \
  apt-get autoremove --purge -y

RUN \
  apt-get install -qy --no-install-recommends \
    build-essential \
    curl \
    git \
    graphviz \
    libboost-all-dev \
    libtool \
    pandoc \
    python3-pip \
    zip \
  && \
  pip3 install --upgrade \
    pip \
  && \
  pip3 install --upgrade \
    coverage \
    flake8 \
    nbmake \
    pytest \
    setuptools_scm \
    twine \
    xdoctest \
  && \
  pip3 install --upgrade \
    sphinx==5.3.0 \
    sphinx_autodoc_typehints \
    sphinx-rtd-theme \
    sphinx_sitemap \
    sphinxcontrib-bibtex \
    nbsphinx \
    ipywidgets

RUN \
  pip3 install --upgrade \
    colorcet \
    colorspacious \
    h5py \
    matplotlib \
    numba==0.56.3 \
    numpy \
    scipy \
    scikit-image \
    tqdm \
    cupy-cuda11x \
    cython

RUN \
  curl -L http://github.com/astra-toolbox/astra-toolbox/archive/refs/tags/v2.1.0.tar.gz -o astra.tar.gz && \
  tar -xf astra.tar.gz && \
  rm -rf astra.tar.gz && \
  cd /astra-toolbox-2.1.0/build/linux && \
  ./autogen.sh && \
  ./configure --with-cuda=/usr/local/cuda \
              --with-python=/usr/bin/python3 \
              --with-install-type=module \
  && \
  make && \
  make install && \
  cd / && \
  rm -rf /astra-toolbox-2.1.0 && \
  python3 -m pip cache purge

CMD /bin/bash
