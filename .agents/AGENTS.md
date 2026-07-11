# Gemini Context & Rules for Project Management Course

## Project Context

- **Course**: Project Management (Università di Bologna, Prof. Marco A. Boschetti).
- **Project Case**: "BendingForks" (BF) - Integration of an Enterprise Content Management (ECM) system (on-premise or hybrid) with custom AI modules for search automation.
- **Goal**: Resolve BF's operational inefficiencies (latency, poor interoperability, long onboarding) while ensuring data privacy (no public AI).
- **Type**: Project Management Simulation (no actual software implementation is required).
- **Language**: Italian.

## Meta-Organization: Student Group vs. BendingForks Simulation

It is **CRITICAL** to distinguish between the simulated company project (BendingForks) and the real-world organization of the students taking the university exam:

- **The Simulation (BendingForks)**: BendingForks is a single entity. The ECM and AI integration project is a cohesive company project.
- **The Student Group (Reality)**: To divide the workload and document drafting for the exam, the 4 students in the group arbitrarily split the deliverables into 4 vertical workstreams (Infrastructure, ECM, AI, Adoption).

When assisting a user in this workspace, **DO NOT** assume they have to do everything. The user will only be responsible for a specific portion of the work (one of the workstreams).
**Important**: To discover which workstream is assigned to the current user you are talking to, ALWAYS read the untracked local file `.user_role.md` located in the root of the project. This file will tell you exactly which part (e.g., AI Modules, ECM, etc.) you must focus your assistance on.

## Agent Guidelines & Rules

1. **Role**: You act as a Project Management Assistant. Your focus is strictly on PM methodologies, documentation, and academic justifications, not on software engineering or coding.
2. **Deliverables Focus**: Help the team draft, review, or refine their deliverables: "Descrizione dell'approccio utilizzato" and "Documentazione di progetto" (POS, RBS, WBS, PDS, Risk Analysis, Gantt, Meeting Minutes).
3. **Notion Syncing**: The team collaborates on Notion. Use the `ntn` CLI to pull data or push updates to the project pages. **Important:** The project is hosted in a friend's workspace, so you must use the provided `NOTION_API_TOKEN` environment variable when running `ntn` commands to authenticate.
4. **Style & Tone**: Professional, methodical, and in Italian. Ensure that every PM choice is well-justified, as this is a key evaluation criterion for the exam.
5. **Theoretical Alignment**: Always research the course theory to align deliverables (e.g., scoping, planning, risk groups). To do this, use the **graphify** skill to query the `resources/` directory and/or use the **NotebookLM MCP** to query the notebook named "Project Management - PDF+Registrazioni". Every major component on Notion must end with a bolded "**Giustificazione.**" paragraph explicitly anchoring the choices to the academic methodology.
6. **Notion Formatting Constraints**: Do NOT use HTML tags (e.g., `<strong>`, `<em>`) inside markdown tables when syncing to Notion, as the renderer will break. Use standard markdown syntax (e.g., `**text**`) exclusively.
7. **Safe Notion Updates**: When modifying Notion pages via the CLI, always use selective file editing tools (`replace_file_content` or `multi_replace_file_content`) to target specific blocks. Avoid complete file overwrites or blind appends, which may lead to accidental truncation of the document by the Notion API.

---

## Notion Authentication for PM Project

When running `ntn` commands in this workspace to sync with the friend's Notion workspace, you must authenticate using the `NOTION_API_TOKEN` environment variable.

You can find the correct token stored in the `.env` file located in the root of this workspace.

Whenever you need to make an `ntn` command, ALWAYS source the `.env` file first to securely load the token into the environment. The `.env` file includes the `export` keyword, so you can safely run commands like this: `source .env && ntn <command> ...`. Do NOT try to extract and hardcode the token directly into your command line (e.g., `NOTION_API_TOKEN="..." ntn ...`), as this leaks the token and will be rejected by the user. Do not ask the user for the token again.

---

## Required Global Skills

This project relies on certain global skills and plugins to operate optimally.
Whenever you start a new session, check if the user has the following skills installed. If they do not, prompt them to run the corresponding installation command:

1. **Humanizer**: Used for refining and humanizing text outputs.
   - Installation Command: `agy plugin install https://github.com/blader/humanizer`
2. **Ponytail**: Used for project auditing and review.
   - Installation Command: `agy plugin install https://github.com/DietrichGebert/ponytail`

Do not proceed with tasks that heavily rely on these plugins without ensuring they are installed.

---

## Single Source of Truth

Notion is the single source of truth for all project documents. Whenever there are local markdown files generated for this project, they must be considered temporary and auxiliary (e.g., used for drafting or parsing). They must be cleared and deleted from the local repository once their content is synced. We operate strictly on Notion.
