#!/bin/bash
set -eo pipefail

rm -f index.zip
cd lambda
zip -X -r ../index.zip *
cd ..
aws lambda update-function-code --function-name comprehend --zip-file fileb://index.zip