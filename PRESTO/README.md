# 安装说明

## 环境要求
- CPU架构：x86
- JDK：Java 8u151+


## 安装
放置好service之后，安装过程按照ambari添加服务的过程即可。

注意：

- 在安装的时候，安装coordinator服务的主机不要勾选安装worker。
- 安装过程进行到配置服务时，填写`discovery.uri`选项值，例如：`http://<coordinator-host>:8787`。

### 伪分布式
安装的时候不要勾选任何worker服务，也就是只安装coordinator服务。

将`node-scheduler.include-coordinator`配置项调节为`true`。

### 分布式
勾选任意数量的worker服务，主要不要勾选要安装coordinator服务的主机上的worker服务。


## Presto UI
安装完成后，访问`discovery.uri`填写的内容，

## Presto Cli
使用presto-cli:

**连接hive**

```
bin/presto --server example.net:8787 --catalog hive --schema default
```


# 待改进
- 优化coordinator和worker服务之间的安装冲突问题。
- 优化代码