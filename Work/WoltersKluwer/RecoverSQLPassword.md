RecoverSQLPassword

# Recover SA Password from SQL Server databse

## Using SGL Server Management Studio

- Login to SQL Server database using Windows Authentication mode
- In Object Explorer, open Security > Logins. Right click on SA and select Properties
- Enter new password and click OK

## Using SQL Script

```sql
GO 
	ALTER LOGIN [sa] WITH DEFAULT_DATABASE=[master] 
GO 
	USE [master] 
GO 
	ALTER LOGIN [sa] WITH PASSWORD=N'NewPassword' MUST_CHANGE 
GO
```

Instead of NewPassword enter the desired password

Using SQL Password recorevy Tool

