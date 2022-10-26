# Lesson
Go through the following on some diagram / graph software (or directly through S3 on AWS)

S3 (Simple Storage Solution)
Highly Available Object Store with 'infinite' storage
Allows you to store and retrieve any data from anywhere on the web, highly scalable, reliable, fast and expensive

Data stored as 'objects', if you wish to edit an object you have to download and upload the new version. 
Objects are stored in an 'S3 Bucket'
Buckets must have a globally unique name so it can be accessed 

## Redundancy
Data in S3 is stored redundantly across multiple facilities + multiple devices in each facility. AWS fully manages this (DSaaS)
You lose approx 1 file per 10 million every 10,000 years (99.9999999999 11 9's reliability)

use cases: 
Storage web content:
larger web content such as videos, audio or HD images can be uploaded and retrieved with a unique URL https://aws-intro-bucket.s3-eu-west-1.amazonaws.com/001.mp3 

Static Web Hosting:
host entire statc sites, includes HTML, CSS, JS + images and other resources. Can be delivered directly from S3 or integrated into a web server 

Backups and Archiving:
storage of large sets of data, generally for companies that need to store data for access at later times. For infrequent read access there are separate and cheaper plans

## Types of storage
https://aws.amazon.com/s3/pricing/?trk=9845b571-f118-41f9-ae80-53f3364524c4&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|GB|EN|Text&s_kwcid=AL!4422!3!536456069933!e!!g!!amazon%20s3%20cloud%20storage%20pricing&ef_id=Cj0KCQjwof6WBhD4ARIsAOi65airFr33b94qfjpYPhcwItZX92R5-C5t_lZ2jnFYZjXp1eD99di34-IaAqROEALw_wcB:G:s&s_kwcid=AL!4422!3!536456069933!e!!g!!amazon%20s3%20cloud%20storage%20pricing
S3 is a blanket term for types of storage, there are multiple types of storage you can use:

Standard:
Default S3, used when data is often accessed (web hosting). Cross region replication for redundancy, most expensive type of storage for adding of data, but cheapest and quickest for retrieval of data ($0.022 per gb approx)

IA (Infrequently accessed):
Data that is accessed less frequently but requires rapid access when it is needed, cheaper for storage but costs $0.01 per gb for retrieval. Useful for backups, where you generally won't ened to retrieve but if you do it is simple and easy to do so ($0.0125 per gb)

IA - One Zone:
Same as IA but it is only stored in one AZ, is cheaper than IA but is less reliable. Not reccomended for critical data ($0.01 per gb)

Intelligent-Tiering:
Optimises storage costs by moving objects between standard and IA dependant on access patterns. Useful for when you do not know how often the data will be accessed, costs the same as standard and IA with a $0.0025 per 1,000 objects cost

Glacier:
Useful for long term low cost storage where data rarely needs to be retrieved. Should not be used if you require quick access as data CAN take several hours. There are many tiers of glacier storage and they are generally used for companies to keep records of transactions that may need retrieval during auditing etc.
Glacier Instant retrieval - Accessed once a quarter (3 months) and retrieved in miliseconds $0.01 per gb and expensive retrieval 
Glacier Flexible retrieval - Accessed once a quarter, can take betwen 1 minute and 12 hours (depending on when the request is made) $0.0036 er gb
Deep archive - accessed once or twice a year and restored within 12 hours $0.00099 per gb

Generally more accessible data is expensive to upload but cheap to access and vice versa

## Upload

There are different methods of adding data to your S3 bucket: 
- Through the AWS site / CLI access to AWS (small files)
- Through an AWS edge location (medium files)
- Physical data storage through snowball (single petabyte files) or snowmobiles (100pb truck) which plugs into your data centre
https://www.youtube.com/watch?v=8vQmTZTq7nw (AWS Snowmobile)


# Demo
Create an S3 bucket and upload the files from https://gitlab.com/Reece-Elder/devops-m5-s3
In the properties of the section make the bucket public and set it to be a static hosted website and select index.html 

# Exercise
Using the S3 sample website, make some slight changes to the HTMl. Create an S3 bucket and host the simple website in the bucket