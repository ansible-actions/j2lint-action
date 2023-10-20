# hadolint ignore=DL3007
FROM python:latest

LABEL "maintainer"="L3D <l3d@c3woc.de>"
LABEL "repository"="https://github.com/ansible-actions/j2lint-action.git"
LABEL "homepage"="https://github.com/ansible-actions/j2lint-action"

# hadolint ignore=DL3008,DL3013,SC1091
RUN pip3 install --no-cache-dir j2lint

COPY j2_docker.py /j2_docker.py
CMD [ "python", "/j2_docker.py"]
