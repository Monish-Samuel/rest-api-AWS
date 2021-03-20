FROM python:3.7-alpine
COPY .  /github_api
WORKDIR /github_api
RUN pip install -r requirements.txt
EXPOSE  5000
CMD ["python", "github_api/issues_api.py"]