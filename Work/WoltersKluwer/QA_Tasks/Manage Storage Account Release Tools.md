Manage Storage Account Release Tools

# Manage Storage Account Release Tools

## How to use
- Install the task in your Azure Devops account by navigating to the marketplace and click install. Select the Azure Devops account where the task will be deployed to.
- Add the task to your release by clicking in your release on add a task. Click the Add button on the Create Storage Account task.
- Configure task.
- On release run the storage account and/or table will be created if not exist.

## 1. Create Storage Account
Provides a possibility to create storage account and a single table on a Release pipeline, before application deployment.

**Configure the task.**
![a08a848928d826cd33e0fcb7054ba1ab.png](attachments/e36264f63f31495caffb0c8980f50dbf.png)

- Select an AzureRM subscription connection - use service principal scoped to one resource group
- Set the storage account name, if not exist it will be created
- Select a location from a dropdown list, if not selected will be inherited from resource group
- Select Sku
- Set the table name if you want to create a table in newly created storage account

## 2. Add Storage Account's connection string to Key Vault

Want to be sure that connection string to your storage account is securely stored in key vault? This task will help.
Configure the task.

![6f291e4894c095e69b32e71293fae8f1.png](attachments/5f91dd67a23e49f5989c45bbad560a0e.png)

- Select an AzureRM subscription connection - use service principal scoped to one resource group
- Set the storage account name, which connection string you want to store
- Set key vault name, if not exist it will be created
- Set key name
- Select a location from a dropdown list, if not selected will be inherited from resource group

## 3. Seed Table Storage from given json file

Enable seeding table storage from a given json file. File should look like below:

```YAML
[
    {
        "PartitionKey": "Partition1",
        "RowKey": "SomeGuid1",
        "CustomColumn": "Values1"
        ...
    },
    {
        "PartitionKey": "Partition2",
        "RowKey": "SomeGuid2",
        "CustomColumn": "Values2"
        ...
    }
    ...
]
```

Task support flat key/value list, only.

**Configure the task.**

![a4fe39e0cdd6c336123af61c17ea6a1a.png](attachments/f6596890ce58402cb3b05009981a9d70.png)
- Select an AzureRM subscription connection - use service principal scoped to one resource group
- Set the storage account name, which you want to seed
- Set the table name, which you want to seed
- Select Json File path, it should be made of a list of flat key / value objects, PartitionKey and RowKey are required
- Set Update Row On Conflict if row should be override

## 4. Override json config file with release variables
Based on existing environment variables on release agent, overwrite json file properties with the same name. Setting prefix is optional. Environment variables on an Azure DevOps are set on configuring release in a variables tab, or linked from variable group.

**Configure the task.**
![e39a4a1a482756437d38009effc361ae.png](attachments/49d2508cf5d547f1aa732ce6b79046a4.png)

- Select Json File path, it should be made of a list of flat key / value objects, PartitionKey and RowKey are required
- Optionally set prefix by which variables will be selected