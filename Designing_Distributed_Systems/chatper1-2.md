# `Designing_Distributed_Systems Note`
## Overview
- 服務與功能快速增長，意味著需要能立即反應用戶需求，微服務或分佈式系統逐漸成為顯學(畢竟不能每次都開戰車吧ＸＤ從agile到micro service都說明這個行業正在趨向分散式系統)
- OOP 以及 分散式系統有著高度相似的設計概念 -> decoupling and componentize
- 歷史故事時間
    - 系統發展
        - 電腦的沿革：舊時王謝堂前燕，飛入尋常百姓家
        - 分散式系統：地位逐漸提升，要如何構建出大型系統彼此溝通將成為難題
            - 容器化、虛擬化的前浪，造就了分散式系統成為可能
    - 軟體開發模式的沿革：很多次的改變，為的就是更好的reuse components
        - 演算法的標準化(1962)
            - Donald Knuth’s collection, The Art of Computer Programming, 1962
            - 不根植於某種OS或硬體，而是解決問題的思維
        - OOP(1990)
            - Erich Gamma, Design Patterns: Elements of Reusable Object-Oriented Programming
            - 提高了可複用性以及演算法的可擴展性
            - reuseable libraries
        - open source(1990-)
            - 社區的力量，推動了分散式系統工具的優化與成熟
- 什麼是分散式系統？
    - 本書談論的是設計思維，不是單一的noSQL或MEAN stack技術棧
- 設計模式的價值？
    - 站在巨人的肩膀上，避免重蹈覆徹
        - 因為當今的分散式系統設計，前人把踩過的坑，都歸結成設計模式了，他不是全新的概念(agile, scalable, reliable)
    - 溝通成本下降，即時根據業務模式有不同的設計模式++，設計模式都讓我們降低溝通的成本
    - 複用組件
        - third-party libraries透過大量使用不斷修復來確保可靠性

## Single-Node Patterns
- 單一機器多個容器的分散式系統設計
    - 容器
        - 資源隔離
        - 所有權
        - 關注點分離(一個image只處理一個任務)
    - 複用基礎建設
    - 發版彈性上升：小步快速迭代

### Sidecar Pattern
- 兩個容器組成
    - 一個是應用程式
    - 一個是邊車容器
        - 強化應用程式容器的功能
        - 共享文件系統、主機名、網路、namesapce相關資源
    - ![sidecar pattern](https://i.imgur.com/RIVDYti.png)
- example1: add SSL cerificate to legacy service
    - 給老舊內部服務加上SSL證書
    - 在流量入口多一個nginx邊車容器處理證書跟導流
    - ![example of sidecar pattern](https://i.imgur.com/0PW4dZ4.png)
- example2: dynamic update legacy service configuration
    - add new http service to sync cloud data to volume path
    - and deliver signal to legacy service and force it restart with new configuration file
- using sidecar to develop reusable service
    - Parameterizing your containers
        - 用環境變量當參數
    - Creating the API surface of your container
    - Documenting the operation of your container
        - 撰寫文件讓使用者知道如何使用
        - [LABEL控制版號](http://label-schema.org/rc1/)
            - the maintainer’s email address
            - web page
            - version of the image
### Ambassador Pattern
- 處理對外部系統的交互，像是你的外交使節？ＸＤ
- ![大使模式](https://i.imgur.com/ZKNYCAJ.png)
- Pros
    - 增加可重用性
    - 關注點分離
- 大使模式範例1
    - 透過中介曾去跟儲存層交互，以MySQL為例，主程式不用管怎麼交互，怎麼聚合結果，只要知道怎麼跟大使交互就可以
    - ![大使模式範例](https://i.imgur.com/itb5RgE.png)
- 大使模式範例2
    - 交互流量控制
    - 透過在ambassador container增加nginx weight配置
        - 可以控制發出流量在production and teed的分佈，藉此測試還在beta中的新功能

### Adapter Pattern
- 將內外部系統各個服務包裝成統一的輸出格式，讓應用程式可以接收統一的輸入，而作相應的處理，在監控(monitor)常需要這樣的統一介面的處理
- ![Adapter pattern](https://i.imgur.com/OyWMymj.png)
- 大多數monitor apis，都實現plugins可以轉換輸出的格式
- 單獨部署Adapter的格式轉換功能也可以避免影響主要程式

### Serving pattern

### Replicated Load-Balanced Services
- 每個server都與其他server相同
- 在server前面有個LB
- features
    - reliability
    - redundancy
    - scaling
#### Stateless Services
![](https://i.imgur.com/QGEc699.png)
- 不需要保存狀態的服務
    - static content servers
    - complex middleware systems that receive and aggre‐ gate responses from numerous different backend systems

#### HA
- most scenario, you need at least two replicas to provide a service with a “highly available” service level agreement (SLA)
    - if you promise your would provide 99.9% availability to users -> downtime 1.4 minute per day(24 × 60 × 0.001)
- Horizontally scalable: systems handle more and more users by adding more replicas
![](https://i.imgur.com/wpo0esg.png)

#### Readiness Probes for Load Balancing
- health probes can be used by a container orchestration system to determine when an application needs to be restarted
- readiness probe determines when an application is ready to serve user requests
    - many applications require some time to become initialized before they are ready to serve

#### Session Tracked Services
![](https://i.imgur.com/GxszhBn.png)
- ensure all requests for a single user map to the same replica
    - performed by hashing the source and destination IP addresses
        - consistent hashing function: minimize the number of users that actually change while scaling up
        - 因為NAT的轉發，在cluster內部使用IP mapping通常效果不佳，此時應該透過application layer，例如cookie

#### Application-Layer Replicated Services
- enables further refinements to the replicated stateless serving pattern for additional functionality
- Caching layer
![](https://i.imgur.com/bCIb7AS.png)
    - web caching proxy
        - an HTTP server that maintains user requests in memory state
- Deploying Cache
![](https://i.imgur.com/lyoNuv8.png)
    - 我們希望cache layer盡可能是大資源數量少的，可以增加命中率，也可以減少資源浪費
    - 使用cache layer之後，IP base的session tracker將失效，因為所有request都被你的cache server轉發了，要改用cookie或header base

#### Varnish reverse proxy
- caching
- throttle module: configured to provide throttling based on IP address and request path
- Rate Limiting and Denial-of-Service Defense
    - 登入前rate limit很低
    - 登入後提高
    - 超限: 429
    - 返回時增加X-RateLimit-Remaining在頭部，讓用戶知道剩下多少額度
- 不支持SSL
    - 在前面再搭一個nginx轉發https流量
    ![](https://i.imgur.com/lZPH8mw.png)
- 相關部署code可以在[這裡](https://github.com/brendandburns/designing-distributed-systems)找到

### Sharded Services
- 通常用於stateful service
- sharding the data is because the size of the state is too large

#### Sharded Caching
![](https://i.imgur.com/A23HMMC.png)

##### Why You Might Need a Sharded Cache
- Each cache has 10 GB of RAM available to store results, and can serve 100 requests per second (RPS)
- 1,000 RPS (10 replicas × 100 requests per second per replica)
- total of 200 GB possible results that could be returned
- we need 10 nodes to response 1000 RPS traffic
    - replicated cache could cache 5% content
    - shared cache could cache 50% content

##### The Role of the Cache in System Performance
- when cache missed, whats the next?
    - hit rate
        - percentage of the time that your cache contains the data for a user request
- improve the speed of requests: less latency
- the total number of requests processed: more RPS
    - if your server could process 1000RPS
    - cache hit rate is 50%
    - you could serve 1500RPS now
- CD的時候要考慮cache要複製，而不是重新部署，否則會有cache rebuild的時間

#### Replicated, Sharded Caches
- 當cache失效之後影響很大的
    - 可以使用sharded cache replicationg pattern

### An Examination of Sharding Functions
- 如何決定end-user request會打到哪個shard cache
    - ShardingFunction
        - Determinism
            - 相同輸入相同輸出
        - Uniformity
            - 輸出在整個輸出空間分布相同

##### Selecting a Key
- 決定誰是你sharding function的輸入
- 可以是多個輸入
    - ip + request_path
- Determining the appropriate key for your sharding function is vital to designing your sharded system well. Determining the correct shard key requires an understanding of the requests that you expect to see.

##### [Consistent Hashing Functions](https://ixyzero.com/blog/archives/4425.html)
- re-sharding
    - hit rate changed if you use normal hash function
- if we use a consistent hashing function for our sharded cache, moving from 10 to 11 shards will only result in remapping < 10% (K / 11) keys.

### Hot Sharding Systems
- scale the cache shard to respond to the increased load
- if you set up autoscaling for each cache shard, you can dynamically grow and shrink each replicated shard as the organic traffic to your service shifts around
![](https://i.imgur.com/EvLvhZD.png)
