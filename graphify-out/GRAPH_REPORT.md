# Graph Report - .  (2026-07-03)

## Corpus Check

- Corpus is ~36,436 words - fits in a single context window. You may not need a graph.

## Summary

- 139 nodes · 194 edges · 12 communities
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 5 edges (avg confidence: 0.79)
- Token cost: 0 input · 255,999 output

## Community Hubs (Navigation)

- [[_COMMUNITY_Scoping & Requirements Gathering|Scoping & Requirements Gathering]]
- [[_COMMUNITY_Launch, Monitoring & Team Roles|Launch, Monitoring & Team Roles]]
- [[_COMMUNITY_PM History & Brooks Principles|PM History & Brooks Principles]]
- [[_COMMUNITY_ProjectProgramPortfolio Definitions|Project/Program/Portfolio Definitions]]
- [[_COMMUNITY_PM Knowledge Areas & Processes|PM Knowledge Areas & Processes]]
- [[_COMMUNITY_Planning Estimation & Scheduling|Planning: Estimation & Scheduling]]
- [[_COMMUNITY_Kanban & Lean Methods|Kanban & Lean Methods]]
- [[_COMMUNITY_Markdown Conversion Tooling|Markdown Conversion Tooling]]
- [[_COMMUNITY_Critical Path & Escalation|Critical Path & Escalation]]
- [[_COMMUNITY_Closing Process Group|Closing Process Group]]
- [[_COMMUNITY_PMLC Models (TPMAPMxPMMPx)|PMLC Models (TPM/APM/xPM/MPx)]]
- [[_COMMUNITY_The Creeps (ScopeHopeEffortFeature)|The Creeps (Scope/Hope/Effort/Feature)]]

## God Nodes (most connected - your core abstractions)

1. `Scoping Process Group - Slide Deck (Ver. 5.1)` - 15 edges
2. `Definizione di Progetto - Slide Deck (Ver. 3.7)` - 10 edges
3. `Planning Process Group - Slide Deck (Ver. 4.8)` - 9 edges
4. `Requirements Breakdown Structure (RBS)` - 9 edges
5. `Introduzione al Project Management - Slide Deck (Ver. 4.8)` - 8 edges
6. `Launching/Executing Process Group - Slide Deck (Ver. 3.3)` - 8 edges
7. `PMBOK (Project Management Body of Knowledge)` - 8 edges
8. `Project Management Life Cycle (PMLC)` - 8 edges
9. `Kanban` - 8 edges
10. `Monitoring & Controlling Process Group - Slide Deck (Ver. 3.2)` - 7 edges

## Surprising Connections (you probably didn't know these)

- `convert()` --references--> `markitdown[pdf] dependency`  [EXTRACTED]
  resources/convert.py → requirements.txt
- `Scrum Story Points / Planning Poker` --conceptually_related_to--> `The Scrum Team (Product Owner, Scrum Master, Dev Team)`  [EXTRACTED]
  7-Planning Process Group - Ver.4.8.md → 2-Introduzione al PM - Ver.4.8.md
- `Scope Change Management Process` --conceptually_related_to--> `The Creeps`  [INFERRED]
  8-Launching Process Group - Ver.3.3.md → 3-Definizione di Progetto - Ver.3.7.md
- `Requirements Breakdown Structure (RBS)` --cites--> `IEEE Std 610.12`  [EXTRACTED]
  6-Scoping Process Group - Ver.5.1.md → 4-Definizione di Project Management - Ver.3.4.md
- `Procedure di Accettazione` --conceptually_related_to--> `Acceptance Criteria`  [INFERRED]
  10-Closing Process Group - Ver.3.2.md → 6-Scoping Process Group - Ver.5.1.md

## Import Cycles

- None detected.

## Hyperedges (group relationships)

- **PDS-to-Markdown conversion pipeline behind the course slide decks** — resources_convert_convert, resources_requirements_markitdown, resources_2_introduzione_al_pm_ver_4_8, resources_3_definizione_di_progetto_ver_3_7, resources_4_definizione_di_project_management_ver_3_4, resources_5_definizione_dei_processi_ver_4_5, resources_6_scoping_process_group_ver_5_1, resources_7_planning_process_group_ver_4_8, resources_8_launching_process_group_ver_3_3, resources_9_monitoring_and_controlling_process_group_ver_3_2, resources_10_closing_process_group_ver_3_2, resources_11_kanban_e_altro_ancora_ver_1_1 [INFERRED 0.75]
- **Five PMBOK/PMLC process groups spanning the course modules** — resources_5_definizione_dei_processi_ver_4_5_process_groups, resources_6_scoping_process_group_ver_5_1, resources_7_planning_process_group_ver_4_8, resources_8_launching_process_group_ver_3_3, resources_9_monitoring_and_controlling_process_group_ver_3_2, resources_10_closing_process_group_ver_3_2 [EXTRACTED 1.00]
- **Agile and Lean project management approaches contrasted across the course (Scrum, Kanban, Agile Manifesto, xPM)** — resources_2_introduzione_al_pm_ver_4_8_scrum_team_concept, resources_2_introduzione_al_pm_ver_4_8_agile_manifesto, resources_11_kanban_e_altro_ancora_ver_1_1_kanban, resources_11_kanban_e_altro_ancora_ver_1_1_kanban_vs_scrum, resources_4_definizione_di_project_management_ver_3_4_xpm [INFERRED 0.85]

## Communities (12 total, 0 thin omitted)

### Community 0 - "Scoping & Requirements Gathering"

Cohesion: 0.16
Nodes (20): Scoping Process Group - Slide Deck (Ver. 5.1), Acceptance Criteria, Business Process Management (BPM), Business Case, Business Model (Canvas), Business Process, Conditions of Satisfaction (CoS), Scegliere il PMLC Model (+12 more)

### Community 1 - "Launch, Monitoring & Team Roles"

Cohesion: 0.15
Nodes (18): Launching/Executing Process Group - Slide Deck (Ver. 3.3), Conflict Resolution Model, Six Phases of Decision-Making (Wysocki), Project Kick-Off Meeting, Kolb's Learning Styles, Project Meetings (Daily/Problem/Review), Project Team Composition, RASCI Responsibility Matrix (+10 more)

### Community 2 - "PM History & Brooks Principles"

Cohesion: 0.16
Nodes (15): Introduzione al Project Management - Slide Deck (Ver. 4.8), Manifesto for Agile Software Development, Brooks's Law (adding people to a late project makes it later), Conceptual Integrity, Execution over Idea, Fred Brooks, Il Mito del Garage (garage myth), Harlan Mills (+7 more)

### Community 3 - "Project/Program/Portfolio Definitions"

Cohesion: 0.20
Nodes (15): Definizione di Progetto - Slide Deck (Ver. 3.7), Business Value, PMBOK (Project Management Body of Knowledge), Definizione di Portfolio, PRINCE2, Definizione di Programma, Classificare i Progetti (Type A/B/C/D), PMBOK Definition of Project (+7 more)

### Community 4 - "PM Knowledge Areas & Processes"

Cohesion: 0.13
Nodes (15): BABOK Guide (IIBA), IEEE Std 610.12, Definizione di Requisito (IEEE/Wysocki), Definizione dei Processi - Slide Deck (Ver. 4.5), Closing Process Group (definition), Herzberg's Two-Factor Theory, Le 9+1 PM Knowledge Areas, Launching/Executing Process Group (definition) (+7 more)

### Community 5 - "Planning: Estimation & Scheduling"

Cohesion: 0.16
Nodes (15): Planning Process Group - Slide Deck (Ver. 4.8), Cash Flow Management, Fixed-Price vs Time-and-Materials Contracts, Stimare e Gestire i Costi, Delphi Technique, Joint Project Planning Session (JPPS), MoSCoW Prioritization, Project Definition Statement (PDS) (+7 more)

### Community 6 - "Kanban & Lean Methods"

Cohesion: 0.27
Nodes (10): Kanban e altro ancora... - Slide Deck (Ver. 1.1), DevOps, Kaizen, Kanban, Kanban Board, Kanban vs Scrum, Lead Time / Cycle Time KPIs, Taiichi Ohno (+2 more)

### Community 7 - "Markdown Conversion Tooling"

Cohesion: 0.33
Nodes (6): Path, convert(), main(), Convert input_path to Markdown via markitdown and write it to output_path., Parse CLI arguments and run the conversion, exiting with an error message on bad, markitdown[pdf] dependency

### Community 8 - "Critical Path & Escalation"

Cohesion: 0.29
Nodes (7): Problem Escalation Strategy, Critical Path & Slack/Float, Management Reserve, Project Network Diagram, Schedule Compression Techniques, Work Package, Problem Escalation Strategy (detailed hierarchy)

### Community 9 - "Closing Process Group"

Cohesion: 0.53
Nodes (6): Closing Process Group - Slide Deck (Ver. 3.2), Procedure di Accettazione, Final Project Report, Installation Approaches (Phased/BU/Cut-Over/Parallel), Post-Implementation Audit, Project Notebook

### Community 10 - "PMLC Models (TPM/APM/xPM/MPx)"

Cohesion: 0.53
Nodes (6): Agile Project Management (APM), Emertxe Project Management (MPx), Project Management Life Cycle (PMLC), The 5 PMLC Models (Linear/Incremental/Iterative/Adaptive/Extreme), Traditional Project Management (TPM), Extreme Project Management (xPM)

### Community 11 - "The Creeps (Scope/Hope/Effort/Feature)"

Cohesion: 0.60
Nodes (5): The Creeps, Effort Creep, Feature Creep, Hope Creep, Scope Creep

## Knowledge Gaps

- **39 isolated node(s):** `Path`, `markitdown[pdf] dependency`, `Harlan Mills`, `Twelve Principles of Agile Software`, `PM Definition (PMI)` (+34 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions

_Questions this graph is uniquely positioned to answer:_

- **Why does `PMBOK (Project Management Body of Knowledge)` connect `Project/Program/Portfolio Definitions` to `Scoping & Requirements Gathering`, `PM History & Brooks Principles`, `PM Knowledge Areas & Processes`, `Kanban & Lean Methods`?**
  _High betweenness centrality (0.354) - this node is a cross-community bridge._
- **Why does `The Scrum Team (Product Owner, Scrum Master, Dev Team)` connect `PM History & Brooks Principles` to `Project/Program/Portfolio Definitions`, `Planning: Estimation & Scheduling`, `Kanban & Lean Methods`?**
  _High betweenness centrality (0.213) - this node is a cross-community bridge._
- **Why does `Definizione di Progetto - Slide Deck (Ver. 3.7)` connect `Project/Program/Portfolio Definitions` to `The Creeps (Scope/Hope/Effort/Feature)`?**
  _High betweenness centrality (0.198) - this node is a cross-community bridge._
- **What connects `Path`, `Convert input_path to Markdown via markitdown and write it to output_path.`, `Parse CLI arguments and run the conversion, exiting with an error message on bad` to the rest of the system?**
  _44 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PM Knowledge Areas & Processes` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
