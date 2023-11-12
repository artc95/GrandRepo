# Lambda - template
purpose: Lambda receives Telegram message from chat, then replies "oke".
reference: https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions

related projects: Sentimental, snelbestel

## AWS > ECR
- select region (region-specific!) e.g. Ireland
- "Create repository"
  - Tag immutability; Scan on push; KMS encryption = disabled

## Github Actions with AWS - cicd_pr.yml
- AWS > IAM
- create User e.g. "sentimental_GithubActions_uploadECR_updateLambda"
  - "Attach policies directly" > "Create policy"
- create Policy (to build Docker image, upload image to ECR, and update Lambda code)
  - can reuse User's name
  - sample description: "For Sentimental project Github Actions. Create Access Key and Secret to use in Github, for Github Actions build Docker image, upload it to ECR and update Lambda code."
  - attach to User (check IAM Policy https://github.com/aws-actions/amazon-ecr-login#docker-credentials):
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetRepositoryScanningConfiguration",
                "ecr:CompleteLayerUpload",
                "ecr:DescribeImages",
                "ecr:DescribeRepositories",
                "ecr:GetDownloadUrlForLayer",
                "ecr:InitiateLayerUpload",
                "ecr:ListImages",
                "ecr:PutImage",
                "ecr:StartImageScan",
                "ecr:TagResource",
                "ecr:UploadLayerPart"
            ],
            "Resource": "arn:aws:ecr:eu-west-1:109746771938:repository/sentimental"
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:UpdateFunctionCode"
            ],
            "Resource": "arn:aws:lambda:eu-west-1:109746771938:function:sentimental"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```
- in User, 
  - 'Security credentials' > create 'Access key'
  - add secrets in Github repo under "Settings" > Security > "Secrets and variables"

## Dockerfile
- create
- push cicd_pr.yml, and Dockerfile etc. to create intial ECR image, to create Lambda (which needs Container image)

## AWS >>> Lambda
- select region (Lambda region-specific!) e.g. Ireland
- "Create function"
  - "Container image"
  - Architecture = default
  - ExecutionRole = "Create a new role with basic Lambda permissions"
- "Configuration"
  - "Function URL"
      - "Create", "Auth type"="NONE", everything else defaults
  - "Environment variables" - in main.py, set all os.environ variables under "Environment variables", for this sample:
    - function_url, from previous step
    - telegram_token, cryptocom_key, cryptocom_secret
  

## lambda_function.py
- Docker build and test locally:
  - (optional) download/open Docker desktop to manage Docker images
  - run in directory with Dockerfile: `docker build --platform linux/amd64 -t docker-image:sentimental .`
  - run built Docker image: `docker run -p 9000:8080 docker-image:sentimental`
  - 
