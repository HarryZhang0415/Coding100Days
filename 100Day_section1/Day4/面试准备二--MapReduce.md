# 广发基金数据研发岗面试准备

## 二、MapReduce

### 1. 定义：

MapReduce是一种编程模型，用于大规模数据集的并行运算。它是面向大数据并行处理的计算模型、框架和平台。Map--映射， Reduce--归约，是它们的主要思想。主要隐含了三层含义：

* MapReduce是基于集群的高性能并行计算平台。它允许使用市场上普通的商用服务器构成一个包含数十，数百甚至数千个节点的分布和并行计算集群
* MapReduce是一个并行计算与运行软件框架。它提供了一个庞大但设计精良的并行计算软件框架，能够自动完成计算任务的并行化处理，自动化分计算数据和计算任务，在集群节点上自动分配和执行任务以及收集计算结果，将数据分布存数据通信、容错处理等并行计算涉及到的很多底层细节交由系统负责处理
* MapReduce是一个并行程序设计模型与方法。它借助于函数式程序设计语言的设计思想，提供了一种简便的并行程序设计方法，用Map和Reduce两个函数编程实现基本的并行计算任务，提供了抽象的操作和并行编程接口，以简单方便地完成大规模数据的编程和计算处理

## 2. Operations

A MapReduce framework is usually composed of three operations:

* Map: Each worker node applies the map function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of the redundant input data is processed.
* Shuffle: Worker nodes redistribute data based on the output keys(produced by the map function), such that all data belonging to one key is located on the same worker node.
* Reduce: Worker nodes now process each group of output data, per key, in parallel.

### 5-step parallel and distributed computation:

		1. **Prepare the Map() input** - The "MapReduce system" designates Map processors , assign the input key K1 that each processor would work on, and provides that processor with all the input data associated with that key.
  		2. **Run the user-provided Map() code** - Map() is run exactly once for each K1 key, generating output organized by key K2
    		3. **"shuffle" the Map output to the Reduce processors** - the MapReduce system designates Reduce processors, assign the K2 key each processor should work on, and provides that processor with all the Map-generated data associated with that key
      		4. **Run the user-provided Reduce() code**
        		5. **Produce the final result**

## 3. Dataflow

Software framework architecture adheres to open-close principle where code is effectively divided into unmodifiable frozen spots and extensible hot spots. The frozen spot of the MapReduce framework is a large distributed sort. The hot spots, which the application defines, are:

* an input reader
* a Map function 
* a partition function
* a compare function
* a Reduce function
* an output writer

Shuffle Step -- > partition + comparison function

### Input reader

The input reader divides the input into appropriate size 'splits'(in practice, typically, 64 MB to 128 MB) and the framework assigns one split to each Map function. The input reader reads data from stable storage (typically, a distributed file system) and generates key/value pairs

### Map function

The Map function takes a series of key/value pairs, processes each, and generates zero or more output key/value pairs. The input and output types of the map can be different from each other.

### Partition function

Each Map function output is allocated to a particular reducer by the applications' partition function for sharding purposes. The partition function is given the key and the number if reduces and return the index of the desired reducer.

A typical default is to hash the key and use the hash value modulo the number of reducers. It is important to pick a partition function that gives an approximately uniform distribution of data per shard for load-balancing purposes. Otherwise, the MapReduce operation can be held up waiting for slow reducers to finish.

Between the map and reduce stages, the data are shuffled in order to move the data from the map node that produced them to the shard in which they will be reduced. The shuffle can sometimes take longer than the computation time depending on network bandwidth.

### Comparison function

The input for each Reduce is pulled from the machine where the Map ran and sorted using the application's comparison function

### Reduce function

The framework calls the application's Reduce function once for each unique key in the sorted order. The Reduce can iterate through the values that are associated with that key and produce zero or more outputs

​		