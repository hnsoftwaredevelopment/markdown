<% "---" %>
<%*
  const modalForm = app.plugins.plugins.modalforms.api;
  const result = await modalForm.openForm("DevNote");
  
-%>
<% "---" %>
![](Epic-1.svg)  
#Developer Note: <% result.get("Project") %> / <% result.get("Date") %>

*Subject:*
<% result.get("Subject") %>

*Notes:*
---
<% result.get("Note") %>

