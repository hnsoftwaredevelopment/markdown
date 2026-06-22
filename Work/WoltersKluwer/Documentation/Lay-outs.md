Lay-outs

# Data Binding Modes

The Report Designer uses one of the following modes to provide dynamic content to your reports: expression bindings or standard data bindings.

## Expression Bindings

Expression bindings enable you to use complex [expressions](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/use-expressions.html) that include two or more fields and various functions. Expressions also allow you to calculate complex summaries without scripts and conditionally shape your data without formatting rules.

This mode is enabled in the Report Designer if the [Property Grid](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/report-designer-tools/ui-panels/property-grid.html) provides the **PropertyName Expression** option in property markers' context menu.

![img](assets/eurd-win-property-grid-data-binding.png)

## Data Bindings

Standard data bindings enable you to assign a single data field to a report control or use [report scripts](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/use-report-scripts.html) to provide custom logic.

This mode is enabled in the Report Designer if the [Property Grid](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/report-designer-tools/ui-panels/property-grid.html) does not provide the **PropertyName Expression** option in property markers' context menu.

![img](assets/eurd-win-property-grid-data-bindings-mode.png)

## Conversion Dialog

The following dialog appears only when [expression bindings](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/data-binding-modes.html#expressions) are enabled in the Report Designer, and you [open an existing report](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/open-reports.html) that uses standard [data bindings](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/data-binding-modes.html#databindings):

![img](assets/eurd-win-bindings-to-expressions-conversion-dialog.png)

This dialog prompts you to convert your report to use expressions (the new binding mechanism). Click **Yes** to run the report conversion, click **No** to open the report without changes.

See the section below for information on how to use expressions instead of data bindings.

## Binding Mode Comparison

### **Bind to a Single Data Field**

- The [Field List](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/report-designer-tools/ui-panels/field-list.html) panel allows you to drop fields onto the design surface or existing report controls. All binding ways are identical in the **data bindings** and **expression bindings** modes.

  ![img](assets/eurd-win-binding-using-field-list.png)

- The control's smart tag enables you to select the target data field in the corresponding drop-down list.

  | Expression Bindings                                      | Data Bindings                                      |
  | :------------------------------------------------------- | :------------------------------------------------- |
  | ![img](assets/eurd-win-smart-tag-expression-binding.png) | ![img](assets/eurd-win-smart-tag-data-binding.png) |

- You can select a report control and bind it to data in the [Property Grid](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/report-designer-tools/ui-panels/property-grid.html).

  | Expression Bindings                                          | Data Bindings                                                |
  | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | Click the **Text** property's marker and choose the **Text Expression** item. Specify an expression in the invoked Expression Editor.![img](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/images/eurd-win-property-grid-data-binding.png) | Expand the **(Data Bindings)** group in the **Data** tab and assign a data field to the **Text**property.![img](assets/eurd-win-property-grid-text-data-binding.png) |

See the following topics for more information:

- [Bind Report Controls to Data (Expression Bindings)](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/bind-controls-to-data-expression-bindings.html)
- [Bind Report Controls to Data (Data Bindings)](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/bind-controls-to-data-data-bindings.html)

### **Bind to Multiple Data Fields**

| Expression Bindings                                          | Data Bindings                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Use the [mail merge](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/use-embedded-fields-mail-merge.html) functionality.![img](assets/eurd-win-binding-modes-mail-merge.png)Click the **Expression** property's ellipsis button and specify the expression.![img](assets/eurd-win-expression-binding-multiple-fields.png) | Use the [mail merge](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/bind-to-data/use-embedded-fields-mail-merge.html) functionality.![img](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/images/eurd-win-binding-modes-mail-merge.png) |

### **Calculate Summary**

| Expression Bindings                                          | Data Bindings                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Select the summary function in the **Expression Editor**'s **Summary** section.All functions has the 'sum' prefix.![img](assets/eurd-win-expression-binding-summary-function.png)See [Calculate a Summary](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-expression-bindings/calculate-a-summary.html) for more information. | Select the summary function in the **Summary Func**drop-down list.![img](assets/eurd-win-data-binding-summary-function.png)See [Calculate a Summary](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-data-bindings/calculate-a-summary.html) for more information. |

### **Complex Bindings, Custom Summary**

| Expression Bindings                                          | Data Bindings                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Use the **Expression Editor** to construct an [expression](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/use-expressions.html) of any complexity.![img](assets/eurd-win-label-advanced-summary-expression.png)Refer to [Calculate an Advanced Summary](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-expression-bindings/calculate-an-advanced-summary.html) for an example. | Use [report scripts](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/use-report-scripts.html).Refer to [Calculate a Custom Summary](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-data-bindings/calculate-a-custom-summary.html)for an example. |

### **Conditionally Customize Appearance**

| Expression Bindings                                          | Data Bindings                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Use the **Expression Editor** to construct [expressions](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/use-expressions.html) for a control's appearance and style properties.![img](assets/eurd-win-shaping-style-name-expression.png)Refer to [Conditionally Change a Control Appearance](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-expression-bindings/conditionally-change-a-control-appearance.html) for an example. | Create formatting rules and assign them to report controls.![img](assets/eurd-win-shaping-formattin-rule-appearance-settings.png)Refer to [Conditionally Change a Control Appearance](https://devexpress.github.io/dotnet-eud/interface-elements-for-desktop/articles/report-designer/report-designer-for-winforms/shape-report-data/shape-data-data-bindings/conditionally-change-a-control-appearance.html)for an example. |