﻿/*
Deployment script for DW_SUCOS

This code was generated by a tool.
Changes to this file may cause incorrect behavior and will be lost if
the code is regenerated.
*/

GO
SET ANSI_NULLS, ANSI_PADDING, ANSI_WARNINGS, ARITHABORT, CONCAT_NULL_YIELDS_NULL, QUOTED_IDENTIFIER ON;

SET NUMERIC_ROUNDABORT OFF;


GO
:setvar DatabaseName "DW_SUCOS"
:setvar DefaultFilePrefix "DW_SUCOS"
:setvar DefaultDataPath "C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\"
:setvar DefaultLogPath "C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\"

GO
:on error exit
GO
/*
Detect SQLCMD mode and disable script execution if SQLCMD mode is not supported.
To re-enable the script after enabling SQLCMD mode, execute the following:
SET NOEXEC OFF; 
*/
:setvar __IsSqlCmdEnabled "True"
GO
IF N'$(__IsSqlCmdEnabled)' NOT LIKE N'True'
    BEGIN
        PRINT N'SQLCMD mode must be enabled to successfully execute this script.';
        SET NOEXEC ON;
    END


GO
USE [$(DatabaseName)];


GO
IF EXISTS (SELECT 1
           FROM   [master].[dbo].[sysdatabases]
           WHERE  [name] = N'$(DatabaseName)')
    BEGIN
        ALTER DATABASE [$(DatabaseName)]
            SET ANSI_NULLS ON,
                ANSI_PADDING ON,
                ANSI_WARNINGS ON,
                ARITHABORT ON,
                CONCAT_NULL_YIELDS_NULL ON,
                QUOTED_IDENTIFIER ON,
                ANSI_NULL_DEFAULT ON,
                CURSOR_DEFAULT LOCAL 
            WITH ROLLBACK IMMEDIATE;
    END


GO
IF EXISTS (SELECT 1
           FROM   [master].[dbo].[sysdatabases]
           WHERE  [name] = N'$(DatabaseName)')
    BEGIN
        ALTER DATABASE [$(DatabaseName)]
            SET PAGE_VERIFY NONE 
            WITH ROLLBACK IMMEDIATE;
    END


GO
ALTER DATABASE [$(DatabaseName)]
    SET TARGET_RECOVERY_TIME = 0 SECONDS 
    WITH ROLLBACK IMMEDIATE;


GO
IF EXISTS (SELECT 1
           FROM   [master].[dbo].[sysdatabases]
           WHERE  [name] = N'$(DatabaseName)')
    BEGIN
        ALTER DATABASE [$(DatabaseName)]
            SET QUERY_STORE (QUERY_CAPTURE_MODE = ALL, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 367), MAX_STORAGE_SIZE_MB = 100) 
            WITH ROLLBACK IMMEDIATE;
    END


GO
PRINT N'Rename refactoring operation with key b6ecd465-7dc9-4f57-8683-e2a4bd35d89d is skipped, element [dbo].[Dim_Fabrica].[Cod_Fabrica] (SqlSimpleColumn) will not be renamed to 123';


GO
PRINT N'Rename refactoring operation with key 89f1c528-b76a-4e9c-b0de-6d670f23b406 is skipped, element [dbo].[Dim_Fabrica].[Id] (SqlSimpleColumn) will not be renamed to Cod_Fabrica';


GO
PRINT N'Rename refactoring operation with key 368fe56a-8102-43e2-8b57-6efab90a3b0b is skipped, element [dbo].[Dim_Fabrica].[123] (SqlSimpleColumn) will not be renamed to Desc_Fabrica';


GO
PRINT N'Creating Table [dbo].[Dim_Fabrica]...';


GO
CREATE TABLE [dbo].[Dim_Fabrica] (
    [Cod_Fabrica]  NVARCHAR (50)  NOT NULL,
    [Desc_Fabrica] NVARCHAR (200) NULL,
    PRIMARY KEY CLUSTERED ([Cod_Fabrica] ASC)
);


GO
-- Refactoring step to update target server with deployed transaction logs

IF OBJECT_ID(N'dbo.__RefactorLog') IS NULL
BEGIN
    CREATE TABLE [dbo].[__RefactorLog] (OperationKey UNIQUEIDENTIFIER NOT NULL PRIMARY KEY)
    EXEC sp_addextendedproperty N'microsoft_database_tools_support', N'refactoring log', N'schema', N'dbo', N'table', N'__RefactorLog'
END
GO
IF NOT EXISTS (SELECT OperationKey FROM [dbo].[__RefactorLog] WHERE OperationKey = 'b6ecd465-7dc9-4f57-8683-e2a4bd35d89d')
INSERT INTO [dbo].[__RefactorLog] (OperationKey) values ('b6ecd465-7dc9-4f57-8683-e2a4bd35d89d')
IF NOT EXISTS (SELECT OperationKey FROM [dbo].[__RefactorLog] WHERE OperationKey = '89f1c528-b76a-4e9c-b0de-6d670f23b406')
INSERT INTO [dbo].[__RefactorLog] (OperationKey) values ('89f1c528-b76a-4e9c-b0de-6d670f23b406')
IF NOT EXISTS (SELECT OperationKey FROM [dbo].[__RefactorLog] WHERE OperationKey = '368fe56a-8102-43e2-8b57-6efab90a3b0b')
INSERT INTO [dbo].[__RefactorLog] (OperationKey) values ('368fe56a-8102-43e2-8b57-6efab90a3b0b')

GO

GO
PRINT N'Update complete.';


GO
