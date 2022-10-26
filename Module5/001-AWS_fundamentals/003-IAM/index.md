# Lesson

IAM (Identity Access Management) enables you to manage AWS services and resources securely. 
You can create users and groups, edit and modify the permissions to deny / allow access

Currently using IAM roles with permissions, you don't have permissions to create new users or change permissions though

IAM works on 'least privilege' permissions where each user has the minimum permissions required to do their job. 

Users - A set of permissions and credentials for a 'person' to use
Groups - A set of users under one set of permissions
Roles - Grant specific permissions to a resource / person for a set duration of time, can be authenticated by AWS (generally a service)

User - has access permanently with set credentials or authentication while a role has temp credentials to do the specific thing