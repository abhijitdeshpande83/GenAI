# Rasa for Dialogue Management and Slot Filling

## Tech Stack

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=000000) 
![Rasa](https://img.shields.io/badge/Rasa-FF3B30?style=for-the-badge&logo=rasa&logoColor=ffffff) 
![Docker](https://img.shields.io/badge/Docker-0AFFFF?style=for-the-badge&logo=docker&logoColor=0A0A0A) 
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=ffffff) 
![Gracenote API](https://img.shields.io/badge/Gracenote_API-8A2BE2?style=for-the-badge&logoColor=ffffff)

---

## Project Overview

**Objective:** Enable structured, multi-turn conversations to collect user inputs and support transactional workflows like movie bookings, seat selection, and email confirmations.

**Why Rasa:** While LLMs are great for free-form conversation, Rasa allows deterministic dialogue management and precise control over conversation state, which is essential for production-ready workflows like bookings and confirmations.

---

## Implementation

- Developed a **movie booking chatbot** handling multi-turn dialogues:  
  - Collects user details: ZIP code, movie name, show date/time, and seat selection.  
  - Manages **slot filling** and **form validation** to ensure all required information is captured before booking.  
  - Integrates with **Gracenote API** to fetch real-time movie listings, theaters, and showtimes.  
  - Sends booking confirmation emails via Python’s `smtplib` using HTML templates.  
- Focused on a **single-domain approach** (movie booking) for reliability and production-readiness.  
- Leveraged Rasa’s dialogue management to implement workflows that require strict input validation and business rules enforcement.

---

## Architecture & Workflow

![Sequence Diagram](ui_assets/sequence-diagram.png) 
*This sequence diagram illustrates the multi-turn dialogue flow, slot filling, form validation, and backend interactions for movie booking. It highlights how the chatbot enforces business rules, validates user input, and triggers email confirmations.*

---

## Key Features / Outcomes

- Search movies by ZIP code and find nearby theaters.  
- View show dates and times for selected movies and theaters.  
- **Seat selection rules:**  
  - Only one seat per theater, show date, and showtime.  
  - Only today or future dates are selectable; past or ongoing shows are disallowed.  
- Automatic booking confirmation emails with full details.  
- Demonstrates a **robust, production-ready conversational workflow** with validated inputs and enforced business rules.

---

## Future Enhancements

- **Multi-Intent Handling:** Extend the chatbot to manage multiple intents in a single conversation (e.g., nearby attractions along with movie queries).  
- **Interactive Responses (Buttons):** Replace typed responses with button-based selections for better UX (currently available in enterprise Rasa version).


## Get the Code

Clone the repository to your local machine:

```bash
git clone https://github.com/abhijitdeshpande83/NLP.git
cd NLP/SupportIQ/rasa
```
