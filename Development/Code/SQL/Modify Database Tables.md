Modify Database Tables

# Modify Database Tables

# Table Columns

## Add Column
```SQL
ALTER TABLE table_name
	ADD COLUMN column_name column_type [NOT NULL] AFTER previous_column_name;
```
Instead of AFTER... you can use FIRST if the new column has to become the first column.

NOT NULL is optional if the column cannot be empty
column_type example: `VARCHAR(4)`


## Delete Column 
Select the Database by double clicking the database nd Enter:

```SQL
ALTER TABLE table_name
  DROP COLUMN column_name;
```

## Rename Column
```SQL
ALTER TABLE table_name
  RENAME COLUMN original_column_name TO new_column_name;
```

# Table's
## Add Table
```SQL
CREATE TABLE [IF NOT EXISTS] table_name(
   column_1_definition,
   column_2_definition,
   ...,
   table_constraints
) ENGINE=storage_engine;
```

## Delete Table
```SQL
DROP TABLE table_name;
```

## Rename Table
```SQL
ALTER TABLE table_name
  RENAME TO new_table_name;
```

