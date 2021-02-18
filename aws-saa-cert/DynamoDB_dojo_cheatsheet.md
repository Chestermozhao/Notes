# DynamoDB cheat sheet note
## Brief Description
- scale up and down throughtput with no downtime
- provide on-demand backup service
    - you could restore point-in-time for last 35 days
- support multi-master write and could cross-region
- limit with firewall, could constraint outbound traffic to specific VPC or Direct connect

## Core component
- Tables
    - initial with 256 limitation
- Items
    - collection of attributes
    - primary key
        - unique key
    - secondary index
        - provide more query flexibility
- Attributes
    - key value pair
    - support most 32 deep nested structure
- Primary key
    - unique, so there are no two items exist same primary key
    - Partition Key
        - composed with **single** attribute
    - Partition Key and sort Key
        - composed with **two** attributes
    - DynamoDB use Partition Key as hash function input
- Secondary Indexes
    - you could create >= 0 secondary indexes in table
    - global secondary index
        - same partition key and sort key
        - most 20 for single table
    - local secondary index
        - same partition key and diff sort key
        - most 5 for single table
## DynamoDB stream
- endpoint is `stream.dynamodb..amazonaws.com`
- each Event is represented as stream record
    - new item added in table
    - item updated
    - item deleted
- lifetime of stream record is 24 hours
- could trigger lambda to do next process
- 搭配Kinesis跟Lambda可以分析操作
- ![](https://i.imgur.com/2fJvRpS.png)

## Data type for attributes
- scalar type
    - simple type
    - primary key must be scalar type
- document type
    - nested type
    - json
- set type
    - set of scalar type

### Others
- consistency
    - strong: not promise for cross region, and it is not stable if network not well
    - eventually
- capacity unit
    - read
        - one strong consistency per second
        - two eventually consistency per second
    - write
- you could set throttling to avoid exceed specified capacity unit exceed

## DynamoDB autoscaling
- enabled by default
- 可以根據讀寫運算單元調整你的額度
- 如果有很多的global secondary index可以全部關聯下

## Tagging
- 快速定位你的資源
- 看帳單比較好看
- 每個資源最多50個tag

## Security
- using **KMS** to manage encrypting keys
- encrypting rest data only available when you create table
- AES-256
- The following is encrypted
    - Table
    - global secondary indexes
    - local secondary indexes
- Auth and access
    - access DynamoDB you need valid credential
    - if you wanna operate db, you need permission
    - Type of identity
        - AWS root user
        - IAM role
        - IAM user

## Items
- expressions
    - project expression
        - if you just need few attributes
    - expression attribute name
    - expression attribute value
    - updated expression
        - specify update data clearly
    - condition expression
        - match it or not

## Queries
- single query most process 1MB data
- filter expression to filter unwant data
- support limit parameter
- **scannedcount** is the condition expression matched count
    - **before filter expression**
- **count** is the matched count **after filter expression**

## Transaction
- Dynamo DB support ACID operation
- support up to 25 items and 4MB transaction operation

## Backup and store
- cloudtrail would save the backup record
- do not guarantee consistency btw items
- include backup
    - database data
    - global secondary indexes
    - local secondary indexes
    - stream
    - provisionded read and write capacity unit
- while back, you can **not** do
    - pause backup
    - delete source data
    - diable backup a table if backup for the table is in progress
- Store
    - if data skew, need more time to restore

## DynamoDB Accelerator(DAX)
- full-managed, high avalibility, in-memory cached
- microsecond response time for eventually consistency data
- increase throuthput and cost saving
- **Not recommend** if you need **strong consistency**
- suitable to **read-intensive** not for **write-intensive**
- support **server-side encrypt** not **TLS**
- provisioned your cluster at least to 3 AZ to make your sevice more available
- horizontal scaling
    - add read replica
        - single DAX could set 10 read replica most
        - you could change your configuration in running node
- vertical scaling
    - select different node type
        - create new node

## Pricing
- using space of disk
    - first 25GB is free per month
- throttling
    - RCU and WCU
    - network transit fee
- while you evaluate CU, you have to specify most nearly KB
- additional charge for
    - DAX
    - backup
    - point-in-time recovery
    - stream
    - global tables
