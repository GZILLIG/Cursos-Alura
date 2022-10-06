CREATE TABLE [dbo].[Dim_Cliente]
(
	[Cod_Cliente] NVARCHAR(50) NOT NULL PRIMARY KEY,
	[Desc_Cliente] NVARCHAR(200),
	[Cod_Cidade] NVARCHAR(50),
	[Desc_Cidade] NVARCHAR(200),
	[Cod_Estado] NVARCHAR(50),
	[Desc_Estado] NVARCHAR(200),
	[Cod_Regiao] NVARCHAR(50),
	[Desc_Regiao] NVARCHAR(200),
	[Cod_Segmento] NVARCHAR(50),
	[Desc_Segmento] NVARCHAR(200)
)
