dockerとDjangoでの簡易アプリのメモ書き

ベストプラクティス：
// 設定(プロジェクト)ディレクトリ
的にプロジェクトディレクトリ名はconfigとかの名称がいいらしい
config

// urls.py
URLはアプリごとに設定する

// ビュー
クラスベースで作成すべき
Genericビューとしてさまざまな用途のクラスの恩恵を受けられる
generic viewを利用することで見通しをよくすることができる


Dockerfileとdocker-compose.ymlはsjisにする、日本語コメントを書いている影響かdocker-compose runが失敗する

// 設定(プロジェクト)ディレクトリの作成(最初に打つコマンド)
docker-compose run --rm todo django-admin.py startproject todo_project .

// アプリ作成コマンド
docker-compose run --rm todo python manage.py startapp todo_app

// runserverはdocker-compose up
docker-compose up

// makemigratiton
docker-compose run --rm todo python manage.py makemigrations

// migrate
docker-compose run --rm todo python manage.py migrate

// createsuperuser
docker-compose run --rm todo python manage.py createsuperuser

コマンド順番
1.migrate
2.docker-compose up
3.変更後のmigrate適用など

<参考：よく使うコマンド>
// コンテナ一覧
docker container ls

// 起動しているコンテナの一覧
docker ps

// 停止コンテナも見たい時
docker ps -a

// image一覧
docker image ls

// image削除
docker rmi <image_id>

// docker-composeで作られたコンテナ、イメージ、ボリュームすべてを削除
docker-compose down --rmi all --volumes

// コンテナに入る
docker exec -i -t コンテナ名 bash

https://docs.docker.jp/compose/django.html

---------------------------------------------------------------------------------------------------
設定ファイルの説明

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


# settings.py
DEBUG = TRUEの部分はアプリ公開時はFALSEにする
ALLOWED_HOSTS:指定したサーバからのアクセスの許可
