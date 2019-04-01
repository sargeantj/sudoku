FROM ubuntu:latest

# Update
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


# Install dependencies
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# Get the model
COPY sudoku /sudoku
COPY model /model

# OPEN CV
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get install -y build-essential apt-utils

RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev \
  libavformat-dev libswscale-dev
RUN  apt-get update && apt-get install -y python-dev python-numpy \
  python3 python3-pip python3-dev libtbb2 libtbb-dev \
  libjpeg-dev libdc1394-22-dev \
  python-opencv libopencv-dev python-pycurl \
  libatlas-base-dev gfortran webp qt5-default libvtk6-dev zlib1g-dev

RUN pip3 install numpy

RUN apt-get install -y python-pip
RUN pip install --upgrade pip

RUN cd ~/ &&\
    git clone https://github.com/Itseez/opencv.git &&\
    git clone https://github.com/Itseez/opencv_contrib.git &&\
    cd opencv && mkdir build && cd build && cmake  -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. && \
    make -j4 && make install && ldconfig && rm -rf ~/opencv*  # Remove the opencv folders to reduce image size


EXPOSE 5000
CMD ["python", "sudoku/app.py"]
