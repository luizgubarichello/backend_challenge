# Usar uma imagem base do Python 3.10.6
FROM python:3.10.6

# Definir a variável de ambiente PYTHONUNBUFFERED para evitar o buffering da saída do Python
ENV PYTHONUNBUFFERED 1

# Instalar Cron
RUN apt-get update
RUN apt-get -y install cron

# Criar um diretório para o nosso projeto dentro do container
RUN mkdir /code

# Definir o diretório de trabalho como o diretório criado
WORKDIR /code

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /code/

# Instalar as dependências do projeto usando o pip
RUN pip install -r requirements.txt

# Copiar o restante dos arquivos do projeto para o diretório de trabalho
COPY . /code/
