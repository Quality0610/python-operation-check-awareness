dockerとDjangoでの簡易アプリのメモ書き

// 設定(プロジェクト)ディレクトリ
ベストプラクティス的にプロジェクトディレクトリ名はconfigとかの名称がいいらしい
config

// アプリディレクトリ
example_app

Dockerfileとdocker-compose.ymlはsjisにする、日本語コメントを書いている影響かdocker-compose runが失敗する

// 設定(プロジェクト)ディレクトリの作成(最初に打つコマンド)
docker-compose run --rm web1 django-admin.py startproject config .

// アプリ作成コマンド
docker-compose run --rm web1 python manage.py startapp example_app


<参考>
// コンテナ一覧
docker container ls

// 起動しているコンテナの一覧
docker ps

// 停止コンテナも見たい時
docker ps -a

// image削除
docker rmi <image_id>

// docker-composeで作られたコンテナ、イメージ、ボリュームすべてを削除
docker-compose down --rmi all --volumes

// コンテナに入る
docker exec -i -t コンテナ名 bash

https://docs.docker.jp/compose/django.html


<Dockerfile>
FROM python:3.6

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# ホストPCの各種ファイルをcodeディレクトリにコピーする
# COPY . /code/

<docker-compose.yml>
version: '3'  # Docker Composeのバージョン
services:
  db:
    image: postgres
  web1:  # コンテナに名前をつける
    build: .  # Dockerfileがあるディレクトリへのパス
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code  # ホストPCのカレントディレクトリとコンテナ内のcodeディレクトリを同期させる
    ports:
      - "8000:8000"
    depends_on:
      - db