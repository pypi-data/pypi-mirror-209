# 用之前的准备：
    * pip install --upgrade tencentcloud-sdk-python
    * https://console.cloud.tencent.com/cam/capi
    * 在以上网址中获取你的腾讯云apikey,并填入到该插件的__init__.py文件指定位置中
## 该插件优先级为100，若前面所有插件都无法拦截消息，则会使用ai聊天进行处理。