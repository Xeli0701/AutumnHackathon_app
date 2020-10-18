# 説明
FastApiを使ったプロプライエタリツイッター。

# ディレクトリ構造
model・sqlite3などのデータは.gitignoreしてます。
(modelはあとで上げるかも)
```
AutumnHackathon_app
├── README.md
├── app
│   ├── auth.py
│   ├── controllers.py
│   ├── create_sampletable.py
│   ├── db.py
│   ├── db.sqlite3
│   ├── generativeSystem.py
│   ├── models.py
│   ├── run.py
│   ├── templates
│   │   ├── chat.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── register.html
│   │   └── register_complete.html
│   ├── urls.py
├── models
│   └── model.pt
└── requirements.txt
```

# Requirements
- requirements.txtからpip install

開発時は以下の通り
```
astroid==2.4.2
click==7.1.2
colorama==0.4.4
fastapi==0.61.1
h11==0.11.0
isort==5.6.4
Jinja2==2.7
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1       
mccabe==0.6.1
pydantic==1.6.1
pylint-django==2.3.0    
pylint-plugin-utils==0.6
python-multipart==0.0.5 
six==1.15.0
SQLAlchemy==1.3.20      
starlette==0.13.6       
toml==0.10.1
uvicorn==0.12.1
wrapt==1.12.1
OpenNMT-py==1.1.1
```

## OpenNMT-py==1.1.1に関して
生成ベース対話システムのコア部分(PyTorchの翻訳システム) 本来大本のシステムを作ったときは0.9.2だが現在は1.1.1 pipでも入るけど不具合の可能性あり(現状は平気)

インストール方法
- pip install OpenNMT-py

or

- git clone http://github.com/OpenNMT/OpenNMT-py.git -b 0.9.2
- cd OpenNMT-py
- pip install -r requirements.txt
- sudo python3 setup.py install

メモ
- Basic認証実装済み
- run.pyを実行でサーバー実行(デフォルトは8000番ポート テスト時は8888番ポート)
- create_table.pyでsampleuser(username:user password:123456)を作成
- ユーザデータはdb.sqlite3(app内部)に存在
- apiドキュメントはurlの後ろに「/docs」を記入で確認可能
- generativeSystem.pyはopenNMTを使った対話システム　models内部のものを使う（テスト時点では150000Step学習のもの）
- フルではないけど一応レスポンシブ対応
