ARG version="3"

FROM python:${version}

ARG workdir="/root"
ENV WORK_DIR=${workdir}
WORKDIR ${WORK_DIR}

COPY django_blog django_blog
COPY tests_behave tests_behave

RUN pip install --upgrade pip
RUN pip install --upgrade -r django_blog/requirements.txt
RUN pip install --upgrade -r tests_behave/requirements.txt
