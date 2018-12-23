# 安装说明

## 测试环境

| 项       | 描述                                 |
| -------- | ------------------------------------ |
| 操作系统 | centos7.2                            |
| CPU架构  | x86   (Presto目前只支持x86)          |
| Ambari   | 2.6.1                                |
| JDK      | Java 8u162   (Presto要求Java 8u151+) |

## 安装

放置好service之后，安装过程按照ambari添加服务的过程即可。

注意：

- 在安装的时候，安装coordinator服务的主机不要勾选安装worker服务。
- 安装过程进行到配置服务时，填写`discovery.uri`配置项的值，例如：`http://<COORDINATOR_SERVER_FQDN>:8787`。

### 伪分布式

安装的时候不要勾选任何worker服务，也就是只安装coordinator服务。

将`node-scheduler.include-coordinator`配置项的值调整为`true`。

### 分布式
勾选任意数量的worker服务，注意**不要**在安装coordinator服务的主机上勾选worker服务。


## Presto UI
安装完成后，访问`discovery.uri`填写的内容，

## Presto Cli
使用presto-cli:

由于PRESTO这个service里已经写好hive.properties，安装成功后，可以直接连接hive，进行操作。

**连接hive示例**

```
bin/presto --server <COORDINATOR_SERVER_FQDN>:8787 --catalog hive --schema default
```


# 待改进
- 优化coordinator和worker服务之间的安装冲突问题。
- 优化代码
