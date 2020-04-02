
# Dockerfile to build Ubuntu:14.04 + Python3.6 + Qt5
FROM ubuntu:14.04

# Sets language to UTF8 : this works in pretty much all cases
ENV LANG en_US.UTF-8
RUN locale-gen $LANG
ENV DOCKER_ANDROID_LANG en_US

# Add some dep
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y \
  autoconf \
  build-essential \
  bzip2 \
  curl \
  gcc \
  git \
  groff \
  lib32stdc++6 \
  lib32z1 \
  lib32z1-dev \
  lib32ncurses5 \
  lib32bz2-1.0 \
  libc6-dev \
  libgmp-dev \
  libmpc-dev \
  libmpfr-dev \
  libxslt-dev \
  libxml2-dev \
  m4 \
  make \
  ncurses-dev \
  ocaml \
  openssh-client \
  pkg-config \
  python-software-properties \
  rsync \
  software-properties-common \
  unzip \
  wget \
  zip \
  zlib1g-dev \
  cmake \
  python3 \
  python3-pyqt5\
  libffi-dev \
  libssl-dev \
  xvfb \
  --no-install-recommends

RUN pip3 install ipython lxml
RUN pip3 install QuantLib-Python
RUN pip3 install QDarkStyle
RUN pip3 install matplotlib
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
