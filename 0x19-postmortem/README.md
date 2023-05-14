Date: 05/08/2023

<img src="./ha.jpg" />

Summary:

On 05/07/2023, our API service went down due to an issue with our host provider's inability to store environment variables. This resulted in the API being unable to retrieve the necessary environment variables required for its operation.

Timeline of Events:

- At 05/07/2023, we discovered that our API service was down.
- After investigating, we found that the issue was related to our host provider's inability to store environment variables.
- We attempted to restart the service but were unsuccessful as the environment variables were not persisted.
- As a workaround, we created an .env file with all the necessary environment variables and had the API consume these variables from the file.
- At 05/08/2023, the service was successfully restarted and the API was back online.

Root Cause:

The root cause of the service outage was due to our host provider's inability to store environment variables which prevented our API from retrieving the necessary variables required for its operation.

Resolution and Recovery:

To resolve the issue, we created an .env file containing all the necessary environment variables and had the API consume these variables from the file. This allowed us to successfully restart the service and bring the API back online.

Next Steps:

Going forward, we will investigate alternative solutions for securely storing sensitive data such as passwords or API keys. We will also evaluate other host providers that can properly store environment variables to prevent similar incidents from occurring in the future.

Lessons Learned:

- It's important to have backup plans and workarounds in place in case of unexpected service outages.
- Environment variables should be stored securely and not accessible to unauthorized users.
- It's important to evaluate host providers carefully to ensure they can meet our service requirements.
- We should document and communicate any outages or incidents to all stakeholders in a timely manner.
