# aws-track-us-visa-dates
Script to check us travel docs website to get alert when the available dates are in range.

Whenevr dates will change and number of days will come down only then the script will publish msg to sns topic.

# How to use

1. install python and boto3
2. create aws access keys and configure them
3. create sns topic and subscribe to it
Put the details and run this py script - set it in crontab or schedule it with your env. ex(Every 30 mins)
