# wechat-verify
微信公众号业务域名验证

## 启动服务

```bash
git clone https://github.com/waketzheng/wechat-verify
cd wechat-verify
poetry shell
poetry install
./runserver.bash
```

## Nginx配置

```
location ~ MP_verify_[a-zA-Z0-9]*\.txt$ {
    proxy_pass http://127.0.0.1:10240;
}
```
