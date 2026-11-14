#!/usr/bin/env python3
"""Classify RC commits by machine relevance and functional area.

Usage: python3 rc_classify.py <commits.txt> <numstat.txt> <out.json>
commits.txt: git log <base>..<rc> --no-merges --name-only --format='@@@%H|%h|%cI|%an|%s'
numstat.txt: git diff --numstat --no-renames <base> <rc>
"""
import json, re, sys
from collections import defaultdict

ALL = ["V630", "V631", "V633", "VB Standard", "WB Standard + Probe Truck", "VB 1040/1250"]
DRILL = ["V630", "V631", "V633"]
SAW = ["VB Standard", "WB Standard + Probe Truck", "VB 1040/1250"]

# (regex on path or subject, machines, area). First match per file wins, so specific rules go first.
RULES = [
    # out of scope product lines
    (r"fabricator|/Fab[A-Z]|FabXml|V912|V35X|V353|LARS|V807|V808|V80x|V623|Transport_V623|"
     r"Laser|Plasma|Robot|Manipulator|ProfileCutter|Punch|Shear|ShotBlaster|PaintDry|"
     r"CuttingUnit|V310|V325|V304|V303|V210|NozzleHandler|GasController|ChainLifter|Trolley|"
     r"MoveableScanner|AutomaticPlateMeasurer|Chiller|LoadingCrane|InterpolationManager|"
     r"KinematicTransformation|Machine\.Robotics|Machine\.Plates|WeldAssemblies|PathValidation|"
     r"ImprintUnit|MovableConveyor", [], "Out of scope"),
    # tests, docs, build: no machine behaviour
    (r"^(docs/|\.github/|vacam/Tests/|twincat/test/|twincat/UnitTest|twincat/BDD|twincat/TestDriver|twincat/src/UnitTest)", [], "Test/Docs/Build"),
    (r"TranslationResources|\.resx$|phrase", ALL, "Translations / UI text"),
    # machine specific
    (r"ProbeTruck|V100StandAlone", ["WB Standard + Probe Truck"], "Probe truck / standalone saw"),
    (r"SawFixedRotatableTable|VB_?Standard", ["VB Standard", "WB Standard + Probe Truck"], "Saw (fixed rotatable table)"),
    (r"Saw/OldStyle|E_SawType|VBS?1x50|VB1[0-9]50", ["VB 1040/1250"], "Saw (VB1050/1250 old style)"),
    (r"Saw|SawBand|ShortPieceRemover", SAW, "Saw shared"),
    (r"V630", ["V630"], "Drill V630"),
    (r"V631", ["V631"], "Drill V631"),
    (r"V633|Suhner", ["V633"], "Drill V633"),
    (r"Main Objects/Drill_V2|ToolClamp", ["V631", "V633"], "Drill V2 (V631/V633)"),
    (r"Main Objects/Drill/|DrillZone|DrillChanger|Drill", DRILL, "Drill shared"),
    # shared core, affects every machine
    (r"twincat/src/.*(Safety|DoorControl|SystemControl|Collision)|vacam/.*Collision", ALL, "Safety / collision"),
    (r"twincat/src/-MAIN/ApplicationConfiguration|MachineHardCoded|_Global Variables|Migrat|Upgrade|"
     r"VacamInstaller|Voortman\.Backups|Voortman\.Settings|VersionCheck|MachineConfiguration", ALL, "Configuration / upgrade"),
    (r"Transport|Conveyor|RollerConveyor|MaterialClamp|Clamp|MeasureUnit|MeasureRoll|DisplacementSensor|Carriage", ALL, "Material transport / measuring"),
    (r"CycleList|Cyclelist|Command|Interpreter|ProcessController|Automatic", ALL, "Cycle list / process control"),
    (r"^twincat/src/|^twincat/MachineControl", ALL, "PLC core"),
    (r"^vacam/", ALL, "VACAM application"),
]
RULES = [(re.compile(p, re.I), m, a) for p, m, a in RULES]
OUT_PREFIXES = {"FAB", "MCPL", "V35X", "V353", "SYS", "DEVOPS", "TST"}
MACHINE_SPECIFIC_AREAS = {"Probe truck / standalone saw", "Saw (fixed rotatable table)", "Saw (VB1050/1250 old style)",
                          "Saw shared", "Drill V630", "Drill V631", "Drill V633", "Drill V2 (V631/V633)", "Drill shared"}
# Other teams' machines, used for the BT1 "Other team alerts" note. First match wins.
OTHER_MACHINES = [
    (r"Fabricator|/Fab[A-Z]|FabXml|WeldAssemblies|Machine\.Robotics|ChainLifter|Trolley", "Fabricator"),
    (r"V912", "V912 profile laser"),
    (r"V35X|V353|LARS|Machine\.Plates|LaserHead|LaserSource|LaserBeam|NozzleHandler|NozzlePositioner|GasController|Chiller", "V353 plate laser"),
    (r"V807|V808|V80x|Plasma|ProfileCutter|Manipulator|Robot", "V807/V808 coping robot"),
    (r"V623|Transport_V623|SawIntegratedShortPieceRemover|ToolStorage|ToolManipulator|MaterialPusher|OutfeedTable", "V623"),
    (r"V310|V304|V303|V210|CuttingUnit|Punch|Shear|AutomaticPlateMeasurer|MoveableScanner", "Plate machines (V30x/V310/V210)"),
    (r"V325|Carousel/", "V325"),
    (r"V613", "V613"),
    (r"ShotBlaster|VSB|PaintDry|Primer|InkJet|ImprintUnit|V704", "Blasting/marking (VSB, VP, V704)"),
    (r"LoadingCrane|V3000|VCT|TranverseTransport|LoadingPanel", "Material handling (V3000/VCT/crane)"),
    (r"InterpolationManager|KinematicTransformation|PathValidation", "CNC/robot motion (laser, coping)"),
]
OTHER_MACHINES = [(re.compile(p, re.I), n) for p, n in OTHER_MACHINES]
ALERT_PREFIX = "BT1"
HIGH_IMPACT = {"Safety / collision", "Configuration / upgrade", "Cycle list / process control"}
KEY_RE = re.compile(r"\b(BT1|BT2|SWMS|TST|FAB|V35X|MCPL|SYS|DEVOPS)-\d+\b", re.I)


def classify(path):
    for rx, machines, area in RULES:
        if rx.search(path):
            return machines, area
    return [], "Other"


def main(commits_path, numstat_path, out_path):
    churn = {}
    for line in open(numstat_path, encoding="utf-8-sig"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) == 3:
            a, d, p = parts
            churn[p] = (int(a) if a.isdigit() else 0) + (int(d) if d.isdigit() else 0)

    commits, cur = [], None
    for line in open(commits_path, encoding="utf-8-sig"):
        line = line.rstrip("\n")
        if line.startswith("@@@"):
            h, sh, date, author, subj = line[3:].split("|", 4)
            cur = {"hash": h, "short": sh, "date": date, "author": author, "subject": subj, "files": []}
            commits.append(cur)
        elif line.strip() and cur is not None:
            cur["files"].append(line.strip())

    areas = defaultdict(lambda: {"commits": set(), "files": set(), "machines": set(), "tickets": set(), "churn": 0})
    machine_hits = defaultdict(lambda: {"commits": set(), "areas": set(), "tickets": set()})
    relevant = []
    for c in commits:
        keys = sorted({m.group(0).upper() for m in KEY_RE.finditer(c["subject"])})
        c["tickets"] = keys
        c_machines, c_areas = set(), set()
        other_line = bool(keys) and all(k.split("-")[0] in OUT_PREFIXES for k in keys)
        c["other_line"] = other_line
        for f in c["files"]:
            ms, area = classify(f)
            if not ms:
                continue
            if other_line and area not in MACHINE_SPECIFIC_AREAS:
                continue
            c_machines.update(ms); c_areas.add(area)
            A = areas[area]
            A["commits"].add(c["short"]); A["machines"].update(ms); A["tickets"].update(keys)
            if f not in A["files"]:
                A["files"].add(f); A["churn"] += churn.get(f, 0)
        # subject can name a machine even if the path does not
        for rx, ms, area in RULES[3:12]:
            if rx.search(c["subject"]) and not other_line:
                c_machines.update(ms)
        if c_machines:
            c["machines"], c["areas"] = sorted(c_machines), sorted(c_areas)
            relevant.append(c)
            for m in c_machines:
                machine_hits[m]["commits"].add(c["short"]); machine_hits[m]["areas"].update(c_areas)
                machine_hits[m]["tickets"].update(keys)

    # BT1 tickets that touch other teams' machines (direct) or shared code (indirect)
    alerts = defaultdict(lambda: {"commits": set(), "direct": defaultdict(set), "shared": defaultdict(set),
                                  "own": set(), "subjects": [], "dates": []})
    for c in commits:
        bt1 = [k for k in c["tickets"] if k.startswith(ALERT_PREFIX + "-")]
        if not bt1:
            continue
        for f in c["files"]:
            if re.search(r"^(docs/|\.github/|vacam/Tests/|twincat/test/|twincat/UnitTest|twincat/BDD|twincat/TestDriver|twincat/src/UnitTest)", f):
                continue
            other = next((n for rx, n in OTHER_MACHINES if rx.search(f)), None)
            ms, area = classify(f)
            for k in bt1:
                T = alerts[k]
                T["commits"].add(c["short"])
                if c["subject"] not in T["subjects"]:
                    T["subjects"].append(c["subject"]); T["dates"].append(c["date"][:10])
                if other:
                    T["direct"][other].add(f)
                elif set(ms) == set(ALL) and area != "Translations / UI text":
                    T["shared"][area].add(f)
                if ms and set(ms) != set(ALL):
                    T["own"].update(ms)
    bt1_alerts = []
    for k, T in alerts.items():
        if not T["direct"] and not T["shared"]:
            continue
        lines = lambda files: sum(churn.get(f, 0) for f in files)
        bt1_alerts.append({
            "ticket": k, "commits": len(T["commits"]), "last_date": max(T["dates"]),
            "subjects": T["subjects"][:8],
            "direct": {n: {"files": len(fs), "churn": lines(fs), "top": sorted(fs, key=lambda f: -churn.get(f, 0))[:5]}
                       for n, fs in sorted(T["direct"].items())},
            "shared": {a: {"files": len(fs), "churn": lines(fs), "top": sorted(fs, key=lambda f: -churn.get(f, 0))[:5]}
                       for a, fs in sorted(T["shared"].items())},
            "own_machines": sorted(T["own"]),
            "level": "Direct" if T["direct"] else "Shared code",
        })
    bt1_alerts.sort(key=lambda x: (x["level"] != "Direct", -sum(v["churn"] for v in list(x["direct"].values()) + list(x["shared"].values()))))

    def score(name, A):
        impact = 3 if name in HIGH_IMPACT else 2
        if len(A["machines"]) <= 1:
            impact -= 1 if impact > 1 else 0
        n = len(A["commits"])
        likelihood = 3 if (n >= 15 or A["churn"] >= 1500) else 2 if (n >= 4 or A["churn"] >= 300) else 1
        s = impact * likelihood
        return s, ("High" if s >= 6 else "Medium" if s >= 3 else "Low")

    out_areas = []
    for name, A in areas.items():
        s, lvl = score(name, A)
        out_areas.append({"area": name, "risk_score": s, "risk": lvl, "commits": len(A["commits"]),
                          "files": len(A["files"]), "churn": A["churn"], "machines": sorted(A["machines"]),
                          "tickets": sorted(A["tickets"]), "top_files": sorted(A["files"], key=lambda f: -churn.get(f, 0))[:10]})
    out_areas.sort(key=lambda x: (-x["risk_score"], -x["commits"]))

    result = {
        "total_commits": len(commits),
        "relevant_commits": len(relevant),
        "areas": out_areas,
        "machines": {m: {"commits": len(v["commits"]), "areas": sorted(v["areas"]), "tickets": sorted(v["tickets"])}
                     for m, v in sorted(machine_hits.items())},
        "tickets": sorted({k for c in relevant for k in c["tickets"]}),
        "bt1_alerts": bt1_alerts,
        "relevant": [{k: c[k] for k in ("short", "date", "author", "subject", "tickets", "machines", "areas")} | {"files": c["files"][:15]}
                     for c in relevant],
    }
    json.dump(result, open(out_path, "w", encoding="utf-8"), indent=1)
    print(f"commits={len(commits)} relevant={len(relevant)} tickets={len(result['tickets'])}")
    for a in out_areas:
        print(f"{a['risk']:6} {a['risk_score']}  {a['area']:35} commits={a['commits']:4} churn={a['churn']:6} {','.join(a['machines'])}")
    for m, v in result["machines"].items():
        print(f"{m:28} commits={v['commits']} tickets={len(v['tickets'])}")
    print(f"BT1 alerts: {len(bt1_alerts)} tickets")
    for t in bt1_alerts:
        print(f"  {t['level']:11} {t['ticket']:9} commits={t['commits']:3} direct={','.join(t['direct'])} shared={','.join(t['shared'])}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
