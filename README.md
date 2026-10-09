# AWS Lambda Layers with Python

Python code for a practical AWS Lambda Layers lab. The shared Layer contains the `requests` dependency and `shared_utils.py`; the Lambda deployment packages contain only their handler modules.

## Files

- `shared_utils.py`: shared response, validation, and logging helpers.
- `process_order.py`: order-processing Lambda handler.
- `validate_customer.py`: customer-validation Lambda handler.
- `requirements.txt`: pinned dependency version for repeatable builds.
- `article-lambda-layers.md`: Portuguese blog article and walkthrough.

## Runtime

The commands in the article use Python 3.12 and the `us-east-1` region. Ensure your AWS CLI profile has the required Lambda and IAM permissions before running them.
