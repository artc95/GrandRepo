# Lambda - template
purpose: Lambda receives Telegram message from chat, then replies with same message.
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
- create it!
- commit and push to Github repo: cicd_pr.yml, and Dockerfile etc. to create intial ECR image, to create Lambda (which needs Container image)

## Telegram
- create bot, get token and check_id etc., see https://core.telegram.org/bots/api

## AWS > Lambda
- select region (Lambda region-specific!) e.g. Ireland
- "Create function"
  - "Container image"
  - Architecture = default
  - ExecutionRole = "Create a new role with basic Lambda permissions"
- "Configuration"
  - "Function URL"
      - "Create", "Auth type"="NONE", everything else defaults
  - "Environment variables" - in main.py, set all os.environ variables under "Environment variables", for this sample:
    - function_url, from "Function URL" previous step
    - telegram_token, from Telegram step
    
## lambda_function.py
- for this sample, test via Telegram - send message to bot, expect same message as reply!
- Docker build and test locally:
  - (optional) download/open Docker desktop to manage Docker images
  - run in directory with Dockerfile: `docker build --platform linux/amd64 -t docker-image:sentimental .`
  - run built Docker image: `docker run -p 9000:8080 docker-image:sentimental`
  - (Windows) in Powershell, `Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post -Body '{}' -ContentType "application/json"`
  - check "StatusCode"=200, "Content"=<what lambda_function.handler returns>
  - (optional) delete container and image in Docker desktop
- after triggering Docker build, upload image to ECR and updating Lambda:
  - test Lambda using `aws lambda invoke --function-name sentimental response.json`
