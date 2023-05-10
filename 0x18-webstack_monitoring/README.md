# 0x18. Webstack monitoring

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)



![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)

## Resources

**Read or watch**:

-   [What is server monitoring](https://intranet.alxswe.com/rltoken/km_XUDAfXEBoXZQsIWEo5Q "What is server monitoring")
-   [What is application monitoring](https://intranet.alxswe.com/rltoken/z9jsikINjrsUo2QY5_Xz8g "What is application monitoring")
-   [System monitoring by Google](https://intranet.alxswe.com/rltoken/_8KIbIUNzMgKi_LiGMBWAw "System monitoring by Google")
-   [Nginx logging and monitoring](https://intranet.alxswe.com/rltoken/V3GsrDcMHPdgrizShj4RCg "Nginx logging and monitoring")


## Tasks

### 0. Sign up for Datadog and install datadog-agent

For this task head to  [https://www.datadoghq.com/](https://intranet.alxswe.com/rltoken/Ufs6rTHMET5LB1Uoylx0nw "https://www.datadoghq.com/")  and sign up for a free  `Datadog`  account. When signing up, you’ll have the option of selecting statistics from your current stack that  `Datadog`  can monitor for you. Once you have an account set up, follow the instructions given on the website to install the  `Datadog`  agent.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T044722Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ba80b00552e829725f11b8a4ff9f1e0d3f85942ed50fb50132cbcb2be1cc9fc1)

-   Sign up for Datadog -  **Please make sure you are using the US website of Datagog (.com)**
-   Install  `datadog-agent`  on  `web-01`
-   Create an  `application key`
-   Copy-paste in your Intranet user profile ([here](https://intranet.alxswe.com/rltoken/elXu5CcaGpeK7GxerBb7wQ "here")) your DataDog  `API key`  and your DataDog  `application key`.
-   Your server  `web-01`  should be visible in Datadog under the host name  `XX-web-01`
    -   You can validate it by using this  [API](https://intranet.alxswe.com/rltoken/5BtVPmgzhb96y7jZDGGHOQ "API")
    -   If needed, you will need to update the hostname of your server

### 1. Monitor some metrics

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some  `monitors`  within the  `Datadog`  dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here:  [System Check](https://intranet.alxswe.com/rltoken/4RPOEVDTqKXuvyU4Gkj2Bw "System Check").

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T044722Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=471eb8a93ffe2f6baf019f5023f72ce492da5559b409df9c3018bef864fe2891)

-   Set up a monitor that checks the number of read requests issued to the device per second.
-   Set up a monitor that checks the number of write requests issued to the device per second.

### 2. [Create a dashboard](./2-setup_datadog)

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

-   Create a new  `dashboard`
-   Add at least 4  `widgets`  to your dashboard. They can be of any type and monitor whatever you’d like
-   Create the answer file  `2-setup_datadog`  which has the  `dashboard_id`  on the first line.  **Note**: in order to get the id of your dashboard, you may need to use  [Datadog’s API](https://intranet.alxswe.com/rltoken/QhlPcQqUocwWcOkZ9s4mWQ "Datadog's API")
