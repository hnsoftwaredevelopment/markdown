
> Officiële Git-spiekbriefje van GitHub Education — vertaald naar het Nederlands

Git is het open source gedistribueerde versiebeheersysteem dat GitHub-activiteiten op je laptop of desktop mogelijk maakt. Dit spiekbriefje geeft een overzicht van de meest gebruikte Git-opdrachten.

## Inhoudsopgave

- [Installeren](#Installeren)
- [Configuratie](#Configuratie)
- [Branches](#Branches)
- [Aanmaken & Klonen](#Aanmaken%20&%20Klonen)
- [Wijzigingen bijhouden](#Wijzigingen%20bijhouden)
- [Wijzigingen ongedaan maken](#Wijzigingen%20ongedaan%20maken)
- [Fragmenten opslaan](#Fragmenten%20opslaan)
- [Bestanden uitsluiten](#Bestanden%20uitsluiten)
- [Geschiedenis bekijken](#Geschiedenis%20bekijken)
- [Synchroniseren](#Synchroniseren)
- [Bestanden verwijderen & verplaatsen](#Bestanden%20verwijderen%20&%20verplaatsen)
- [Tags](#Tags)
- [Meer leren](#Meer%20leren)

---
## Installeren

GitHub biedt desktopcliënts met een grafische interface voor de meest voorkomende acties. Voor gevanceerde scenario's is er een automatisch bijgewerkte opdrachtregel-versie van Git inbegrepen.

- **GitHub Desktop voor Mac en Windows** — [desktop.github.com](https://desktop.github.com/)
- **Git-distributies voor Linux en POSIX** — [git-scm.com](https://git-scm.com/)

---
## Configuratie

Stel gebruikersinformatie in voor alle lokale repositories.

```bash
git config --global user.name "[naam]"
```

Stel de naam in die zichtbaar is bij commits.

```bash
git config --global user.email "[e-mailadres]"
```

Stel het e-mailadres in dat gekoppeld wordt aan commits.

```bash
git config --global color.ui auto
```

Schakel handige kleurweergave in de opdrachtregel in.

---
## Branches

Branches zijn een belangrijk onderdeel van werken met Git. Elke commit bevindt zich op een branch en je kunt heen en weer schakelen tussen branches.

```bash
git branch
```

Toont alle lokale branches in de huidige repository.

```bash
git branch [naam-branch]
```

Maakt een nieuwe branch aan.

```bash
git branch -d [naam-branch]
```

Verwijdert de opgegeven branch.

```bash
git checkout [naam-branch]
```

Schakelt over naar de opgegeven branch en werkt de werkdirectory bij.

```bash
git checkout -b [naam-branch]
```

Maakt een nieuwe branch aan en schakelt er direct naartoe over.

```bash
git merge [naam-branch]
```

Voegt de geschiedenis van de opgegeven branch samen met de huidige branch.

---
## Aanmaken & Klonen

Start een nieuw repository of haal er een op uit een bestaande URL.

```bash
git init [projectnaam]
```

Maakt een nieuw lokaal repository aan met de opgegeven naam.

```bash
git clone [url]
```

Downloadt een project inclusief de volledige versiegeschiedenis.

---
## Wijzigingen bijhouden

Bekijk bestanden en voer staging-acties uit als onderdeel van een commit.

```bash
git status
```

Toont alle nieuwe of gewijzigde bestanden die nog niet zijn gecommit.

```bash
git diff
```

Toont de nog niet ge-stagede bestandswijzigingen.

```bash
git add [bestand]
```

Maakt een bestand klaar voor commit (staged).

```bash
git add .
```

Staged alle gewijzigde en nieuwe bestanden in de werkdirectory.

```bash
git diff --staged
```

Toont de bestandsverschillen tussen staging en de laatste bestandsversie.

```bash
git reset [bestand]
```

Haalt een bestand uit de staging area, zonder de inhoud te wijzigen.

```bash
git commit -m "[beschrijving]"
```

Slaat de gestagede bestanden permanent op in de versiegeschiedenis.

---
## Wijzigingen ongedaan maken

Verwijder fouten en herstel de geschiedenis.

```bash
git reset [commit]
```

Zet alle commits terug na `[commit]`, maar bewaart lokale wijzigingen.

```bash
git reset --hard [commit]
```

Gooit alle geschiedenis en wijzigingen weg tot aan de opgegeven commit.

```bash
git revert [commit]
```

Maakt alle wijzigingen van de opgegeven commit ongedaan via een nieuwe commit (veiliger dan reset voor gedeelde branches).

> ⚠️ **Let op:** `git reset --hard` verwijdert commits permanent. Gebruik `git revert` voor gedeelde branches om de geschiedenis intact te houden.

---
## Fragmenten opslaan

Sla tijdelijk onafgemaakte wijzigingen op en herstel ze later.

```bash
git stash
```

Slaat alle gewijzigde bijgehouden bestanden tijdelijk op.

```bash
git stash list
```

Toont alle opgeslagen stashes.

```bash
git stash pop
```

Zet de meest recent opgeslagen bestanden terug.

```bash
git stash drop
```

Verwijdert de meest recent opgeslagen stash.

---
## Bestanden uitsluiten

Voorkom onbedoeld committen van tijdelijke of persoonlijke bestanden.

```
*.log
build/
temp-*
```

Sla een bestand op met de naam `.gitignore` en gebruik globbing-patronen om te voorkomen dat onbedoelde bestanden worden bijgehouden. Voeg dit bestand toe aan je repository zodat het voor iedereen geldt.

```bash
git ls-files --other --ignored --exclude-standard
```

Toont alle genegeerde bestanden in dit project.

---
## Geschiedenis bekijken

Bekijk de evolutie van projectbestanden.

```bash
git log
```

Toont de versiegeschiedenis van de huidige branch.

```bash
git log --follow [bestand]
```

Toont de versiegeschiedenis van een bestand, inclusief hernoemingen.

```bash
git log --pretty=format:"%h %s" --graph
```

Toont de commit-geschiedenis als ASCII-grafiek met branches en samenvoegingen.

```bash
git diff [eerste-branch]...[tweede-branch]
```

Toont de inhoudsverschillen tussen twee branches.

```bash
git show [commit]
```

Toont de metadata en inhoudswijzigingen van de opgegeven commit.

---
## Synchroniseren

Registreer een externe repository (URL) en wissel versiegeschiedenis uit.

```bash
git fetch [remote]
```

Downloadt alle geschiedenis van de remote repository.

```bash
git merge [remote]/[branch]
```

Voegt de remote branch samen met de huidige lokale branch.

```bash
git push [remote] [branch]
```

Uploadt alle commits van de lokale branch naar GitHub.

```bash
git push [remote] --delete [branch]
```

Verwijdert een remote branch.

```bash
git pull
```

Downloadt de geschiedenis en voegt wijzigingen samen (`fetch` + `merge` gecombineerd).

---
## Bestanden verwijderen & verplaatsen

Verwijder bijgehouden bestanden uit de project-index.

```bash
git rm [bestand]
```

Verwijdert het bestand uit de werkdirectory en staged de verwijdering.

```bash
git rm --cached [bestand]
```

Verwijdert het bestand uit de versiebeheer maar bewaart het lokaal.

```bash
git mv [origineel-bestand] [hernoemd-bestand]
```

Hernoemt het bestand en staged de hernoeming voor commit.

---
## Tags

```bash
git tag [tagnaam]
```

Markeert de huidige commit met een tag (handig voor releases, bv. `v1.0.0`).

```bash
git tag -a [tagnaam] -m "[beschrijving]"
```

Maakt een geannoteerde tag aan met een beschrijving.

```bash
git push origin [tagnaam]
```

Pusht een tag naar de remote repository.

```bash
git push origin --tags
```

Pusht alle lokale tags naar de remote repository.

---
## Meer leren

- **Pro Git** — volledig gratis boek (NL deels beschikbaar): [git-scm.com/book](https://git-scm.com/book/nl/v2)
- **GitHub Documentatie**: [docs.github.com](https://docs.github.com/)
