dockerとDjangoでの簡易アプリのメモ書き

Dockerfileとdocker-compose.ymlはsjisにする、日本語コメントを書いている影響かdocker-compose runが失敗する

// 最初に打つコマンド
docker-compose run web_test django-admin.py startproject django_test .



<参考>
// コンテナ一覧
docker container ls

// 起動しているコンテナの一覧
docker ps

// 停止コンテナも見たい時
docker ps -a

// image削除
docker rmi <image_id>