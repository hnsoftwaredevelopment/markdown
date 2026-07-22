<% "---" %>
<%*
  const modalForm = app.plugins.plugins.modalforms.api;
  const result = await modalForm.openForm("DevNote", {
  "omit": [
  "Subject",
  "Project",
  "Date",
  "Note"
  ]
  });
  
-%>
<% "---" %>
{{Subject}}
{{Project}}
{{Date}}
{{Note}}
