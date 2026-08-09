# Project Athena

## Personalized PCOS Lifestyle Recommendation system using Memory-aware RAG

- A Conversational AI assistant for women with PCOS thet provides **personalized** lifestyle guidance (Eg. Diet, Exercise, sleep, stress, cycle-aware suggestions) using **Retrieval Augmented Generation**, user memory, ans optionally a PCOS risk/diagnosis module.

## Goals:

1. To provide a solution that offers personalized recommendations instead of just vague LLM responses.
2. Solve the current problem of Hallucination in LLMs.
3. A single checkpoint solution for PCOS diagnoised women.
4.

## Tech Stack:

| Service           | Technology                                |
| ----------------- | ----------------------------------------- |
| Frontend          | `Flutter`                                 |
| Backend           | `Fast API`                                |
| LLM Orchestration | `LangChain`                               |
| Embeddings        | `all-miniLM-L6-v2` or `BAAI/bge-small-en` |
| Vector DB         | `ChromaDB`                                |
| Short Term Memory | `Redis` (Coversational memory)            |
| Long Term Memory  | `PostgreSQL` (User Database)              |
| Autentication     | `Firebase Auth`                           |

## Modules:

1. _User Profile & Memory System_
2. _Knowledge base & RAG_
3. _Recommendation engine_
4. _Explainability & Source grounding_
5. _User Interface & Conversational interface_

- Wearable + Health data integration
- Symptoms + Cycle + Habit tracker

---

## Contact

Developed by **Raj Vardhan Singh**  
📧 Email: srajvardhan11@gmail.com
👥 LinkedIn: [rajvsingh11](https://linkedin.com/in/rajvsingh11)

---

> _"Empowering preventive healthcare through technology."_
