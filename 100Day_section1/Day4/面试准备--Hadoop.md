# 广发基金面试准备

## 一、Hadoop 知识整理

### 1.定义： Hadoop是一个由Apache基金会所开发的分布式系统基础架构。 用户可以在不了解分布式底层细节的情况下，开发分布式程序。Hadoop实现了一个分布式文件系统(HDFS)。 HDFS有高容错的特点，并且设计用来部署在低廉的硬件上；同时，HDFS提供了高吞吐量来访问应用程序的数据，适合有着超大数据集的应用程序。Hadoop的框架核心设计就是HDFS和MapReduce，HDFS为海量的数据提供了存储，MapReduce则为海量的数据提供了计算。

## 2.优点：

* Hadoop是一个能够对大量数据进行分布式处理的软件，它可靠，高效，可伸缩
* Hadoop的可靠性：它假设计算元素和存储过程会失败，因此它维护多个工作数据副本，确保能够针对失败的节点重新分布处理
* Hadoop的高效性：它以并行的方式工作，通过并行处理加快处理速度
* Hadoop是可伸缩的，能够处理PB级数据

## 3.核心架构：

Hadoop由许多元素组成，其最底部是Hadoop Distributed File System(HDFS), 它存储Hadoop集群中所有存储节点上的文件。HDFS的上一层是MapReduce引擎，该引擎由JobTracker和TaskTracker组成。通过对Hadoop分布式计算平台最核心的分布式文件系统HDFS、MapReduce处理过程，以及数据仓库工具Hive和分布式数据库Hbase的介绍，基本涵盖了Hadoop分布式平台的所有技术核心

### 3.1 HDFS

对外部客户机而言，HDFS就像一个传统的分级文件系统。可以创建、删除、移动或者重命名文件。但是HDFS的架构是基于一组特定的节点构建的/这些节点包括：NameNode(在1.x版本中有且仅有一个)，它在HDFS内部提供元数据服务；DataNode，它为HDFS提供存储块。由于仅存在一个NameNode，因此这是HDFS1.x版本的一个缺点(单点失败)。在Hadoop2.x版本可以存在两个NameNode，解决了单点故障的问题。

![img](https://bkimg.cdn.bcebos.com/pic/8326cffc1e178a8205c409d5f503738da877e8cf?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1)

存储在HDFS中的文件被分成块，然后将这些块复制到多个计算机中(DataNode)。这与传统的RAID架构大不相同。块的大小(1.x默认为64MB，2.x默认为128MB)和复制的块数量在创建文件时由客户机决定。NameNode可以控制所有文件操作，HDFS内部的所有通信都是基于标准的TCP/IP协议

### 3.2 NameNode

NameNode是一个通常在HDFS实例中的单独机器上运行的软件。它负责管理文件系统名称空间和控制外部客户机的访问。NameNode决定是否将文件映射到DataNode上的复制块上。对于最常见的三个复制块，第一个复制块存储在同一机架的不同节点上，最后一个复制块存储在不同机架的某个节点上

实际的I/O事务并没有经过NameNode，只有表示DataNode和块的文件映射的元数据经过NameNode。当外部客户机发送请求要求创建文件时，NameNode会以块标识和该块的第一个副本的DataNode IP地址作为响应。

NameNode在一个成为FsImage的文件中存储所有关于文件系统名称空间的信息。这个文件和一个包含所有事务的记录文件将存储在NameNode的本地文件系统上。FsImage和EditLog文件也需要复制副本，以防文件损坏或者NameNode系统丢失

### 3.3 DataNode

DataNode也是一个通常在HDFS实例中单独机器上运行的软件。Hadoop集群包含一个NameNode和大量的DataNode。DataNode通常以机架的形式组织，机架通过一个交换机将所有系统连接起来。

Hadoop的一个假设是：机架内部节点之间的传输速度快于机架间节点的传输速度

DataNode响应来自HDFS客户机的读写请求。他们还响应来自NameNode的创建、删除和复制块的命令。NameNode依赖来自每个DataNode的定期心跳消息。 每条消息都包含一个块报告，NameNode可以依据这个报告验证块映射和其他文件系统元数据。如果DataNode不能发送心跳消息，NameNode将采取修复措施，重新复制在该节点上丢失的块。

### 3.4 文件操作

HDFS并不是一个万能的文件系统。它的主要目的是支持以流的形式访问写入的大型文件。

如果客户机想要将文件写道HDFS上，首先需要将该文件缓存到本地的临时存储。如果缓存的数据大于所需的HDFS块大小，创建文件的请求将发送给NameNode。NameNode将以DataNode标识和目标块响应客户机。

同时，NameNode通知将要保存文件块副本的DataNode.当客户机开始将临时文件发送给第一个DataNode时，将立即通过管道的方式将块内容转发给副本DataNode。客户机也负责创建保存在相同HDFS名称空间中的校验和checksum文件。

### 4 jargon

**Name Node**: HDFS consists of only one Name Node that is called the Master Node. The master node can track files, manage the file system and has the metadata of all of the stored data within it. In particular, the name node contains the details of the number of blocks, locations of the data node that the data is stored in, where the replications are stored, and other details. The name node has direct contact with the client.

**Data Node**: A Data Node stores data in it as blocks. This is also known as the slave node and it stores the actual data into HDFS which is responsible for the client to read and write. These are slave daemons. Every Data node sends a Heartbeat message to the Name node every 3 seconds and conveys that it is alive. In this way when Name Node does not receive a heartbeat from a data node for 2 minutes, it will take that data node as dead and starts the process of block replications on some other Data node.

**Secondary Name Node**: This is only to take care of the checkpoints of the file system metadata which is in the Name Node. This is also known as the checkpoint Node. It is helper Node for the Name Node.

**Job Tracker**: Job Tracker receives the requests for Map Reduce execution from the client. Job tracker talks to the name node to know about the location of the data that will be used in processing. The name node, responds with the metadata of the required processing data.

**Task Tracker**: It is the Slave Node for the Job Tracker and it will take the task from the Job Tracker. And also it receives code from the Job Tracker. Task Tracker will take the code and apply on the file. The process of applying that code on the file is known as Mapper.