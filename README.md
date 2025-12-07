<p align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg" 
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs" 
       width="100%">
</p>

<h2 align="center">DCQN-MATRIX — Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  <strong>Real-text verification • Zero hallucination • Reproducible LLM reasoning</strong>
</p>

<p align="center">
  <a href="https://osf.io/qwa6s"><img src="https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2FQWA6S-blue.svg"></a>
  <a href="https://doi.org/10.17605/OSF.IO/WZ6AR"><img src="https://img.shields.io/badge/Registration-10.17605%2FOSF.IO%2FWZ6AR-purple.svg"></a>
  <img src="https://img.shields.io/badge/Protocol-Deterministic-orange.svg">
  <img src="https://img.shields.io/badge/LLM-Evaluation-green.svg">
  <img src="https://img.shields.io/badge/State-Machine_Logic-black.svg">
</p>

---

# DCQN.MATRIX – LLM Axiomatic Protocol (OSF Reference)

This repository contains a **deterministic protocol** for large language models (LLMs)
designed to read, extract and activate the axiomatic system of:

> **“DCQN.MATRIX – Die Stimme der Neutralität”**  
> Author: Benjamin Hupe  
> **OSF Project DOI:** 10.17605/OSF.IO/QWA6S  
> **OSF Registration DOI:** 10.17605/OSF.IO/WZ6AR  
> **OSF URLs:**  
> – Project: https://osf.io/qwa6s  
> – Registration: https://osf.io/wz6ar  
> License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**

This repository does **not** mirror the full paper.  
Instead, it defines *exactly how* an LLM must:

1. Access the text (via OSF DOI or uploaded PDF),
2. Verify real-text access (no hallucinated PDFs),
3. Confirm full-text reading via machine status flags,
4. Reconstruct axioms and rules **only** from the document,
5. Activate the DCQN.MATRIX axiomatic system as the deterministic logic basis.

Goal: **Reproducibility. Determinism. Zero hallucination. DOI-anchored grounding.**

---

## Why does this repository exist?

Modern LLMs often:

- simulate DOI access instead of admitting offline status,  
- hallucinate PDF contents,  
- generate axioms that never appear in the text.

For a formal system like **DCQN.MATRIX**  
(deterministic neutrality quantification),  
such behaviour is unacceptable.

This protocol enforces:

- strict DOI/text access flags (`STATUS_STEP1`),  
- strict full-text reading flags (`STATUS_STEP2`),  
- forbidden simulation / hallucination fallback paths,  
- deterministic extraction of axioms and rules,  
- reproducible activation of the reasoning logic `DCQN_LOGIK_SESSION_V1`.

---

## Repository structure

- **`Protocol_DCQN_Matrix_Axiomatik_LLM.md`**  
  Main takeover protocol for LLMs.

- **`STATUS_DEFINITION.md`**  
  Machine-state flags (`STATUS_STEP1`, `STATUS_STEP2`).

- **`DCQN_LLM_Protocol.json`**  
  JSON protocol: for automation + evaluation harnesses.

- **`LICENSE.md`**  
  CC BY 4.0.

- **`README.md`**  
  You are here.

---

## How to use this protocol with an LLM

### **Step 1 — Provide access to the paper**

Download from OSF:

- Project page: https://osf.io/qwa6s  
- Registration: https://osf.io/wz6ar

Provide PDF to the model if it cannot access the DOI.

### **Step 2 — Execute the protocol**

Start a **fresh conversation** → paste the entire content of:
