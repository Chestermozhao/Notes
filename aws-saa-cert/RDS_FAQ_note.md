# RDS FAQ note
## Brief Description
### What is RDS?
- 在雲端設定操作和擴展關聯式資料庫
- support MySQL、MariaDB、Oracle、SQL Server and PostgreSQL
- auto backup your data if you want
- scaling with no effort
- payment on demand

### RDS versus database AMI
- Each engine varies greatly from engine to engine, see the [documentation](https://aws.amazon.com/tw/products/databases/)

### Hybrid or on-premise using RDS?
- you could using AWS outposts or VMware to execute RDS instance

## RDS Instance
- Whats Instance
    - 雲端中的資料庫環境，包含您指定的運算和儲存資源
- How many database instances can Amazon RDS execute?
    - most 40 instances by default
        - most 10 instances support authed Oracle or SQL server
        - RDS for SQL Server most executing 100 databases for single instance
        ![database limitation](https://i.imgur.com/DNX4L7g.png)

- How do we import data to RDS?
    - import method provided by the database engine
    - AWS Database Migration Service
- Is my database instance available during maintenance events?
    - If a maintenance event is scheduled for a given week, it will be initiated during the maintenance window you identify
    - Maintenance events that require Amazon RDS to take your DB instance offline are scale compute operations
    - If you do not specify a preferred weekly maintenance window when creating your DB instance, a 30 minute default value is assigned
    - Running your DB instance as a Multi-AZ deployment can further reduce the impact of a maintenance event
- What should I do if my queries seem to be running slowly?
    - enable Enhanced Monitoring, which provides access to over 50 CPU, memory, file system, and disk I/O metrics
    - High levels of CPU utilization can reduce query performance
        - scaling your DB instance class
    - MySQL and mariaDB support slow query logs
        - You could set the "slow_query_log" DB Parameter and query the mysql.slow_log table to review the slow-running SQL queries
    - OracleDB
        - Oracle trace file data to identify slow queries
    - SQL Server
        - use the client side SQL Server traces to identify slow queries

## DB engine versions
- Different engines have different versions of support
- New version provided within five months of releasing

### When you create DB instance, you can identify your DB version
- It is important to note that not all versions of the database engine are available in every AWS region.

### How to upgrade my DB version?
- you could using AWS Modify DB Instance API, you could assign upgrade immediately or upgrade while next mainteinance window
- If we find that the new version contains major bug fixes compared to the previously released
    - an automatic Upgrade of the individual schedule will be performed for the database set to `Yes` by `Auto Minor Version Upgrade`. These upgrades will be scheduled to be performed during the next maintenance window specified by the customer.
    - if you dont need auto upgrade, you can assign `Auto Minor Version Upgrade` to `No`
    - Oracle and SQL server won't auto upgrade even though you assign the `Auto Minor Version Upgrade` to `Yes`
### Can I test my DB instance with a new version before upgrading?
- Yes
- Steps
    - Create a database snapshot of an existing database instance
    - restore from the database snapshot to create a new database instance, and then initiate version upgrades for the new database instance
    - You can then safely test on the upgraded database instance copy and decide whether to upgrade the original database instance.

### Does Amazon RDS provide guidelines for deprecating database engine versions that are currently supported?
- support major version releases for at least 3 years after they are initially supported by Amazon RDS
    - MySQL 5.6, PostgreSQL 9.6
- support minor versions for at least 1 year after they are initially supported by Amazon RDS
    - MySQL 5.6.37, PostgreSQL 9.6.1

### What happens when an RDS DB engine version is deprecated?
- minor version deprecated
    - provide a three (3) month period after the announcement before beginning automatic upgrades
    - automatic upgrade to the latest supported minor version during their scheduled maintenance windows
- major version deprecated
    - provide a minimum six (6) month period after the announcement of a deprecation for you to initiate an upgrade to a supported major version
- DB instance restored from a DB snapshot created with the unsupported version will automatically and immediately be upgraded to a currently supported version

## Billing
- pay only for what you use, and there are no minimum or setup fees
- 未滿一小時的資料庫執行個體小時數按一小時計費
- 每月的佈建 IOPS – 佈建 IOPS 費率，不論 IOPS 的使用量如何
- 備份儲存 – 備份儲存是與自動資料庫備份和所有客戶啟動資料庫快照相關的儲存。延長備份保留期或拍攝額外資料庫快照會增加資料庫所消耗的備份儲存
- 傳入和傳出資料庫執行個體的網際網路資料傳輸

### When does billing of my Amazon RDS DB instances begin and end?
- instance terminated
    - broken or removed

### How will I be billed for a stopped DB instance?
- you are charged for
    - provisioned storage (including Provisioned IOPS) and backup storage (including manual snapshots and automated backups within your specified retention window)
- not for DB instance hours

### Why does my additional backup storage cost more than allocated DB instance storage?
- storage provisioned to your DB instance for your **primary data** is located within a **single Availability Zone**
- **backup data** (including transactions logs) is geo-redundantly replicated **across multiple Availability Zones** to provide even greater levels of **data durability**

### How will I be billed for Multi-AZ DB instance deployments
- Multi-AZ DB instance hours – Based on the class (e.g. db.t2.micro, db.m4.large) of the DB instance consumed
- **Provisioned storage** (for Multi-AZ DB instance) – If you **convert your deployment between standard and Multi-AZ** within a given hour, you will be **charged the higher of the applicable storage rates for that hour**.
- I/O requests per month – Total number of storage I/O requests:
    - **Write I/O usage** associated with database updates **will double** as Amazon RDS synchronously replicates your data to the standby DB instance
    - **Read I/O** usage will **remain the same**
- **Backup Storage** – Your backup storage usage will **not change** whether your DB instance is a standard or Multi-AZ deployment
- **Data transfer** – You are **not charged** for the data transfer incurred in replicating data **between your primary and standby**. Internet data transfer in and out of your DB instance is **charged the same as with a standard deployment**.

## Free Tier
- supported engines
    - MySQL
    - MariaDB
    - PostgreSQL
    - licensed
        - Oracle
            - Bring-Your-Own-License (BYOL)" licensing model
        - SQL Server Express Edition

## Reserved Instances
### What is a reserved instance (RI)?
- the option to reserve a DB instance for a one or three year term and in turn receive a significant discount
    - 承諾使用，獲取折扣的方案選擇
    - There are three RI payment options
        - No Upfront
        - Partial Upfront
        - All Upfront
-  用了RI，如果真的有用，那每小時費率會比按需付費低

### Do reserved instances include a capacity reservation
- RI are purchased for a **Region** rather than for a specific **Availability Zone**
    - not capacity reservations
    - discount will apply to matching usage in any Availability Zone within that Region
- RI承諾只在Region層次，意思就是無法承諾給你某個AZ保留多少容量，如果該AZ沒容量了，你可以在相同區域內創建instance，然後依然給你折扣

### How many reserved instances can I purchase
- **40**
- more than 40 DB instances, please complete the **Amazon RDS DB Instance request form**.

### If I sign up for a reserved instance, when does the term begin? What happens to my DB instance when the term ends?
- once your request is received while the payment authorization is processed.
- When your reservation term **expires**, your reserved instance will revert to the appropriate **On-Demand hourly** usage rate for your DB instance class and Region.

### If I scale my DB instance class up or down, what happens to my reservation?
- you **purchased a db.m4.2xlarge** MySQL reservation. If you decide to **scale up** the running DB instance to a **db.m4.4xlarge**, the discounted rate of this **RI will cover 1/2 of the usage of the larger DB instance**.
    - 部分DB engine支持彈性擴容，那當你選擇不同instance，那你的RI會涵蓋部分擴容的內容
- If you are **running a DB engine** or license model that is **not** eligible for **size-flexibility** (Microsoft SQL Server or Oracle "License Included")
    - only be applied to a DB instance with the same attributes for the duration of the term
    - 意思就是如果你選了不支持彈性擴容的RDS reservation instance，那不好意思，on-demand payment

### Can I move a reserved instance from one Region or Availability Zone to another?
- RI is associated with Region
- so you could move with different AZ within specific region
- however, you couldnt move to other regions

### RI available for Multi-AZ deployments?
- Yes
- if you are using a DB engine and license model that supports reserved instance size-flexibility, a Multi-AZ reserved instance will cover usage for two Single-AZ DB instances

### Are reserved instances available for read replicas??
- be applied to a read replica, provided the **DB instance class** and **Region** are the same

### Can I cancel a reservation?
- No
- You will continue to pay for every hour during your Reserved DB instance term regardless of your usage

## Hardware and Scaling
### Which instance class tyep is suitable to me?
- assess your application’s 
    - compute
    - memory
    - storage

### Scaling up your instance
- When you modify your DB Instance class or allocated storage
    - changes will be applied during your specified maintenance window
    - use the **“apply-immediately”** flag to apply your scaling requests immediately
    - Bear in mind that **any other pending system changes** will **be applied** as well
- **Some older RDS for SQL Server instances** may **not be eligible for scaled storage**

### What is the hardware configuration for Amazon RDS storage?
- RDS uses **EBS** volumes for **database and log storage**

### Will my DB instance remain available during scaling?
- No

### How can I scale my DB instance beyond the largest DB instance class and maximum storage capacity?
- you can implement **partitioning**, thereby spreading your **data across multiple DB instances**

### What is Amazon RDS General Purpose (SSD) storage?
- **3 IOPS/GB** and ability to burst up to **3,000 IOPS**
- suitable to most of applications

### Amazon RDS Provisioned IOPS (SSD) storage?
- designed to deliver fast, predictable, and consistent I/O performance
- optimized for **I/O-intensive**, **transactional (OLTP) database workloads**

### What is Amazon RDS Magnetic storage?
- **small** database **workloads** where data is accessed **less frequently**
- Magnetic storage is **not** recommended **for production** database instances

### How do I choose among the Amazon RDS storage types?
- **High-performance OLTP workloads**: Amazon RDS Provisioned IOPS (SSD) Storage
- Database workloads with **moderate I/O** requirements: Amazon RDS General Purpose (SSD) Storage

## Automatic Backups and Database Snapshots
### What is the difference between automated backups and DB Snapshots?
- automated backup
    - point-in-time recovery
    - automatically performs a full daily snapshot of your data
    - backup **retention period**, which by default is **7 days** but can be set to **up to 35 days**
    - restore and specify any **second** during your retention period
    - use the **DescribeDBInstances API** to return the latest restorable time for you DB instance, which is typically within the **last five minutes**
- DB Snapshots
    - user-initiated
    - restore to that specific state at any time
    - created with **CreateDBSnapshot API**, or create-db-snapshot command and are **kept until you explicitly delete them**.
- When you perform a restore operation to a point in time or from a DB Snapshot
    - a **new DB Instance** is created with a new endpoint (the **old DB Instance can be deleted if so desired**)
    - enable you to **create multiple DB Instances from a specific DB Snapshot or point in time**

### Do I need to enable backups for my DB Instance or is it done automatically?
- By default, Amazon RDS enables **automated backups of your DB Instance with a 7 day retention period**
- **disable** automated backups
    - change the **RetentionPeriod to 0**

### What is a backup window and why do I need it? Is my database available during the backup window?
- **user-defined** period of time during which your **DB Instance is backed up**
- During the backup window, **storage I/O** may be **briefly suspended** while the backup process initializes
- **no I/O suspension** for **Multi-AZ DB deployments**, since the **backup is taken from the standby**

### Where are my automated backups and DB snapshots stored?
- store at **S3**

### Why do I have more automated DB snapshots than the number of days in the retention period for my DB instance?
- 自動資料庫快照的數量比保存期天數多 1 或 2 個，屬於正常現象

### What happens to my backups and DB snapshots if I delete my DB instance?
- When you delete a DB instance, you can create a final DB snapshot upon deletion
- **Automated backups are deleted** when the DB instance is deleted. **Only manually created DB Snapshots are retained** after the DB Instance is deleted.

## Security
### How is using Amazon RDS inside a VPC different from using it on the EC2-Classic platform (non-VPC)?
- 在VPC跟不在VPC裡面創建RDS有差嗎？
- If your AWS account was created before 2013-12-04, you may be able to run Amazon RDS in an Amazon Elastic Compute Cloud (EC2)-Classic environment.
    - 在2013-12-04以前可以在非VPC裡面創建RDS

### What is a DB Subnet Group and why do I need one?
- 很大段ＸＤ，但我的理解就是，Subnet group就是很多subnet，RDS如果創建在VPC內就要指定subnet，透過subnet就可以綁定VPC跟RDS的關聯(之前提到過的ENI介面，這樣就可以高速傳輸啦)
- DB Subnet Group is a collection of subnets that you may want to designate for your RDS DB Instances in a VPC
- Amazon RDS creates and associates an Elastic Network Interface to your DB Instance with that IP address
- recommend you use the DNS Name to connect to your DB Instance as the underlying IP address can change
- For Multi-AZ deployments, defining a subnet for all Availability Zones in a Region will allow Amazon RDS to create a new standby in another Availability Zone should the need arise. You need to do this even for Single-AZ deployments

### How do I connect to an RDS DB Instance in VPC?
- VPN
- bastion hosts that you can launch in your public subnet
- Amazon RDS's Publicly Accessible option

### Can I move my existing DB instances outside VPC into my VPC?
- Yes

### Can I move my existing DB instances from inside VPC to outside VPC?
- No
- since security, it is not supported to restored to outside VPC, besides, “Restore to Point in Time” is not supported

### What precautions should I take to ensure that my DB Instances in VPC are accessible by my application?
- modifying routing tables and networking ACLs in your VPC to ensure that your DB instance is reachable from your client instances in the VPC

### Can I change the DB Subnet Group of my DB Instance?
- Yes
- but remove subnet will make your app broken

### What is an Amazon RDS master user account and how is it different from an AWS account?
- 前者是管理DB(例如MYSQL的帳戶)
- 後主事AWS console的帳號

### Can programs running on servers in my own data center access Amazon RDS databases?
- configuring Security Groups

### encrypt connections between my application and my DB Instance using SSL/TLS
- Yes
- be aware that SSL/TLS encryption is a compute-intensive operation and will increase the latency of your database connection

### Can I encrypt data at rest on my Amazon RDS databases?
- **encryption** at rest for all database engines, using keys you manage using **AWS Key Management Service (KMS)**.

### How do I control the actions that my systems and users can take on specific RDS resources?
- AWS IAM policies that you apply to your users and groups

### Can I get a history of all RDS API calls made on my account?
- AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you

### Can I use Amazon RDS with applications that require HIPAA compliance?
- Yes, all RDS database engines are HIPAA-eligible

## Database Configuration
### What are DB Parameter groups?
- 可套用到一或多個資料庫執行個體
- 資料庫執行個體以您自訂的引擎設定值執行，只需建立一個新資料庫參數群組，再修改所需的參數，然後修改資料庫執行個體以使用新資料庫參數群組

### How can I monitor the configuration of my Amazon RDS resources?
- use AWS Config to continuously record configurations changes to Amazon RDS
    - DB Instances
    - DB Subnet Groups
    - DB Snapshots
    - DB Security Groups
    - Event Subscriptions
- notification of changes through Amazon Simple Notification Service (SNS)

## Multi-AZ Deployments
### What does it mean to run a DB instance as a Multi-AZ deployment?
- 自動在不同的可用區域佈建和維護一份同步「備用」複本
- 個體的更新將同步複製到可用區域的備用副本，以保持同步並保護最新的資料庫更新，防止資料庫執行個體出現故障
- 資料庫執行個體故障或可用區域故障情況下，Amazon RDS 將自動容錯移轉到備用副本

### What do “primary” and “standby” mean in the context of a Multi-AZ deployment?
- 「主」副本為資料庫寫入和讀取操作提供服務
- 在容錯移轉情況下會「提升」備用副本
    - 容錯移轉後，備用副本成為主副本，並接受資料庫操作

### What are the benefits of a Multi-AZ deployment?
- enhanced database **durability** and **availability**

### Are there any performance implications of running my DB instance as a Multi-AZ deployment?
- elevated latencies relative to a standard DB instance deployment in a single Availability Zone
    - synchronous data replication need some time to downgrade performance

### When running my DB instance as a Multi-AZ deployment, can I use the standby for read or write operations?
- No, a Multi-AZ standby cannot serve read requests.

### What happens when I convert my RDS instance from Single-AZ to Multi-AZ?
- A snapshot of your primary instance is taken
- A new standby instance is created in a different Availability Zone, from the snapshot
- Synchronous replication is configured between primary and standby instances
- as such, the latency increased

### What events would cause Amazon RDS to initiate a failover to the standby replica?
- Loss of availability in primary Availability Zone
- Loss of network connectivity to primary
- Compute unit failure on primary
- Storage failure on primary
- Note that Amazon RDS Multi-AZ deployments **do not fail over automatically**
    - in response to database operations such as long running queries, deadlocks or database corruption errors

### Will I be alerted when automatic failover occurs?
- Yes

### What happens during Multi-AZ failover and how long does it take?
- Amazon RDS simply flips the canonical name record (CNAME) for your DB instance to point at the standby
- Failovers
    - as defined by the interval between the detection of the failure on the primary and the resumption of transactions on the standby, typically complete within one to two minutes
- AWS also recommends the **use of Provisioned IOPS with Multi-AZ instances**, for fast, predictable, and consistent throughput performance.

### Can I initiate a “forced failover” for my Multi-AZ DB instance deployment?
- Amazon RDS provides an option to initiate a failover when rebooting your instance

### Will my standby be in the same Region as my primary?
- Yes
- different Availability Zone of the same Region as your DB instance primary

### Can I see which Availability Zone my primary is currently located in?
- Yes
- AWS Console or DescribeDBInstances API

### How do DB Snapshots and automated backups work with my Multi-AZ deployment?
- Multi-AZ deployment
    - automated backups and DB Snapshots are simply taken from the standby to avoid I/O suspension on the primary
    - may experience increased I/O latency (typically lasting a few minutes) during backups for both Single-AZ and Multi-AZ deployments

## Read Replicas
### What does it mean to run a DB Instance as a read replica?
- You can create multiple read replicas for a given source DB Instance and distribute your application’s read traffic amongst them

### hen would I want to consider using an Amazon RDS read replica?
- Scaling beyond the compute or I/O capacity of a single DB instance for read-heavy database workloads. This excess read traffic can be directed to one or more read replicas.
- Serving read traffic while the source DB instance is unavailable. If your source DB Instance cannot take I/O requests (e.g. due to I/O suspension for backups or scheduled maintenance), you can direct read traffic to your read replica(s). For this use case, keep in mind that the data on the read replica may be “stale” since the source DB Instance is unavailable.
- Business reporting or data warehousing scenarios; you may want business reporting queries to run against a read replica, rather than your primary, production DB Instance.
- You may use a read replica for disaster recovery of the source DB instance, either in the same AWS Region or in another Region.

### Do I need to enable automatic backups on my DB instance before I can create read replicas?
- Yes
- 備份必須維持啟用狀態，僅供讀取複本才能運作

### Which versions of database engines support Amazon RDS read replicas?
- Aurora
    - All DB clusters
- MySQL
    - All
    - 只有執行 MySQL 5.6 和更新版本的 Amazon RDS 僅供讀取複本支援複本上的自動備份，5.5 不支援
- PostgreSQL
    - `>= 9.3.5`
- MariaDB
    - All
- Oracle
    - Oracle Database Enterprise Edition 使用自有授權模式，且已授權 Active Data Guard Option 的 Oracle 12.1.0.2.v12 版本及所有 12.2 版本。
- SQL Server
    - 2016 和 2017 的 AlwaysOn 可用性群組基礎複寫技術時，異地同步備份中的 Enterprise Edition 支援僅供讀取複本

### 如何為指定的資料庫執行個體部署僅供讀取複本
- 當您啟動僅供讀取複本的建立時，Amazon RDS 將對來源資料庫執行個體拍攝快照，並開始複寫。因此，在拍攝快照時，您的來源資料庫執行個體上的 I/O 可能會暫停一下
- Amazon RDS 目前正在進行優化 (即將發行)，因此如果您在 30 分鐘內建立多個僅供讀取複本，所有副本都將使用相同的來源快照以盡量減少 I/O 影響 (每個僅供讀取複本將在建立後開始「趕上」複寫)

### 連接到我的僅供讀取複本
- 去AWS console上面看他的endpoint

### 指定的來源資料庫執行個體建立幾個僅供讀取複本？
- MySQL、MariaDB、PostgreSQL、Oracle 和 SQL Server 皆可允許您為指定的來源資料庫執行個體建立最多 5 個僅供讀取複本

### 與來源資料庫執行個體不同的 AWS 區域中建立僅供讀取複本
- Yes
- 資料寫入來源資料庫執行個體以及在僅供讀取複本中可使用資料之間的時間長短，取決於兩個區域之間的網路延遲

### Amazon RDS 僅供讀取複本是否支援同步複寫?
- No
- Amazon RDS for MySQL、MariaDB、PostgreSQL、Oracle 和 SQL Server 的僅供讀取複本實作均使用這些引擎的原生異步複寫

### 是否可以使用僅供讀取複本來增強資料庫寫入可用性或保護來源資料庫執行個體中的資料，以防出現故障？
- 異地同步備份部署會採用同步複寫，這表示主副本和備用副本上的所有資料庫寫入都同時發生。這樣可保護最新的資料庫更新，因為在需要容錯移轉時，必須能夠使用備用副本上的資料

### 是否可利用異地同步備份資料庫執行個體部署建立僅供讀取複本做為其來源？
- Yes
- 異地同步備份資料庫執行個體可提供您增強的寫入可用性和資料持久性，而關聯的僅供讀取複本可改善讀取流量擴展性

### 是否可以將 Amazon RDS 僅供讀取複本本身設定為異地同步備份？
- Yes

### 是否可以為另一個僅供讀取複本建立僅供讀取複本？
- available
    - Amazon Aurora, Amazon RDS for MySQL、MariaDB
- not available
    - Amazon RDS for PostgreSQL、Oracle and SQL Server

### 我的僅供讀取複本是否只能接受資料庫讀取操作？
- 大多數是的
- 部分案例中可以接受DDL SQL statement
    - Amazon RDS for MySQL

### 是否可以將僅供讀取複本提升成「獨立」資料庫執行個體？
- Yes

### 僅供讀取複本是否會與其來源資料庫執行個體一起保持在最新狀態？
- 未必，原因可能是
    - 來源資料庫執行個體的寫入 I/O 磁碟區超過變更可套用到僅供讀取複本的速率 (如果僅供讀取複本的運算容量低於來源資料庫執行個體，特別可能發生此問題)
    - 來源資料庫執行個體的複雜或長時間執行的交易阻礙僅供讀取複本的複寫
    - 來源資料庫執行個體和僅供讀取複本之間有網路分割或延遲

### 僅供讀取複本的費用為何？ 如何計算帳單週期？
- 和標準資料庫執行個體一樣，僅供讀取複本的每「資料庫執行個體小時」費率取決於僅供讀取複本的資料庫執行個體類別 – 有關最新的定價資訊

## Enhanced Monitoring
### 增強型監控支援哪些引擎？
- All of engines

### 增強型監控支援哪些執行個體類型？
- t1.micro 和 m1.small 除外

### 我的 RDS 帳戶抽樣指標的所有執行個體是否會是同樣的間隔
- No
- 隨時修改任何執行個體的間隔

### RDS 主控台上可以回溯到多久之前的歷史指標
- 所有指標的效能值最多可以往回查 1 小時，間隔最高為 1 秒

### 何時應該使用 CloudWatch 而不是 RDS 主控台儀表板？
- RDS 主控台儀表板上沒有提供的歷史資料，則應該使用 CloudWatch
- CloudWatch 支援最高 1 分鐘的間隔

### 如何刪除歷史資料
- CloudWatch Logs 中為增強型監控設定的預設保留期是 30 天
- 您可以控制它的保留期

### 增強型監控對我每月的費用有何影響
- 指標擷取到 CloudWatch Logs 中，所以只要超過 CloudWatch Logs 免費方案，就會按照 CloudWatch Logs 資料傳輸和儲存費率來計費
![](https://i.imgur.com/SgnZk09.png)

## Amazon RDS Proxy
### 為什麼要使用 Amazon RDS Proxy？
- 透過容納和共享資料庫連接來提高可擴展性
- 透過將資料庫容錯轉移時間減少多達 66％，並在容錯轉移期間保留應用程式連接，來提高可用性
- 透過可選擇性地對資料庫強制執行 AWS IAM 身份驗證，並在 AWS Secrets Manager 中安全地儲存登入資料來提高安全性

### 哪些使用案例？
- 工作負載不可預測的應用程式
- 經常開啟和關閉資料庫連接的應用程式
- 使連接保持開啟但處於空閒狀態的應用程式
- 需要在出現暫時性故障時獲得可用性的應用程式
- 改進的安全性和集中式登入資料管理

### 何時應該直接連接到資料庫而不使用 Amazon RDS Proxy？
- 如果您的應用程式不能忍受 5 毫秒的延遲，或者不需要連接管理和 RDS Proxy 支援的其他功能

### 無伺服器應用程式可從 Amazon RDS Proxy 獲得什麼好處？
- RDS Proxy 透過容納和重用資料庫連接，來使無伺服器應用程式高效地擴展
- 使用 RDS Proxy 時，您不再需要在 Lambda 程式碼中處理資料庫登入資料
- 您無需管理任何新的基礎設施或程式碼

### Amazon RDS Proxy 支援哪些資料庫引擎？
- Aurora
- part of MySQL
- coming soon for other db class types
