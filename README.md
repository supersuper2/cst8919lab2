# Azure Flask Login Monitoring Lab

Video Demo Link: https://youtu.be/6W0-18ZkHxI

## Lab Summary / What I Learned

In this lab, I built and deployed a Python Flask application to Azure Web App that includes a `/login` route designed to simulate successful and failed login attempts. Diagnostic logging was enabled and directed to a Log Analytics workspace, allowing the application logs to be queried using Kusto Query Language (KQL). I then created an alert rule in Azure Monitor that triggers when more than five failed login attempts occur within a five-minute window, and connected it to an action group that sends an email notification.

I continuted by deploying a Flask app using Azure CLI, how to configure App Service diagnostic settings to stream logs into Log Analytics, and how to write effective KQL queries for application monitoring. I also became familiar with setting up alert rules and action groups to automate incident detection and notification using Azure Monitor.

## Challenges Faced

One challenge was ensuring the Flask app would start correctly in Azure’s hosting environment. This required updating the `app.run()` method to bind to `0.0.0.0` and use the `PORT` environment variable provided by Azure. Another issue was that email notifications weren’t visible in some parts of the alert creation workflow, which I solved by creating the action group directly through Azure Monitor’s “Manage Actions” interface. Another minor issue that had occured was that sending the HTTP request might have taken some time, this could be due to many reasons.

## KQL Query with Explanation

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(1h)
| where ResultDescription has "Failed login attempt"
```
This query searches the App Service console logs for entries in the last 1 hour that contain the phrase "Failed login attempt". It filters and returns only those log messages that indicate failed login attempts, which are generated using app.logger.warning() in the Flask application. This Query was effective in find the failed login attempts, as it was directly searching for the keywords of the unsuccessful attempts.

## Real-World Improvements

To enhance this setup in a real-world environment, several improvements could be made. First, the login logging can be improved with metadata such as IP addresses, user-agent strings, and geolocation to provide better context and traceability. Implementing rate-limiting or CAPTCHA for repeated login attempts would help prevent any type of brute-force attacks. Instead of relying on basic keyword detection, more advanced pattern recognition (e.g., time-series anomaly detection) could be used to catch suspicious behavior.
