<%*
  const modalForm = app.plugins.plugins.modalforms.api;
  const result = await modalForm.openForm("DevNote");

  if (result) {
    // Haal de gegevens op (werkt direct via result.Veldnaam)
    const project = result.Project || "Geen Project";
    const date = result.Date || "Geen Datum";
    const subject = result.Subject || "";
    const note = result.Note || "";

    // Maak de projectnaam veilig voor Windows/Mac bestandsnamen
    const cleanProject = project.replace(/[\\/:*?"<>|]/g, "-");

    // Hernoem het bestand direct
    await tp.file.rename(`Developer Note ${cleanProject} - ${date}`);

    // Bouw de volledige inhoud van je notitie op via tR
    tR += `---\n`;
    tR += `Subject: ${subject}\n`;
    tR += `Project: ${project}\n`;
    tR += `Date: ${date}\n`;
    tR += `---\n`;
    tR += `![](Epic-1.svg)  \n`;
    tR += `# Developer Note ${project} - ${date}\n\n`;
    tR += `**Subject:**\n${subject}\n\n`;
    tR += `**Notes:**\n`;
    tR += `------\n`;
    tR += `${note}\n`;
  }
-%>
