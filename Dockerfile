FROM centos:7
RUN mkdir -p /getBandwidthPool
ADD getbandwidthpool.py /getBandwidthPool/getbandwidthpool.py
RUN yum install -y python3
RUN curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip install softlayer
CMD python3 /getBandwidthPool/getbandwidthpool.py > tempresult.log
