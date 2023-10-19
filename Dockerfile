# python 3.8에서 실행
# melanoma_server를 옮김
# 그안에 requiremetes.sh 실행해서 필요한 패키지 다운로드
# myserver.py실행
FROM sjw980523/python-client:v1
RUN mkdir server
WORKDIR /server
COPY . .
ENTRYPOINT ["python","-u", "myserver.py"]
