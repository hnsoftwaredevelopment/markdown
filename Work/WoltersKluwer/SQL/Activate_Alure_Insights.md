Activate_Alure_Insights

```sql
USE Autor
GO

EXEC dba.i01_OPTIE @a_opt_id=101, @a_opt_oms='Alure Insights'

EXEC dba.i01_GEBRUIKERSTAAK @a_gbt_id=719, @a_gbt_oms='Alure Insights - Openen draaitabel', @a_gbt_app_id=3
EXEC dba.i01_FUNCTIE @a_fun_id=5957, @a_fun_oms='Alure Insights - Openen draaitabel', @a_fun_app_id=3
EXEC dba.i01_OBJECT @a_obj_id=51925, @a_obj_master='AlureInsights', @a_obj_control='OpenPivotTable' , @a_obj_app_id=3, @a_obj_oms='Alure Insights - Open pivottable', @a_obj_type='menuitem'

EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51925, @a_obg_fun_id=5957
EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5957, @a_fgb_gbt_id=719
EXEC dba.i01_OPTIE_GEBRUIK @a_opg_opt_id = 101, @a_opg_gbt_id = 719
EXEC dba.i01_GEBR_TAAK_GEBRUIK @a_gtg_gbt_id=719, @a_gtg_ggr_innolan_id=1
GO

IF EXISTS (SELECT 1 FROM OPTIE WHERE opt_id = 15)
BEGIN
  EXEC dba.i01_OBJECT @a_obj_id=51928, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau1' , @a_obj_app_id=3, @a_obj_oms='Organizationlevel 1 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51929, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau2' , @a_obj_app_id=3, @a_obj_oms='Organizationlevel 2 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51930, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau3' , @a_obj_app_id=3, @a_obj_oms='Organizationlevel 3 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51931, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau4' , @a_obj_app_id=3, @a_obj_oms='Organizationlevel 4 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51932, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau5' , @a_obj_app_id=3, @a_obj_oms='Organizationlevel 5 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51933, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau6' , @a_obj_app_id=3, @a_obj_oms='Organisationlevel 6 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51934, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau7' , @a_obj_app_id=3, @a_obj_oms='Organisationlevel 7 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51935, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau8' , @a_obj_app_id=3, @a_obj_oms='Organisationlevel 8 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51936, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau9' , @a_obj_app_id=3, @a_obj_oms='Organisationlevel 9 for Alure Insights', @a_obj_type='Column'
  EXEC dba.i01_OBJECT @a_obj_id=51937, @a_obj_master='UUR|AlureInsights', @a_obj_control='Organisatieniveau10', @a_obj_app_id=3, @a_obj_oms='Organisationlevel 10 for Alure Insights', @a_obj_type='Column'

  EXEC dba.i01_FUNCTIE @a_fun_id=5959, @a_fun_oms='Alure Insights alle organisatieniveau 1', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5960, @a_fun_oms='Alure Insights alle organisatieniveau 2', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5961, @a_fun_oms='Alure Insights alle organisatieniveau 3', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5962, @a_fun_oms='Alure Insights alle organisatieniveau 4', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5963, @a_fun_oms='Alure Insights alle organisatieniveau 5', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5964, @a_fun_oms='Alure Insights alle organisatieniveau 6', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5965, @a_fun_oms='Alure Insights alle organisatieniveau 7', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5966, @a_fun_oms='Alure Insights alle organisatieniveau 8', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5967, @a_fun_oms='Alure Insights alle organisatieniveau 9', @a_fun_app_id=3
  EXEC dba.i01_FUNCTIE @a_fun_id=5968, @a_fun_oms='Alure Insights alle organisatieniveau 10', @a_fun_app_id=3

  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51928, @a_obg_fun_id=5959
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51929, @a_obg_fun_id=5960
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51930, @a_obg_fun_id=5961
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51931, @a_obg_fun_id=5962
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51932, @a_obg_fun_id=5963
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51933, @a_obg_fun_id=5964
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51934, @a_obg_fun_id=5965
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51935, @a_obg_fun_id=5966
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51936, @a_obg_fun_id=5967
  EXEC dba.i01_OBJECT_GEBRUIK @a_obg_obj_id=51937, @a_obg_fun_id=5968

  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5959, @a_fgb_gbt_id=150
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5960, @a_fgb_gbt_id=151
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5961, @a_fgb_gbt_id=152
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5962, @a_fgb_gbt_id=153
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5963, @a_fgb_gbt_id=487
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5964, @a_fgb_gbt_id=488
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5965, @a_fgb_gbt_id=489
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5966, @a_fgb_gbt_id=490
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5967, @a_fgb_gbt_id=491
  EXEC dba.i01_FUNCTIE_GEBRUIK @a_fgb_fun_id=5968, @a_fgb_gbt_id=492
END
GO
```

