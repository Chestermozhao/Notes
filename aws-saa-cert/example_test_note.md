# SAA SAMPLE QUESTIONS REVIEW
## Topic based
### CloudFront
#### 1. AWS Global Infrastructure that is used for content distribution
![Edge location](https://i.imgur.com/iZmLh5L.png)
- Edge location
    - deliver high availability, scalability, and performance of your application
    - used by other services such as Lambda and Amazon CloudFront
- (X) Bastion Hosts
    - not part of the AWS Global Infrastructure
    - a host computer or a “jump server” used to allow SSH access to your EC2 instances from an outside network
- (X) Hypervisor
    - a computer software, firmware, or hardware that creates and runs virtual machines
    - not part of the AWS Global Infrastructure
- (X) VPC Endpoint
    - not part of the AWS Global Infrastructure
    - used to privately connect your VPC to other AWS services and endpoint services

#### 2. member-only access to some of its high quality media files with CloudFront
- Signed Cookies and signed URLs provide the same basic functionality；allow you to control who can access your content
    - Use signed URLs for the following cases:
        - You want to use an RTMP distribution. Signed cookies aren’t supported for RTMP distributions.
        ![](https://i.imgur.com/IigvPpB.png)
        ![](https://i.imgur.com/ZHDQMlY.png)
        - You want to restrict access to individual files, for example, an installation download for your application.
        - Your users are using a client (for example, a custom HTTP client) that doesn’t support cookies.
    - Use signed cookies for the following cases:
        - You want to provide access to multiple restricted files, for example, all of the files for a video in HLS format or all of the files in the subscribers’ area of a website.
        - You don’t want to change your current URLs.
- (X) use Match Viewer as its Origin Protocol Policy which will automatically match the user request
    - configures CloudFront to communicate with your origin using HTTP or HTTPS, depending on the protocol of the viewer request
    - CloudFront caches the object only once even if viewers make requests using both HTTP and HTTPS protocols.
- (X) Configure your CloudFront distribution to use Field-Level Encryption to protect your private data and only allow access to members
    - Field-Level Encryption only allows you to securely upload user-submitted sensitive information to your web servers
    - does not provide access to download multiple private files

#### 3. Using CloudFront, what method would be used to serve content that is stored in S3, but not publicly accessible from S3 directly?
- When you create or update a distribution in CloudFront, you can add an origin access identity (OAI) and automatically update the bucket policy to give the origin access identity permission to access your bucket(S3)
    - Deny access to anyone that you don’t want to have access using Amazon S3 URLs.
    - Grant the CloudFront origin access identity the applicable permissions on the bucket.

#### 4. application’s origin server is being hit for each request instead of the AWS Edge locations, which serve the cached objects
- You can control how long your objects stay in a CloudFront cache before CloudFront forwards another request to your origin. Reducing the duration allows you to serve dynamic content. Increasing the duration means your users get better performance because your objects are more likely to be served directly from the edge cache.
    - The Cache-Control and Expires headers control how long objects stay in the cache
        - Cache-Control max-age directive lets you specify how long (in seconds) you want an object to remain in the cache before CloudFront gets the object again from the origin server. The minimum expiration time CloudFront supports is 0 seconds for web distributions and 3600 seconds for RTMP distributions

#### 5. you found out that there are other travel websites linking and using your photos
- In Amazon S3, all objects are private by default
- the object owner can optionally share objects with others by creating a pre-signed URL
- who receives the pre-signed URL can then access the object
- (X) Blocking the IP addresses of the offending websites using NACL is also incorrect.
    - Blocking IP address using NACLs is not a very efficient method because a quick change in IP address would easily bypass this configuration.
- (X) Storing and privately serving the high-quality photos on Amazon WorkDocs instead
    - WorkDocs is simply a fully managed, secure content creation, storage, and collaboration service
    - not a suitable service for storing static content
    - WorkDocs is more often used to easily create, edit, and share documents for collaboration and not for serving object data like Amazon S3.

#### 6. secure your application by allowing multiple domains to serve SSL traffic over the same IP address
- SNI Custom SSL relies on the SNI extension of the Transport Layer Security protocol, which allows multiple domains to serve SSL traffic over the same IP address by including the hostname which the viewers are trying to connect to.
- Some users may not be able to access your content because some older browsers do not support SNI and will not be able to establish a connection with CloudFront to load the HTTPS version of your content
- If you need to support non-SNI compliant browsers for HTTPS content, it is recommended to use the Dedicated IP Custom SSL feature
- Classic Load Balancer does not support Server Name Indication (SNI)

#### 7. the load on the website has increased which resulted in slower response time for the site visitors
- static for CDN
- application with elasticache
- (X) Deploying the website to all regions in different VPCs for faster processing
    - too expensive
- (X) Storage Gateway
    - for storage

### S3
#### 1. The company stores all its backups on an Amazon S3 bucket. It is required that data stored on the S3 bucket must be encrypted.
![](https://i.imgur.com/M7PrM6c.png)
- server-side encrypt
    - Use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)
        - uses AES-256 encryption
    - Use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)
    - Use Server-Side Encryption with Customer-Provided Keys (SSE-C)
- client-side encrypt
    - Client-side encryption is the act of encrypting data before sending it to Amazon S3
    - using local master key pair

#### 2. Test realize about Amazon S3 Standard – Infrequent Access storage class
![](https://i.imgur.com/V2ViL06.jpg)
- data that is accessed less frequently
- rapid access when needed
- Key Features:
    - Same low latency and high throughput performance of Standard
    - Designed for durability of 99.999999999% of objects
    - Designed for 99.9% availability over a given year
    - Backed with the Amazon S3 Service Level Agreement for availability
    - Supports SSL encryption of data in transit and at rest
    - Lifecycle management for automatic migration of objects

#### 3. cost-efficient and scalable storage option for start-up company
![](https://i.imgur.com/TPIuRYU.png)
- Use Amazon S3 as the data storage and CloudFront as the CDN.
- (X) Redishift: usually for warehouse

#### 4. need to aggregate all the data in the fastest way
- Transfer Acceleration
- Multipart upload
    - allows you to upload a single object as a set of parts. After all the parts of your object are uploaded, Amazon S3 then presents the data as a single object. This approach is the fastest way to aggregate all the data.
- replicating the objects to the destination bucket takes about 15 minutes.

#### 5. transfer obsolete data from their S3 bucket to a low-cost storage system in AWS
![](https://i.imgur.com/dw774o3.png)
- Transition actions
    - In which you define when objects transition to another storage class. For example, you may choose to transition objects to the STANDARD_IA (IA, for infrequent access) storage class 30 days after creation, or archive objects to the GLACIER storage class one year after creation.
- Expiration actions
    - In which you specify when the objects expire. Then Amazon S3 deletes the expired objects on your behalf.
- Use CloudEndure Migration
    - a highly automated lift-and-shift (rehost) solution that simplifies, expedites, and reduces the cost of migrating applications to AWS.

#### 6. protect the S3 objects in your bucket from both accidental deletion and overwriting
- Versioning
    - a means of keeping multiple variants of an object in the same bucket. Versioning-enabled buckets enable you to recover objects from accidental deletion or overwrite
- MFA (Multi-Factor Authentication)

#### 7. most cost-effective solution for archive most of data and some of data need transfer to IA type
![](https://i.imgur.com/7Mq2SHj.png)
- 因為題目提到最成本效益考量ＸＤ所以選one-zone

#### 8. Data need encrypt but master keys and the unencrypted data should never be sent to AWS
![](https://i.imgur.com/WYgJ0X7.png)
- client side encrypt
    - 1. The Amazon S3 encryption client generates a one-time-use symmetric key (also known as a data encryption key or data key) locally. It uses the data key to encrypt the data of a single Amazon S3 object. The client generates a separate data key for each object.
    - 2. The client encrypts the data encryption key using the master key that you provide. The client uploads the encrypted data key and its material description as part of the object metadata. The client uses the material description to determine which client-side master key to use for decryption.
    - 3. The client uploads the encrypted data to Amazon S3 and saves the encrypted data key as object metadata (x-amz-meta-x-amz-key) in Amazon S3.
    - 4. When downloading an object – The client downloads the encrypted object from Amazon S3. Using the material description from the object’s metadata, the client determines which master key to use to decrypt the data key. The client uses that master key to decrypt the data key and then uses the data key to decrypt the object.

### EC2
