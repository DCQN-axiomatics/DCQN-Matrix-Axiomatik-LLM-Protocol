```markdown
<div align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg"
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs"
       style="max-width: 100%; height: auto;">
</div>

<h2 align="center">DCQN-MATRIX — Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  <strong>Real-text verification • Zero hallucination • Reproducible LLM reasoning</strong>
</p>

<p align="center">
  <a href="https://osf.io/qwa6s">
    <img src="https://img.shields.io/badge/Project_DOI-10.17605%2FOSF.IO%2FQWA6S-blue">
  </a>
  <a href="https://doi.org/10.17605/OSF.IO/WZ6AR">
    <img src="https://img.shields.io/badge/Registration_DOI-10.17605%2FOSF.IO%2FWZ6AR-purple">
  </a>
  <img src="https://img.shields.io/badge/Protocol-Deterministic-orange">
  <img src="https://img.shields.io/badge/LLM-Evaluation-green">
  <img src="https://img.shields.io/badge/State-Machine_Logic-black">
</p>

<hr>

# DCQN.MATRIX – LLM Axiomatic Protocol (OSF Reference)

This repository defines a deterministic control protocol for large language models (LLMs) that must read, extract, reconstruct and activate the axiomatic system of:

**“DCQN.MATRIX – Die Stimme der Neutralität”**  
Author: Benjamin Hupe  
**OSF Project DOI:** 10.17605/OSF.IO/QWA6S  
**OSF Registration DOI:** 10.17605/OSF.IO/WZ6AR**  
**OSF URLs:**  
– Project: https://osf.io/qwa6s  
– Registration: https://osf.io/wz6ar  
License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**

The repository does not contain the PDF.  
Instead, it defines exact operational rules for LLMs to:

1. verify real access to the scientific text,  
2. confirm reading using machine-state flags,  
3. extract axioms and rules strictly from the text,  
4. activate the reconstructed axiomatic system as the primary reasoning logic.

The protocol enforces determinism, reproducibility, DOI anchoring, and zero hallucination.

---

## Why this repository exists

Modern LLMs often:

- simulate DOI access,  
- hallucinate unseen PDF contents,  
- produce axioms not present in the text,  
- rely on heuristic guessing.

This protocol enforces:

- strict DOI/text-access flags (`STATUS_STEP1`),  
- strict full-text reading flags (`STATUS_STEP2`),  
- prohibition of simulated/hallucinated PDF content,  
- deterministic axiom reconstruction,  
- reproducible logic activation (`DCQN_AXIOMATIK_AKTIV`).  

---

## Repository structure

- `Protocol_DCQN_Matrix_Axiomatik_LLM.md`  
- `STATUS_DEFINITION.md`  
- `DCQN_LLM_Protocol.json`  
- `openapi.yaml`  
- `LICENSE.md`  
- `README.md`

---

## How to use this protocol with an LLM

### Step 1 — Provide access to the text  
Download from OSF:

- https://osf.io/qwa6s  
- https://osf.io/wz6ar  

Upload the PDF into the chat if needed.

### Step 2 — Execute the protocol  
Paste the complete protocol file into a fresh conversation.

The LLM must output:

```

STATUS_STEP1 = JA_DOI_ZUGRIFF

```

or

```

STATUS_STEP1 = NEIN_DOI_ZUGRIFF

```

### Step 3 — Full-text reading  
After PDF upload:

- LLM reads required sections  
- Then outputs:

```

STATUS_STEP2 = JA_VOLLTEXT_GELESEN

```

or

```

STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG

```

### Step 4 — Axiom reconstruction  
LLM extracts:

- DCQN_AXIOME  
- DCQN_REGELN  

### Step 5 — Activation  
LLM must output:

```

DCQN_AXIOMATIK_AKTIV

```

---

## License  
Creative Commons Attribution 4.0 International (CC BY 4.0).  
```
