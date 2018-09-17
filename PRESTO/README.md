# 安装说明

安装过程按照ambari安装服务的过程即可。



## 注意

- 在安装的时候，安装coordinator服务的主机不要勾选安装worker。
- 安装过程进行到配置服务时，将`coordinator-properties`和`worker-properties`中的`discovery.uri`选项值修改成正确信息。



# 待改进

- 优化coordinator和worker服务之间的安装冲突问题。
- 自动获取并修正`discovery.uri`值。
- 优化代码