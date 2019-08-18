FROM python:3.6-alpine as base                                                                                                
                                                                                                                              
FROM base as builder                                                                                                          
                                                                                                                              
RUN mkdir /install                                                                                                            
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev                                                             
WORKDIR /install                                                                                                              
COPY requirements-prod.txt /requirements-prod.txt                                                                                     
RUN pip install --install-option="--prefix=/install" -r /requirements-prod.txt                                                    
                                                                                                                              
FROM base                                                                                                                     

RUN mkdir /usr/src/app                                                                                                                
COPY --from=builder /install /usr/src/app                                                                                   
COPY . /usr/src/app                                                                                                   
RUN apk --no-cache add libpq                                                                                                
WORKDIR /usr/src/app
ENV FLASK_APP flasky.py
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]