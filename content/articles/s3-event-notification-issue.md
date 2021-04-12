Title: How to resolve "Unable to validate the following destination configurations" while adding event notification to your S3 bucket?
Date: 2021-2-25 22:11
Modified: 2021-2-25 22:11
Category: tutorial fixes
Tags: S3, AWS, lambda, awscli
Slug: s3-event-notification-issue
Summary: In this small article, I'll demonstrate how I
resolved the lambda issue while adding S3 event notification.

# Problem

I have an existing S3 bucket and I wanted to add an S3 event notification to invoke my lambda function's dev alias. I
read
the `s3api` [put-bucket-notification-configuration](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-notification-configuration.html)
documentation and prepare the `notification.json` file like this:

```json
{
    "LambdaFunctionConfigurations": [
        {
            "Id": "ToInvokeMyLambdaFunction",
            "LambdaFunctionArn": "arn:aws:lambda:ap-northeast-1:123456789101:function:TestFunc:dev",
            "Events": [
                "s3:ObjectCreated:Put"
            ],
            "Filter": {
                "Key": {
                    "FilterRules": [
                        {
                            "Name": "suffix",
                            "Value": "awesome_data.csv"
                        }
                    ]
                }
            }
        }
    ]
}
```

Then I execute the `s3api` command:

```bash
$ aws s3api put-bucket-notification-configuration \
 --bucket MyAwesomeBucket \
 --notification-configuration file://notification.json
```

I got an error that said:

```bash
An error occurred (InvalidArgument) when calling the PutBucketNotificationConfiguration operation: Unable to validate the following destination configurations
```

I checked my `aws-cli` version, it was the recommended one:

```bash
╰─$ aws --version
aws-cli/2.0.12 Python/3.7.4 Darwin/20.3.0 botocore/2.0.0dev16
```

*But... It works when I do it from the S3 console...*

![cat](https://media.giphy.com/media/xT0GqtpF1NWd9VbstO/giphy.gif)

I tried executing the same `aws s3api` command again now with the `--debug` flag. And in the middle of the long debug
output, I see this:

```
$ aws s3api put-bucket-notification-configuration \
 --bucket MyAwesomeBucket \
 --notification-configuration file://notification.json \
 --debug

...
2021-02-25 21:39:13,902 - MainThread - botocore.parsers - DEBUG - Response body:
b'<?xml version="1.0" encoding="UTF-8"?>\n<Error><Code>InvalidArgument</Code><Message>Unable to validate the following destination configurations</Message><ArgumentName1>arn:aws:lambda:ap-northeast-1:123456789101:function:TestFunc:dev, null</ArgumentName1><ArgumentValue1>Not authorized to invoke function [arn:aws:lambda:ap-northeast-1:123456789101:function:TestFunc:dev]</ArgumentValue1><RequestId>2B8705F2FD8848F2</RequestId><HostId>bj9ahrqPxN3emWnZ008dtkVmVR9VVxfFjAJAw9hKvhoa4vtdHXaGi/x4a4Okki3oJhbaeHe0Ppk=</HostId></Error>'
...
```

The gist of it is `Not authorized to invoke function [arn:aws:lambda:ap-northeast-1:123456789101:function:TestFunc:dev]`

So the problem was with the lambda permission. :thinking:

# Solution

Digging around the internet I find [this](https://forums.aws.amazon.com/thread.jspa?threadID=182758)
And the solution is to give your lambda a permission to being invoked by S3 first. Which can be done like this:

```bash
$ aws lambda add-permission \
 --function-name TestFunc:dev \
 --profile default \
 --statement-id AllowToBeInvoked \
 --action "lambda:InvokeFunction" \
 --principal s3.amazonaws.com \
 --source-arn "arn:aws:s3:::MyAwesomeBucket" \
 --source-account 123456789101
```

I got the output like this:

```bash
{
 "Statement": "{\"Sid\":\"AllowToBeInvoked\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:ap-northeast-1:123456789101:function:TestFunc:dev\",\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"123456789101\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::MyAwesomeBucket\"}}}"
}
```

Finally, executing the `aws s3api` command, I was able to put S3 event notification on `MyAwesomeBucket`

```bash
$ aws s3api put-bucket-notification-configuration \
 --bucket MyAwesomeBucket \
 --notification-configuration file://notification.json
```

I checked my lambda console and I can verify the S3 trigger is applied. :confetti_ball:
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1104077/1013252b-7ede-d418-a023-4a7052031a4d.png)

References:

1. https://forums.aws.amazon.com/thread.jspa?threadID=182758
2. https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html
3. https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-notification-configuration.html
