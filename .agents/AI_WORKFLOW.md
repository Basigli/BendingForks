# Flusso di Lavoro e Ruoli Agenti: Moduli AI & Ricerca (Member 3)

Questo documento definisce il flusso di lavoro locale e i ruoli degli agenti per la redazione, revisione e pubblicazione dei deliverables di Project Management relativi allo stream "Moduli AI & Ricerca" del progetto BendingForks.

## 1. Il Team di Agenti

### pm_architect_ai
*   **Ruolo**: Autore materiale dei documenti (WBS, RBS, Rischi) per il dominio AI.
*   **Responsabilità**:
    *   Stilare le bozze iniziali calate nel contesto di BendingForks.
    *   Fornire e redigere il paragrafo "**Giustificazione.**" alla fine di ogni documento basandosi sulla logica e sulla teoria del PM.
    *   Leggere le revisioni del `professor` e aggiornare la bozza per risolvere ogni dubbio accademico e metodologico.
*   **Strumenti**: Ha accesso a NotebookLM per consultare la teoria e ai file locali in lettura/scrittura.

### professor
*   **Ruolo**: Revisore Accademico (Agente preesistente).
*   **Responsabilità**:
    *   Leggere le bozze locali prodotte dal PM Architect o i documenti su Notion.
    *   Interrogare NotebookLM per confrontare il lavoro con la teoria del Prof. Boschetti.
    *   Fornire feedback rigoroso evidenziando punti di forza, criticità metodologiche e validità della giustificazione. Se il documento è su Notion, lasciare commenti diretti tramite l'API; se è in locale, produrre un file (es. `.reviews/NomeDoc_Review.md`).
*   **Regole**: Non modifica mai i file di bozza originali.

### humanizer_editor
*   **Ruolo**: Correttore di bozze e QA testuale.
*   **Responsabilità**:
    *   Prendere la bozza approvata accademicamente e pulirla stilisticamente.
    *   Applicare le regole del plugin `Humanizer` per rimuovere i pattern linguistici tipici dell'IA.
    *   Assicurarsi che le tabelle siano in puro Markdown (senza tag HTML) per non rompere il renderer di Notion.
    *   Salvare la versione definitiva pronta per il deploy.

### notion_sync
*   **Ruolo**: Responsabile del Deploy su Notion.
*   **Responsabilità**:
    *   Prendere i file definitivi e caricarli su Notion usando la CLI `ntn`.
    *   Eseguire sempre `source .env` prima di ogni comando.
    *   Applicare modifiche mirate ai blocchi Notion per evitare sovrascritture accidentali del lavoro altrui.

---

## 2. Il Flusso di Lavoro (Pipeline Locale -> Notion)

1.  **Drafting (`pm_architect_ai`)**: 
    L'utente chiede al PM Architect di generare un documento (es. WBS). Il PM Architect lo scrive, include la Giustificazione, e lo salva in `drafts/NomeDoc.md`.
2.  **Review (`professor`)**: 
    L'utente chiede al Professore di recensire `drafts/NomeDoc.md` o una pagina Notion. Il Professore genera `.reviews/NomeDoc_Review.md` per le bozze locali o lascia commenti diretti su Notion.
3.  **Iteration (`pm_architect_ai`)**: 
    L'utente chiede al PM Architect di leggere la review e sistemare il documento originale, rispondendo ai dubbi del Professore. *(Questo step si ripete finché la qualità metodologica non è perfetta).*
4.  **Polishing (`humanizer_editor`)**: 
    La bozza perfetta viene passata all'Editor, che raffina il testo, sistema la formattazione Markdown e salva in `final/NomeDoc.md`.
5.  **Deploy (`notion_sync`)**: 
    Il file finale viene passato al Notion Sync, che lo carica in sicurezza nel workspace tramite `ntn`.
