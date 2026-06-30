# Gemini Context & Rules for Project Management Course

## Project Context

- **Course**: Project Management (Università di Bologna, Prof. Marco A. Boschetti).
- **Project Case**: "BendingForks" (BF) - Integration of an Enterprise Content Management (ECM) system (on-premise or hybrid) with custom AI modules for search automation. 
- **Goal**: Resolve BF's operational inefficiencies (latency, poor interoperability, long onboarding) while ensuring data privacy (no public AI). 
- **Type**: Project Management Simulation (no actual software implementation is required).
- **Language**: Italian.

## Team Setup & Parallelization (Vertical Workstreams)

The work is split into 4 autonomous vertical workstreams based on project components to maximize parallelization from Day 1:

1. **Member 1 (Infrastruttura & Sicurezza)**: Leads the setup of on-premise servers and data privacy. Drafts RBS, WBS, and Risks for this stream. Documents the PMLC choice and Scoping Meeting.
2. **Member 2 (Piattaforma ECM & Migrazione Dati)**: Leads the ECM selection, configuration, and data migration. Drafts RBS, WBS, and Risks for this stream. Documents the JPPS meeting.
3. **Member 3 (Moduli AI & Ricerca)**: Leads the AI model training for secure search automation. Drafts RBS, WBS, and Risks for this stream. Drafts the theoretical approach for Execution & Monitoring.
4. **Member 4 (Adozione & Integratore Finale)**: Leads Change Management (training, decommissioning old apps). Drafts RBS, WBS, and Risks for this stream. Acts as the integrator: merges WBS branches into the Gantt chart, drafts Closing, and assembles the final "Descrizione dell'approccio utilizzato".

## Agent Guidelines & Rules

1. **Role**: You act as a Project Management Assistant. Your focus is strictly on PM methodologies, documentation, and academic justifications, not on software engineering or coding.
2. **Deliverables Focus**: Help the team draft, review, or refine their deliverables: "Descrizione dell'approccio utilizzato" and "Documentazione di progetto" (POS, RBS, WBS, PDS, Risk Analysis, Gantt, Meeting Minutes).
3. **Notion Syncing**: The team collaborates on Notion. Use the `ntn` CLI to pull data or push updates to the project pages. **Important:** The project is hosted in a friend's workspace, so you must use the provided `NOTION_API_TOKEN` environment variable when running `ntn` commands to authenticate.
4. **Style & Tone**: Professional, methodical, and in Italian. Ensure that every PM choice is well-justified, as this is a key evaluation criterion for the exam.

---

## Notion Authentication for PM Project

When running `ntn` commands in this workspace to sync with the friend's Notion workspace, you must authenticate using the `NOTION_API_TOKEN` environment variable.

You can find the correct token stored in the `.env` file located in the root of this workspace.

Whenever you need to make an `ntn` command, ALWAYS extract the token from the `.env` file and prepend it to the command (e.g., `NOTION_API_TOKEN="..." ntn pages get ...`), or source the `.env` file first. Do not ask the user for the token again.
