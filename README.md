# 説明
FastApiを使った何か。

# ディレクトリ構造

```
├── README.md
├── requirements.txt
└── app
    └── templates
    |   ├── form.html
    |   ├── layout.html
    |   └── result.html
    ├──auth.py
    ├──controllers.py
    ├──db.py
    ├──create_sampletable.py
    ├──models.py
    ├──run.py
    └──urls.py

```

# Requirements
- requirements.txtからpip installすれば必須

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
```

メモ
- Basic認証実装済み
- run.pyを実行でサーバー実行(デフォルトは8000番ポート テスト時は8888番ポート)
- create_table.pyでsampleuser(username:user password:123456)を作成
- ユーザデータはdb.sqlite3(app内部)に存在
- apiドキュメントはurlの後ろに「/docs」を記入で確認可能
- 
