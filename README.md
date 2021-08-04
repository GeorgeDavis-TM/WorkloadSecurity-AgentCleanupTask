# WorkloadSecurity-AgentCleanupTask

Manually force cleanup of agents on Trend Micro Cloud One Workload Security via APIs

> :warning: **Note:** This script is used to force manual cleanup on Cloud One Workload Security. For automated tasks, refer to Workload Security documentation on [Inactive Agent Cleanup](https://cloudone.trendmicro.com/docs/workload-security/agent-clean-up-inactive/)

## Setup Instructions

Step 1: Create a Cloud One Workload Security API Key. Refer to the Workload Security documentation for steps to create this API key - https://cloudone.trendmicro.com/docs/workload-security/api-send-request/#create-an-api-key

Step 2: Setup the Cloud One Workload Security API key in the `config.json` file and the target Agent status to cleanup. In this example, we use `Activation Failed`.

Step 3: Run the Python script `python3 workloadsecurity_agentcleanuptask.py`
