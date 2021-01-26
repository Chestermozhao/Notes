# SAA certificate note
## AWS Certified Cloud Practitioner
### Introduce to AWS
- billing
    - 用多少付多少
- graphic region
    - seperated to multiple AZ(availablity zone)
        - HA的需求通常會deploy在不同AZ，那某個AZ崩潰還是可以讓服務不中斷
    - other secret regions for US government
    - CDN結點很多(cloud front)
        - 提供標準的攻擊防護(DDos and others)
- Aws management console
    - web-base user interface to AWS
    - require an aws account
    - monitor costs
    - aws console mobile app
- Aws SDK支持多語言
    - python, go, ruby...
- Aws cli(command line)
    - 版本區分蠻可怕的，語法會不同

### Intro to storage service
- cloud computin models
    - IaaS(Infrastructure as a Service)
        - basic buildong block for cloud IT
    - Paas(Platform as a Service)
        - ES, RDS, EMR
    - SaaS(Software as a Service)
        - product as a service, mostly refer to end-user application
- Serveless computing
    - Faas(Function as a service)
        - example: S3, Lambda, DynamoDB, SNS
    - provide service without thinking server
- Simple Sotrage Service(S3)
    - bucket
- Glacier
    - cheapest storage option to AWS
    - used for long-term archive data
    - 可讀性比S3插，如果要做歸檔，可以設定S3的歸檔時間，自動歸檔到Glacier
- Amazon elastic block store(EBS)
    - high avaliable and low latency block storage
    - specifically for attaching to server launched on ec2
- Amazon elastic file syetem(EFS)
    - network attached storage
    - specifically for attaching to server launched on ec2
    - 可以想像是NAS
- Aws storage gateway
    - 容許混合的儲存，可以接受混合低端跟雲端的解決方案
    - low latency透過緩存高頻訪問文件，將低頻訪問文件存到雲服務
- Snowball
    - portable, petabyte, scalable
    - 常用於數據遷移或大數據存儲

### Intro to Database Services
- Relational Database service(RDS)
    - MySQL, PGSQL, MariaDB
- DynamoDB:
    - noSQL engine
- Redshift
    - petabyte data storing
    - postgreSQL engine
- ElatiCache
    - in-memory data store
- Data migration Service(DMS)
    - could migrate differnet engine db
- Neptune
    - grapgh databse engine

### Intro to compute services
- Elastic compute cloud(Ec2)
    - auto-scaling: dynamically scaling
    - health check
    - high availablity
- Amazon Lightsail
    - easiest way to launch virtual service on aws cloud
    - 最簡易的部屬方式之一?
        - 感覺serveless更簡易ＸＤ
- Elastic Container Service(ECS)
    - container will run on ec2 instance
- Lambda
    - serveless service
    - Faas

### Intro to network services
- cloud front
    - global CDN service
    - over 100 edge location across the globe
    - provide protection for DDos
- Virtual Private Cloud(VPC)
    - let us provision isolated section on aws cloud
    - run application in virtual network
- Aws Direct connect
    - high speed dedicated network connection to Aws, provided to enterprise
        - 商業方案的特殊通道
- Elastic load balancing(ELB)
    - automatically distribute incoming traffic across multiple ec2 instance
    - could across multiple AZ
- Route53
    - highly availablity and scalable domain name system(DNS)
    - from domain name to backend service(ip)
- API gateway
    - fully managed service to create and deploy secure application programming interface or API
    - serveless service

### Intro to Management Services
- cloud watch
    - monitor service and call SNS to user
        - billing
- cloudformation
    - use text file to define your infrastructure and deploy resources on AWS cloud
    - 簡單來說就是可以透過設定文件幫你部署跟搭架Infra的服務
- Service catalog
    - allow enterprese to catalog resources that can be deployed on aws cloud
- System manager
    - provide unified user interface
    - 基本上共用的組件都可以在這個服務內找到
- CloudTrail
    - monitors and logs AWS account activity including actions taken through the AWS management console
- Aws Config
    - enable you access, edit, and evaluate your aws resources
        - auditing, security analysis, change management and control, trouble shooting
- OpsWorks
    - manage instance of Chef(?) and Puppet(?)
- Trusted Adivisor
    - online expert system, analysis aws accountand resources inside -> advise you how to achieve high security and best profermance

### Intro to Application services
- Step functions
    - 可以組合多個微服務的工作流
- Simple workflow service(SWF)
    - 類似step function, 但是新服務都推薦用step function，感覺是過去提供的一種解決方案
- Simple Notification Service(SNS)
    - fully managed pub/sub messageing service
        - 創建一個channel，要收推送的用戶subcribe
    - 支援推送移動端
- Simple queue Service(SQS)
    - fully managed message queue service
    - 可以擋在auto-scaling ec2前面 作為buffer
    - 同時透過cloud watch監聽SQS狀態，如果附載太重可以送SNS給自己(這時候可能是ec2一直起不來之類的)
- Amazon connect
    - 透過電話開啟服務
- Amazon pinpoint
    - 透過email開啟服務
- Simple Email Service(SES)
    - cloud-based bulk email sending service

### Intro to analytics
- Amazon Elastic MapReduce(EMR)
    - Aws提供的hadoop服務
    - integrets Spark, hbase, flink
    - 要分析的資料可以存儲在s3, DynamoDB(AWS提供的nosql引擎)
- Athena
    - 用標準的SQL語句分析資料
    - 資料源可以是s3
- Amazon Elasticsearch service
    - allow high-speed quering
- Kinesis
    - collect process and analyze real-time streaming data
- Quick sight
    - BI工具


### Intro to ML
- Deeplens
    - deep learning camera?
- Sage maker
    - flagship machine learning product
    - help us build and train ML models
    - deploy to AWS cloud as BE application
- Rekognition
    - provide dl based analysis of video and image
- Lex
    - build conversational chatbot
- Polly
    - natural sound text-to-speech(文字轉語音服務)
- Comprehend
    - 分析文字的關係或聚類
- Translate
    - 文本翻譯服務
- Transcribe(要再查下ＸＤ)
    - automatically speech recognition service

### Intro to security identity and 
- Aws artifact
    - online portal that provide us to access AWS security and compliance documentation
- Aws certificate manager
    - intergrate with route53 and cloudfront
- Aws cloud directory
    - 雲目錄
- Aws directory service
    - fully managed Microsoft Active Directory service in aws cloud
- Aws cloudHSM
    - dedicate hardware security module in aws cloud
- Amazon Cognito
    - provide sign in and sign up capability for your web and mobile app
    - could connect google/FB oauth process
- IAM(identity and Access management)
    - manage user access to your AWS service and resource in your account
- Aws Organizations
    - provide policy for multiple aws account
- Amazon inspector
    - automatically security access service
    - identify vulnerability or area of improvement in account
- Key management service(KMS)
    - create and control encrypted data
    - 也支持硬體module
- Aws Shield
    - provide protection to DDos attack
- Web application Firewall(WAF)
    - firewall in front of your application, provdie additional protection(SQL inhection)


### Create S3 bucket
- permission
    - using permission generator gen policies
        - and paste result to permission content
- properties
    - static website hosting
        - set https certificate
            - #certificate manager

### certificate manager
- provision certificate
    - request a certificate
        - add domain name
        - DNS validate
    - create record for route53


### create cloudfront distribution
- create distribution
    - origin domain name
    - alternative domain names
    - custom SSL certificate
        - choose certificate manager result
    - default root object


### routing with route53
- 設定route53指向剛剛的CDN


### What is IAM?
- user, user group, role
- organization
- A webservice that allow you to security control individual and group to access your AWS resource
- Features
    - shared access
    - granular permission
    - secure access EC2
    - grant permission for user outside of AWS
    - Payment Card Industry and Data Security Standard Compliance
    - Log auditing by CloudTrail
    - Eventually Consistency
    - Free to user
- including of name and credential
    - eg: name --> Bill
    - credential --> ARN:....
        - could associate to a user
            - console password
            - Access key
    - Never user root user
        - even you, just create a IAM administrator user
- password policy
    - min length
    - character types
    - change password by user
    - expiration
    - prevent user using previous pwd
    - force user contact administrator while expiring


### More about IAM
- Groups
    - collection of users
    - user assume permission of group
    - user could belong to multi group
    - group could contain user not nested
- Roles
    - define permission that could assume from user or resource
    - allow Ec2 instance to access other resources
    - grant access for another AWS user account to access your resources
    - temporarily assume a rule, identity deferation
        - AWS Cognito
        - Oauth
        - SSO
- Organisation
    - allow multiple AWS account used by an organisation to be part of OU(organisation unit)
    - service control policies allow the whitlist and blacklist with OU
    - blacklist priority higher than user group
    - Pros
        - centrally management permission
        - control access
        - automate creation and management with APIs
        - consolidate billing
- Amazon Resource Name(ARN)
    - format
        - arn:aws:iam::account:resource(note region missing, since IAM is global service)
- User based versus Resource based policies
    - IAM policy is follow user based
    - some resources followed resource based policy
        - s3: ACL
        - Glacier vault access policy
        - SNS topics
        - SQS queue
        - Key management
- Identity Federation
    - outside user get temporailiy access permission
    - Methods to creating federing users
        - Cognito
        - SAML
        - Oauth
        - SSO
        - AWS enterprise access
- AWS cloudtrail
    - aws console, sdk, cli all communicate aws service with APIs
    - AWS log calls from API
    - logs are stored in bucket for analysis(Athena, EMR)
    - SNS topic could alert security issues


### IAM best practice
- Lock root user keys
- create individual user
- user group to assign user permission
- grant least privilege
- use access level to review IAM permissiom
- configure strict pwd policy to your user
- enable multiple-factor auth for privileged user
- delegate by role
- use role for application that run on ec2
- rotate credential regularly
- remove unnecessary credential
- use policy condition for federation login
- monitor activity in your account bt CloudTrail


### Trusted advisor
- 好像是會給你infra security的建議跟優化費用建議
- for enterprise


### Elastic Compute Cloud(EC2)
- purchasing options
![purchase options](https://img.onl/jhWCKI)

- saving plans
![saving plan](https://img.onl/19H8s1)

- how to select type of instance purchasing policies
![purchasing tips](https://img.onl/rzFE0g)

- instance types
![instance types](https://img.onl/872zGg)

- t2/t3 bustable(CPU credit)
  - 每個小時有固定的credit
  - 24小時內可以累積
  - 只要不是0就可以burstable
  - 如果超出去每分鐘遞減1
  - 如果到0就代表你可能需要重開別的instance或者換instance type
![burstable CPU credit](https://img.onl/cIM6uZ)

- using ARM
![using ARM](https://img.onl/9kbxvF)

- EC2 fleet
  - [docs](https://aws.amazon.com/tw/about-aws/whats-new/2018/04/introducing-amazon-ec2-fleet/#:~:text=Amazon%20EC2%20Fleet%20%E6%98%AF%E4%B8%80,Amazon%20EC2%20%E5%AE%B9%E9%87%8F%E7%9A%84%E7%A8%8B%E5%BA%8F%E3%80%82&text=Amazon%20EC2%20Fleet%20%E7%8F%BE%E5%B7%B2%E9%96%8B%E6%94%BE%E6%89%80%E6%9C%89%E5%85%AC%E6%9C%89%E5%8D%80%E5%9F%9F%E4%B8%AD%E4%BD%BF%E7%94%A8%E3%80%82)
![EC2 fleet](https://img.onl/gObVRQ)

- Amazon machine image
![AMI](https://img.onl/Mr9OGO)

- EC2 states
![EC2 states](https://img.onl/7WWHZJ)

- EC2 instance lifecycle
![EC2 instance lifecycle](https://img.onl/kvCAxX)

- EC2 cluster networking
![EC2 cluster networking](https://img.onl/n6LQXI)

- EC2 storage options
  - [different instance type could choose different storage type](https://aws.amazon.com/tw/ec2/instance-types/)
![EC2 storage options](https://img.onl/Exw8cv)
![EC2 storage options2](https://img.onl/qWpMVC)

- EC2 connected from remote
![EC2 connected from remote](https://img.onl/kS2prr)

---
### S3 on hands
- Add policy
  - Principal for all access
  - Action for all
  - Add ARN(optional), set S3 ARN to this field
  - After choose completed, creating policy

### Database on AWS
- What is RDS?
  - Manage relation database service
  - PG, MySQL, MariaDB, Oracle, MS SQL, Aurora
  - Paas Service, handling provision, patching, backup, recovery, failure detection and repair
- Backup
  - RDS sanpshot
    - User initiate RDS
  - backup to S3
    - Deleted by default
    - Disable by setting backup retention period to 0
- Encryption RDS is optional
- cross multi-AZ
  - if you open this service, 他會幫你在兩個AZ啟動
- read replica
  - 如果流量大需要一個read only的RDS instance
  - not support for MS SQL and Oracle
  - canot put bahind AWS ELB
    - Use arora cluster
      - route53 routing HaProxy
- Aurora
  - MySQL and PGSQL compatibale
  - faster than MySQL 5 times, 3 times for PG SQL
  - cluster load balance by aurora service and instance with single reader endpoint
  - Scale
    - vertical: resize
    - horizon: 15 read replicas
  - Pay by second
  - sutible for infrequent, intermittent, unpredicable workload
- DynamoDB
  - NoSQL DB
  - consist of
    - Table: collection
    - Attribute: field
    - Items: document
    - Partition key and sort key: index
  - autoscaling base on demand
  - sutible for predict traffic, traffic consistent, capacity requirement can forecast and control costs
  - specify the number of R & W per second that you expected
- Neptune
  - graph DB
  - purpose build and store data relationship
  - use graph structure
    - node
    - edge
    - properties store data and those node
  - graph query language
    - Gremlin
    - SPARQL
- Amazon Redshift
  - big data(PB level)
  - base on PG engine
- ElasticCache
  - in memory data store service
  - low latency
  - Redis or Memcached engine
  - 可以搭配Dynamo DB做緩存設計
    - 因為Dynamo DB讀寫計價
- Amazon document DB
  - MongoDB compatible
  - lanched for cluster, up to 16 instances(1 primary and 15 replicas)
  - 99.99 avalibility
  - Replica for 6 copies across 3 AZ
  - continuously backup to S3 and provide up ro 35 days point-in-time recovery with no downtime and performance degeadation

### VPC(Virtual Private Cloud)
- create ec2 with default VPC
- internet connectivity
  - public IP
  - VPC has an internet gateway
  - route define in route table from subnet to internet gateway

### Cloudformation
- desing template
    - you could design your structure here
    - after design, you will get json or yaml config
- create stack
    - With cloudformation, you could design template with GUI platform and create dev-env with yaml file automatically
- update stack
    - if you update the json file, you could deploy with this

### CloudWatch
- metrix of(not avaliable for all regions)
    - Billing
    - BynamoDB
    - EC2, EBS
    - Elastic Beanstalk
    - Opworks
    - Kinesis Firehose
    - Full list in Developer Guide
- not only for raw data, support averge, max, min
- or you could get statistics with API/CLI
    - maximum number of data points can be required is 50850
    - maxmium number of data points returned from single request is 1440
    - if you need collect large data, you need get it with stream method
- view with console and create dashboard
- Alarms
    - Integrates with SNS
    - three state
        - OK
        - ALARM
        - INSUFFICIENT_DATA
    - exceed threshold for 3 periods, the alarm is invoked
- CloudWatch Logs
    - monitor and store your logs from EC2, CloudTrail, other resources
    - Real-time monitoring of log infomation
    - Log streams: sequence of log events from source
    - Log groups: streams the same retention, monitoringm and access control settings
    - Metrix filters: define how info is extracted to create data points
    - Retention settings: how long log events are kept in CloudWatch logs
- CloudWatch Events
    - Event
        - Occur when resources change state
            - EC2 state changed
            - Autoscaling
        - CloudTrail integration
            - API calls
            - Log into console
    - Rules
        - Match incoming events and route them to one or multi targets for processing
    - Targets
        - Lambda
        - SNS
        - SQS
        - Kinesis streams

### Deployment
- Infrastructure as code
    - version control
    - example
        - Cloudformation templates
        - Cloudformation Designer
        - AMI
            - aws image
- CD in Application
    - auto delivery of prod ready code
    - allows repid deployment and rollback if necessary
    - example
        - CodeCommit
        - CodePipeline
        - Elastic BeanStalk
        - OpsWorks
        - Elastic Container Service(ECS)
- Both application and Infrastructure
    - example
        - CodePipeline
        - CodeCommit
        - Elastic BeanStalk
        - OpsWorks
        - Elastic Container Service(ECS)
    - Hybrid Deployments
        - seperate app and infra deployments
- Application Updating Options
    - Prebaking AMIs
    - In-place Upgrade
        - Application update on live EC2 instance
    - Disposable Upgrade
        - Rolling out new EC2 instance and terminating old one
        - Allow staged deployment
- Blue-Green Deployment
    - Staged rollout from existing env(Blue) while tesing new one(Green)
    - Using domain name service(DNS) to increase traffic to green env in stages
    - Requires doubling up on resources
        - $$

### Using Elastic BeanStalk to lauch multiple environments
- seems just demo how to switch mapping env and domain
- but not using same domain name to implement blue-green deployment

### CodePipeline CICD(持續交付/持續整合)
- Background
    - Github
    - Elastic BeanStalk deploy node app
- source - build - staging - production
    - just demo from build to staging
- connect to github repo branch
- deploy as Elatic BeanStalk

### OpsWorks
- Introduction
    - configuration management platform
    - provide more control over infrastructure design and management then ELB
    - infrastructure as code using Chief recipes for fine-grained control
    - consiste of CM model on Stacks Layers Recipes
- Core entities
    - Stack
        - you could imagine the collective of EC2 instances or LBs
    - Layer
        - how to set up instance and reosurces
        - you can mix and match layers, can be used for multiple stacks
        - must include of more than one instance
    - Instance
        - application
- Scaling
    - 24/7 instances added to layer can manually start, stop, reboot the corresponding EC2 instances
    - Auto-scaling
        - time-base instances base on a schedule
        - load-base instances base on several load metric(traffic / CPU utilize)
    - combine 3 types us an effective strategy
- Chef recipes: 我的想像是可以寫一些配置，不同entity可以複用
    - Customisation
    - Redeployment
    - Version control
    - Code reuse

### CloudFront(CDN)
- Introduction
    - cache regular used content
    - web service for high performance content delivery
    - world-wide network of data centres(edge location)
    - reduces number of hops for requests
- Edge locations(2016/1)
    - 16 regions
    - 42 AZ
    - 50+ Edge Locations
- CloudFront Origin Server(資料源頭)
    - Location of content to be delivered
    - Origin server is either S3 or HTTP server
        - HTTP server can be on EC2 instance
        - webservice you managed
    - CloudFront must have access to origin server
- CloudFront Distribution
    - which origin server to get your files and TTL
    - assign a domain name to your new distribution
    - if edge location exist file return, if not it will request origin server and cache at edge location
    - distribution could be invalidated to force renew data
- Delivering Dynamic Content
    - Low TTL
    - dont cache dynamic content
    - ![Cloudfront options](https://i.imgur.com/f6OrpTK.jpg)

### SQS
- Introduction
    - Queue for storing messages
    - Acts as buffer of data for processing servers
    - smooth out the peak demand
    - Up to 10 attributes can be added to a message additional to the message body
    - message size can be set 1KB - 256KB
- Decoupling Processes
    - If average demand exceeds processing capacity, queue will grow indefinitely
    - SQS cam provide cloudwatch metrix -> auto scaling
    - provide upper and lower setpoints
    - ![SQS structure with EC2](https://i.imgur.com/8R5l0qq.png)
- Queue Types
    - Standard
        - default queue type
        - unlimited number of transaction per second
        - guarantee message us delivered at least once although rarely duplicate
        - best-effort ordering(不保證輸入輸出順序？)
    - FIFO
        - limited to 300 transactions per second
        - FIFO delivery
        - Exactly once processing
        - not available for all regions
- Message Lifecycle
    - message receive by the SQS
    - message receive from processing server
        - visibility timeout starts
    - message processed by processimg server
        - visibility timeout ends
    - visibility timeout
        - the time which the message is invisible in the queue and has not been deleted
        - if the message has not been deleted by the visibility timeout period, the message becomes visible and can received again by the processing server
- Dead Letter Queue
    - Queue can be target for message that cannot be processed successfully
    - analysis them or reprocessed later
    - dead letter queue must in the same region and from same account as queue
- Delay Queue
    - Postpone the delivery of new messages
    - message is not visible when it is first added to the queue for defined period time
    - 120000 limit got the number of inflight messages per queue
- Message Timer
    - initial invisibility period for an individual message
    - can be created by console or with DelaySeconds parameter of SendMessage
- Polling
    - Short Polling send response immediately back whether message in queue or not
    - Long Polling waits until a message is available in the queue before sending a response
    - Reduce the number of empty responses when there are no messages available to return
    - Set WaitTimeSeconds(ReceiveMessage) ot ReceiveMesssageWaitTimeSeconds(CreateQueue/SetQueueAttributes) parameter btw 1-20

### SNS
- Introduction
    - Enable to send message up to 256KB to subscribing endpoints or clients
    - Topic means endpoint of publishers to post messages
    - Subsribers subsribe to the topic name
- Transport Protocols
    - HTTP/HTTPS
        - notifications will be delivered through an POST to specified URL
    - Email/Email Json
    - SQS
    - SMS
- Message Format
    - Email transport only contains the payload(message body)
- Support SNS mobile push notification
- Support Amazon Product notification: kindle?
