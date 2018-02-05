REST API wrapper for AWS comprehend.

Currently hosted at https://k20p04h3vi.execute-api.us-west-2.amazonaws.com/prod/comprehend on the primary "metaltoad" AWS account (831442996354).

To deploy code changes, make sure you have a valid access key in `~/.aws/credentials` and run `./publish.sh`.

Note -- at the time this code was written, the version of boto3 bundled with AWS lambda was out of date and didn't support the comprehend service, so it was necessary to install a copy of boto3 in the "lambda" folder before deploying. Unclear if this is still a problem -- refer to https://forums.aws.amazon.com/thread.jspa?messageID=817111.