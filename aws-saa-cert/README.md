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
