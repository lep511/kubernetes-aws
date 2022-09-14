# AWS Lambda – Container Image Support

### [Link](https://aws.amazon.com/es/blogs/aws/new-for-aws-lambda-container-image-support/)
<br>

1. docker build -t sample-lambda .

2. docker run -p 9000:8080 sample-lambda

3. curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

4. aws ecr get-login-password --region *us-east-1* | docker login --username AWS --password-stdin *554815294851*.dkr.ecr.*us-east-1*.amazonaws.com

5. aws ecr create-repository \
    --repository-name python-sample \
    --image-scanning-configuration scanOnPush=true \
    --region *us-east-1*

6. docker tag python-sample:latest *554815294851*.dkr.ecr.*us-east-1*.amazonaws.com/python-sample:latest

7. docker push *554815294851*.dkr.ecr.*us-east-1*.amazonaws.com/python-sample:latest