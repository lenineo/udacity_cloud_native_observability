**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![Alt text](./answer-img/svc_pods.PNG?raw=true "Optional Title")
## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![Alt text](./answer-img/grafana_main.PNG?raw=true "Optional Title")
## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![Alt text](./answer-img/prometheus_simple_dashboard.PNG?raw=true "Optional Title")

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
* SLO - 99% uptime in a given month. SLI - actual measurement of uptime in minutes to all minutes in month in percents.
* SLO - not more than 500ms per request/response. SLI - actual measurement of request response time for given request/response.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
* Latency - amount of time that the system responds to request
* Traffic - how many requests or sessions system can serve per second 
* Errors - how many requests returns errors
* Saturation - what is the overall percentage of CPU or disk in use
* Uptime - how many HTTP requests statuses have 2XX codes

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
![Alt text](./answer-img/general_grafana_dashboard_1.PNG?raw=true "Optional Title")
![Alt text](./answer-img/general_dash_2.PNG?raw=true "Optional Title")

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.
![Alt text](./answer-img/jaeger_span.PNG?raw=true "Optional Title")

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
![Alt text](./answer-img/jaeger_dash.PNG?raw=true "Optional Title")

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: Error: HTTP 500 internal error. Endpoint: /star

Date: November 30 2021

Subject: Call of /star to add star in post query return 500 error

Affected Area: Add star operation on backend

Severity: Critical

Description: When user try to add a new star he receives 500 server error.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.
* Latency 
* Errors 
* Uptime
## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.
* Latency not more than 500ms per request/response in 99% of cases per day
* Errors number of 500 errors/requests per day less than 0.05%
* Uptime >= 99.95% per day
* Amount of 20x responses not less than 99.95% per day
## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
* Jaeger duration tracing
* 50x errors/requests in 24 hours
* 40x errors/requests in 24 hours
* 20x code in requests in 34 hours
* Uptime by backend and frontend
![Alt text](./answer-img/final_sli_1.PNG?raw=true "Optional Title")
![Alt text](./answer-img/final_sli_2.PNG?raw=true "Optional Title")

