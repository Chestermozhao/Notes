# S3 白皮書整理
### breif description
- Amazon S3 是專為從網際網路任何位置存放和擷取任何資料量所建立的物件儲存。這是一項簡單的儲存服務，以極低的成本提供產業領先的耐用性、可用性、效能、安全性以及幾乎無限的可擴展性
### What is S3
- upload and download data from web GUI page
- 按實際用量付費
### 可以在 Amazon S3 存放多少資料
- 總資料量和物件數量不受限制
- 個別物件的大小可在最小 0 位元組到最大 5 TB 之間
- 單一 PUT 可上傳的最大物件為 5 GB
- 大於 100 MB 的物件，客戶應該考慮使用分段上傳功能
### [S3 categories](https://aws.amazon.com/tw/s3/storage-classes/)
![s3 store types](https://i.imgur.com/M6OTysT.png)
- standard: 適用於經常存取資料的一般用途儲存
    - features
        - 低延遲與高輸送量效能
        - 實現跨多個可用區域的 99.999999999% 物件耐用性
        - 針對影響整個可用區域的事件仍可恢復
        - 其設計提供一年內 99.99% 的可用性
        - 以 Amazon S3 服務水準協議做為可用性的保障
        - 為傳輸中資料提供 SSL 支援以及提供靜態資料加密
        - 用於自動將物件遷移至其他 S3 儲存類別的 S3 生命週期管理
- S3 Intelligent-Tiering: 具有未知或變更中存取模式的資料
    - 上傳或轉換到 S3 Intelligent-Tiering 的物件自動存放在經常存取層。S3 Intelligent-Tiering 會監控存取模式，將連續 30 天未存取的物件移到不常存取層，自動將連續 90 天未存取過的物件移至存檔存取層，然後在連續 180 天無存取後移至 Deep Archive 存取層
    - you could extend the archive threshold to most 2 years
    - if you wanna make data from archive or deep archive to usually visited layer
        - archive layer need 3-5 hours
        - deep archive layer need 12 hours
    - how do you know where the data store in?
        - export CSV, OCR, or Parquet report
        - using HEAD request to trace data status
    - 最小時長是30天，小於１２8KB的data不符合這個類別，用標準價格計費
    - available for all regions
    - features
        - 自動優化存取模式不斷變化資料的儲存成本
        - 將物件儲存在四個分別針對經常、不常、存檔和深度存檔存取優化的存取層
        - 經常和不常存取層具有與 S3 標準相同的低延遲和高輸送量效能
        - 針對極少存取的物件啟用選用自動存檔功能
        - 封存存取和深度存取層具有與 Glacier 和 Glacier Deep Archive 相同的效能
        - 實現跨多個可用區域的 99.999999999% 物件耐用性
        - 其設計提供一年內 99.9% 的可用性
        - 以 Amazon S3 服務水準協議做為可用性的保障
        - 些微的每月監控費用和自動分層費用
        - 在 S3 智慧型分層儲存類別內移動物件時，不會產生營運開銷、擷取費用以及額外方案費用。
- S3 standard IA: 適用於長效但不常存取的資料
    - 不常存取但需要在必要時進行快速存取的資料
    - high durability, transfer quantity, low latency
        - 99.999999999% durability
        - 99.9% availability
        - follow SLA
            - 支持SLA 99% availability
    - how to choose standard-IA
        - assign x-amz-storage-class to STANDARD_IA
        - set lifecycle policy
    - if you copy IA to standard
        - you need pay for IA COPY and IA data serialize
    - 最小使用天數30天
    - 128KB最低物件存儲費用
    - features(availability相對standard低)
        - 與 S3 標準相同的低延遲與高輸送量效能
        - 實現跨多個可用區域的 99.999999999% 物件耐用性
        - 針對影響整個可用區域的事件仍可恢復
        - 資料在一個可用區域徹底毀滅的情況下仍可恢復
        - 其設計提供一年內 99.9% 的可用性
        - 以 Amazon S3 服務水準協議做為可用性的保障
        - 為傳輸中資料提供 SSL 支援以及提供靜態資料加密
        - 用於自動將物件遷移至其他 S3 儲存類別的 S3 生命週期管理
- S3 single AZ IA: 適用於長效但不常存取的資料
    - 其他 S3 儲存類別會將資料存放到至少三個可用區域 (AZ)，但 S3 單區域 – IA 不一樣，它會將資料存放到單一 AZ 中，而且成本較 S3 標準 – IA 減少 20%
    - which tyep of data is suitable for single AZ IA
        - replica
        - no matter data recreated easily
    - 有掉資料風險
        - 如果AZ有災情那資料會掉
    - 支持SLA 99% availability
    - you could set multiple object type for single bucket
    - support for all regions
    - features(有永久丟資料的風險)
        - 與 S3 標準相同的低延遲與高輸送量效能
        - 專為單一可用區域中 99.999999999% 的物件耐用性所設計†
        - 其設計提供一年內 99.5% 的可用性
        - 以 Amazon S3 服務水準協議做為可用性的保障
        - 為傳輸中資料提供 SSL 支援以及提供靜態資料加密
        - 用於自動將物件遷移至其他 S3 儲存類別的 S3 生命週期管理
- S3 Glacier: 適用於長期存檔和數據保留
    - 安全、耐用、成本低的儲存類別，適用於資料存檔
    - 不可以使用 Amazon Glacier 直接 API 存取已存檔到 Amazon S3 Glacier 的物件
    - 要請求Glacier的object時需要轉換時間
        - 快速轉換大約1-5分鐘內完成
        - 一般轉換大約需3-5小時
        - 大批轉換大約需5-12小時
    - 有提供更快地還原服務
        - "tier" 任務參數，向同一個物件發出另一個還原請求，即可使用 S3 還原速度升級
        - 需要支付每次還原請求的費用，還有更快還原方案的每 GB 轉換費用
        - 例如，如果您發出大量方案還原，然後在快速方案發出 S3 還原速度升級請求來覆寫進行中的大量方案還原，則需要支付兩次請求的費用，還有快速方案的每 GB 轉換費用
    - 存檔於 Amazon S3 Glacier 的物件至少必須儲存 90 天，而在 90 天內刪除的物件則需按比例支付剩餘天數的儲存費用
        - 提早刪除內容，需要額外支付存儲費用
    - features
        - 實現跨多個可用區域的 99.999999999% 物件耐用性
        - 資料在一個可用區域徹底毀滅的情況下仍可恢復
        - 為傳輸中資料提供 SSL 支援以及提供靜態資料加密
        - 低成本的設計很適用於長期存檔
        - 可設定的擷取時間，從數分鐘到數小時
        - 用於直接將物件上傳至 S3 Glacier 的 S3 PUT API，以及用於自動遷移物件的 S3 生命週期管理
- S3 Glacier Deep Archive: 適用於長期存檔和數位保留
    - 最低成本儲存類別，支援長期保留和數位保留一年存取一或兩次的資料，適用於包含經常擷取或幾分鐘內急需使用之資料的存檔，所有物件至少跨三個分散在各處的可用區域來進行複寫和存放，受到 99.999999999% 耐用性的保護，而且可在 12 小時內還原。
    - 離線保護，或者當公司政策、合約或合規要求必須長期保留資料時
    - 標準轉換速度提供 12 小時傳回資料
    - 大批轉換會在 48 小時內傳回資料
    - SLA提供99.99% availability
    - 99.999999999% durability and 99.99% availability
    - magnetic gateway
        - AWS storage gateway service
        - you need create new magnetic brand on AWS storage gateway
            - later, select target as Glacier/Glacier Deep Archive
    - how to transfer data to S3 Glacier Deep
        - Snowball support big data transferring
        - VTL could backup data and set this data to S3 immediately
        - Direct Connect
    - how to recover data to single-AZ IA
        - using standard transfer and you could access daata after 48 hours
    - 至少要存180天
    - 最少支持40KB資料，如果硬要存，也要付40KB的錢
    - features
        - 實現跨多個可用區域的 99.999999999% 物件耐用性
        - 最低成本的儲存類別，旨在長期保留將保留 7-10 年的資料
        - 非常適合於替代磁帶程式庫
        - 12 小時內的擷取時間
        - 用於直接將物件上傳至 S3 Glacier Deep Archive 的 S3 PUT API，以及用於自動遷移物件的 S3 生命週期管理
- S3 Outposts: 內部部署物件儲存以滿足資料駐留需求
    - 將物件儲存傳送至內部部署 AWS Outposts 環境，多個裝置和伺服器上以持久、冗餘的方式存放資料
    - features
        - 透過 S3 SDK 的 S3 物件相容性和儲存貯體管理
        - 旨在將資料以持久、冗餘的方式存放於您的 Outposts
        - 使用 SSE-S3 和 SSE-C 進行加密
        - 使用 IAM 和 S3 存取點進行身份驗證和授權
        - 使用 AWS DataSync 將資料傳輸至 AWS 區域
        - S3 生命週期過期動作
### S3資料組織方式
- bucket
- key: your data path
### 支持S3 SLA協議
![](https://i.imgur.com/noHDDaM.png)
![](https://i.imgur.com/2l93ev4.png)
- 簡言之就是如果服務中斷，AWS會給予積分回饋
### PCU
- 保證快速擷取的擷取容量可在您需要時供您使用
- 確保每 5 分鐘至少可執行 3 次快速擷取，且提供最高每秒 150 MB 的擷取輸送量
- 佈建容量單位的費用為每月 100 USD
### 相同bucket可以使用不同category S3?
- yes
### 數據一致性
- 先寫後讀，保證每次讀取都是最新數據
### regions and AZs
- 創建bucket時可以選擇region
- 會自動備份到三個AZ
    - AWS 可用區域是 AWS 區域內的實體隔離位置。在每個 AWS 區域內，S3 至少在三個相隔數英里的 AZ 運作，以避免受到火災、洪水等當地事件的影響。
### 費用
- 不同region不同計費
    - 各地AWS成本不同
- 跨region要另外計費
- 定價不含稅
- [費用計算工具](https://calculator.aws/#/)
#### Free Tier
- 第一年每月可以獲得
    - 5 GB 的 Amazon S3 標準儲存
    - 20,000 次 Get 請求
    - 2,000 次 Put 請求
    - 15 GB 的資料傳入
    - 15 GB 的資料傳出
- 這邊有流量計算的教學～我看得不是特別仔細，可以再看下
#### Versioning fee
- 3/1 4GB and 3/16 5GB
    - `(4GB*31 + 5GB*16)*24h/per day`
    - 每月 6.581 GB
#### 其他AWS帳號想存取你的bucket
- 可以選擇將bucket設定為申請者付款
- client side need pay the money of request and download

### IPv6
- 只要將應用程式指向 Amazon S3 的新「雙堆疊」端點即可開始使用，此端點同時支援透過 IPv4 和 IPv6 存取
- 使用 IPv6 而受到影響的應用程式可以隨時切換回標準的僅 IPv4 端點
- 使用網站託管和透過 BitTorrent 存取時，目前無法使用 IPv6 支援
- 所有 AWS 區域都支援 IPv6

### Notification
- Amazon S3 中進行 PUT、POST、COPY 或 DELETE 這類動作時，會傳送 Amazon S3 事件通知做為回應
    - SQS
    - SNS
    - Lambda
- free for notification, but you need pay the fee of SQS/SNS/Lambda

### Transfer Acceleration
- 用戶端與 Amazon S3 儲存貯體之間提供快速、輕鬆且安全的長距離檔案傳輸
- 使用場景
    - 來源與目的地之間距離較遠
    - 有更多可用頻寬
    - 物件大小較大
- 安全性與 Amazon S3 一般傳輸的安全程度相當
- 傳輸速度不如一般的 Amazon S3
    - 不會收取費用
    - 上傳時會繞過 S3 Transfer Acceleration 系統
- 可以搭配分段上傳
- CDN vs Transfer Acceleration
    - 物件小於 1 GB 或是資料集的大小小於 1 GB，您應該考慮使用 Amazon CloudFront 的 PUT/POST 命令
    - 較高的輸送量時，S3 Transfer Acceleration 是較佳的選擇
- AWS Snowball vs Transfer Acceleration
    - AWS Snowball 通常需要 5 到 7 天的往返運送時間
        - 速度較慢，但可以傳輸大量資料
    - 如果資料超大，可以混合使用，先透過SnowBall initialize
- HIPAA 合格服務
    - 某種醫療規範，對隱私跟一些規範的定義

### Security in S3
- four mechanisms for resource accessment
    - IAM
    - bucket policy
    - ACL
    - presign url
- access log
    - configure cloudtrail
        - request type, access resources, date and datetime
- encrypt
    - server side
        - SSE-S3
            - 由 Amazon 管理金鑰
        - SSE-C
            - Amazon S3 的物件進行加密及解密，但您需要管理傳送到 Amazon S3 用於加密和解密物件的金鑰
        - SSE-KMS
            - 用 AWS Key Management Service (AWS KMS) 來管理您的加密金鑰
    - client-side
        - 傳送物件到 Amazon S3 儲存之前先加密物件，請使用用戶端庫

### Amazon S3 的 Amazon VPC endpoint
- gateway endpoint
    - 在路由表中指定的閘道
- interface endpoint
    - 用私有 IP 將請求從您的 VPC 內部、內部部署或其他 AWS 區域路由
- bucket policy could limit access authenication to specific VPC endpoint
- privatelink
    - S3 -> interface endpoint
        - 在endpoint透過ENI(彈性網路界面)
        - ENI裡面有S3的private IP
    - AWS Direct Connect/AWS VPN
        - 透過ENI連線到S3
        - 走AWS內部網路非常快
- 怎麼取決用gateway endpoint or private link?
    - if your vpc and S3 locate in same region
        - gateway endpoint
        - the reason is when your service locate in same region, transiting is free
    - else
        - PrivateLink
- May I set either type endpoints to my VPC?
    - Positive
    - you could set gateway endpoint for most of traffic
    - specific dns name will transfer data by interface endpoint if matching the rule

#### Macie
- use machine learning to discover, classify, and protect your stored data
    - dataset is access log of S3 data
    - if the suspicious operation take place, it will be triggered and ask you reset password or access failed notification
- Macie just save part of your log data for continuously analysis

#### Access Analyzer
- 評估您的儲存貯體存取策略，並讓您能發現和快速修復具有潛在意外存取權限的bucket

### Access point
- you could create hundreds of access points with one bucket
    - access point provide customized route path
    - particular auth limit and network control policy
- you could create a access point for your specific app
    - limit particular VPC
    - create policy which just allow specific prefix resource could be accessed
    - each AP include the only DNS name
- whats different btw bucket and AP?
    - AP is the resource definition of bucket, it include of some of resource definition element
        - ARN
        - host name
            - `https://[access_point_name]-[account ID].s3-accesspoint.[region].amazonaws.com`
        - access policy
        - network source control
    - not support CopyObject API
- how to manage AP?
    - using cloudformation to deploy the APs
    - using CloudTrail to trace APs
- 對組織中的所有存取點強制執行「無網際網路資料存取」政策
    - AWS SCP，僅支援 `create_access_point()` API 中 “network origin control” 參數的 “vpc” 值
    - 之前曾建立過任何網際網路對應存取點，則可將其移除
- may I remove bucket access for all traffic?
    - No, but you could add a policy for refusing all traffic without AP
- you could create 1000 APs for single resion per account
    - this is default value
- using AP is free, you just need pay for S3

### Durability
- most S3 service support `99.999999999%(9*10^-11)`
    - Amazon S3 standard, S3 standard – IA, and S3 Glacier, copy data to 3AZ before response with "SUCCESS"
- how to check data correction? error detection?
    - CRC
    - Content-MD5
- versioning
    - everytime you operate CUD for your data, AWS tag the particular version
    - get method will access the latest version of data
    - recover data while deleting or modifying data accidently
    - the only one could remove versions is bucket owner
    - you could configure lifecycle configuratino and version setting to make your policy more cost-effective
- MFA
    - multi-factor authemticatino will decrease the propability of operation error

### Store management
#### object tags
- key-value pair for object
- you could set most 10 tags for single object
- you could set CRUD operation, lifecycle configuration or expire rules on tags
- update tags with PUT method, which means you need request for all tags, it is not increasing

#### Storing Class type analysis
- S3 功能會自動識別何時為不常存取模式，以協助您將儲存轉換成 S3 標準 – IA
- 儲存類別分析在 S3 管理主控台會每天更新
- you could export analysis report to specific bucket

#### Inventory
- 針對 S3 bucket或prefix，每日或每週提供物件及其對應中繼資料的 CSV、ORC 或 Parquet 檔案輸出
- 驗證物件的加密和複寫狀態
- 簡化並加速商業工作流程和大數據任務
- you could encrypt inventory report

#### Batch operation
- 跨多個物件自動執行單一操作
    - 複製物件、或執行 AWS Lambda 函數
- S3 批次操作還能管理重試、顯示進度、傳遞通知、提供完整報告，以及將事件傳送到 AWS CloudTrail

#### Object Lock
- 阻擋在客戶定義的保留期內刪除物件版本，讓您能夠執行保留政策，為資料增加另一層的保護或遵守法律規定
    - 指定時間內version不可刪除或修改
    - 優先級高於生命週期轉換
- two patterns
    - control pattern
        - IAM user with auth could remove data
    - rule pattern
        - no one could remove data, even though root user

#### CloudWatch storing index
- activate cloudwatch index
    - you could use it after 15mins
- by default, all bucket activate this index and export data everyday
- you could set some rules for notification
    - for instance
        - if 4xx ratio more than 5%

#### lifecycle policy
- transfer store class base on create days
    - you could specify particular prefix
- 將物件設定為在特定時段之後刪除
    - pros
        - 透過限制不完整的分段上傳的存放時間來節省成本
        - 您的應用程式上傳了數個分段物件部分，但從未遞交它們，您仍需支付該儲存的費用

### Storage anaysis and insight
- Storage Lens
    - analysis the quantity of using
    - you could view this as dashboard, in the meanwhile, it could provide you advice to improve your security configuration and cost effectiveness
    - aggregate quentity of using and activity logs
    - suitable to large dataset which spread to multiple regions, account or storage class
    - if you set for account, it will support you after 24-48 hours; however setting for organization will take less wating time
    - daily report export to CSV or Parquet
    - 免費指標保留 14 天的歷史資料，而進階指標和建議保留 15 個月的歷史資料。對於可選的指標匯出，您可以設定所需的任何保留期限，並且將支付標準的 S3 儲存費用
    - difference btw Inventory
        - inventory 提供了物件及其對應中繼資料的清單，此清單可用於對您的儲存執行物件層面的分析。S3 Storage Lens 提供按組織、帳戶、區域、儲存類別、儲存貯體和前綴層面彙總的指標，從而提高了您的儲存在組織範圍內的可見性
    - differnce btw SCA
        - 基於個別儲存貯體/前綴/標籤內在過去 30-90 天內的物件層面存取模式建立物件存留期分組，S3 儲存類別分析可提供最佳儲存類別方面的建議

### Query in place
- 不需要額外下載就可以針對資料做分析
    - Ahena
    - Select
    - Redshift Spectrum

#### S3 Select
- 使用簡單的 SQL 陳述式從物件擷取較小的目標資料集
- 搭配 Presto、Apache Hive 和 Apache Spark 等大數據架構，以掃描和篩選 Amazon S3 的資料
- S3 Select 掃描物件內容並篩選為較小的目標資料集，簡化並提升高達 400% 的效能

#### Athena
- 無伺服器的服務，您不須設定或管理任何基礎架構，即可立刻開始分析資料
- 使用 Presto，提供完整的標準 SQL 支援且能接受各種標準資料格式，包括 CSV、JSON、ORC、Apache Parquet 和 Avro
- 提供迅捷的臨機操作查詢功能，也和 Amazon QuickSight 整合提供簡易的視覺化功能，同時還可以處理複雜的分析，包括大規模聯結、視窗函數和陣列

#### Redshift Spectrum
- 可擴展到數千個執行個體，因此無論資料大小都能快速執行查詢
- Amazon S3 資料使用與目前 Amazon Redshift 查詢完全一樣的 SQL，並使用相同的 BI 工具連接到相同的 Amazon Redshift 端點

### Replication
- origin data could have from identical or different account
- you could set replica across region or set in the same region
- need activate versioning first
- lifecycle policy would NOT replacate to by default
- support for multiple replica target bucket
- support mutual replicate but you need configure settings respectively
- replicate encrypt content through KMS
- 物件在整個複寫程序中都會保持加密。加密的物件會透過 SSL 傳輸
- 可以跨 AWS 帳戶使用複寫功能來防止惡意或意外刪除
- 複製時間控制
    - S3 複寫時間控制的設計可在幾秒內複寫大部分的物件、在 5 分鐘內複寫 99% 的物件，以及在 15 分鐘內複寫 99.99% 的物件
- replica index and event
    - 搭配cloudwatch如果發生改變可以透過SQS, SNS, lambda推送
- 複寫時間控制服務水準協議 (SLA)
    - 在 15 分鐘內複寫 99.99% 的物件
        - 在 15 分鐘內的複寫物件低於 99.9%，則 S3 RTC SLA 會為任何複寫時間超過 15 分鐘的物件提供服務積分
        - 對複寫區域在 15 分鐘內的複寫物件低於 99.9%，則您有資格獲得 Amazon S3 複寫時間控制 SLA 積分
- pricing
    - 在選取的目標 S3 儲存類別中儲存的 S3 費用
    - 主要副本和複寫 PUT 請求的儲存費用
    - 不常存取儲存擷取費用
    - 針對 CRR
        - 您也要支付區域間資料傳輸費用
        - S3 複寫指標的計費方式與 Amazon CloudWatch 自訂指標相同
        - S3 複寫時間控制要支付複寫時間控制資料傳輸費
- 複寫刪除標記
    - 會在所有複本中生效
- Amazon S3 複寫不可在 AWS 中國區域與中國以外的 AWS 區域之間使用

#### CRR(cross-region replication)
- 在不同的地理區域提供低延遲的資料存取
- 變更複寫之物件的帳戶擁有權，以防止資料被意外刪除

#### SRR(single-region replication)
- SRR 可以將資料副本保存在與原始帳戶區域相同的另一個 AWS 帳戶中
- 使用 SRR 變更複寫之物件的帳戶擁有權，以防止資料被意外刪除
- 彙總來自不同 S3 儲存貯體的日誌以進行區域內處理
- 在測試與開發環境之間設定即時複寫
