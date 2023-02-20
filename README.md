# pythonのstreamlitのテスト
## installation
```bash
git clone https://github.com/GodRyosuke/streamlit-test.git
cd streamlit-test
mkdir db
cd docker
docker compose build
docker compose up -d
```
## 実行
Streamlit
```bash
docker compose exec asdf bash
# コンテナ内
cd src
streamlit run app.py
```
localhost:8888にアクセスする．
