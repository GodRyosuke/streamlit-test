# ベースイメージの指定
FROM mysql:8.0

# 作成した設定ファイルをコンテナ内にコピー
COPY ./sql.conf /etc/my.conf

CMD ["mysqld"]