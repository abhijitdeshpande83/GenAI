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

## Docker Training Instructions

### Overview

This guide walks you through the process of training a Rasa model inside a Docker container. 

**Note:** Models trained on MacOS aren't compatible with Linux Docker containers, so it's crucial to train inside the Docker container to avoid compatibility issues later on.

### Prerequisites

Before you start, make sure you have the following:

- **Docker** installed and running on your machine.
- A **Rasa custom image** (named `rasa-custom-image` in this case) with Rasa installed.
- **Training data** located inside the `/app/data` directory inside the container.
- A local directory on your host machine to store the trained models.

### Train the Model in Docker

To train your Rasa model inside the Docker container, use the following command:

```bash
docker run --rm -v $(pwd)/models:/app/models rasa-custom-image train --data /app/data
```
After training, update the symlink so Rasa can find the latest model:
```bash
ln -sf <new_model_file>.tar.gz latest.tar.gz
```
Need of Symlink: Inside a Docker container, in this case when copy or mount models manually, the symlink may not get created. If the symlink isn’t there, Rasa looks for latest.tar.gz and fails with “No valid model found”. That’s why explicitly create or update it after training in the container to mimic the local behavior.

## Future Enhancements

- **Multi-Intent Handling:** Extend the chatbot to manage multiple intents in a single conversation (e.g., nearby attractions along with movie queries).  
- **Interactive Responses (Buttons):** Replace typed responses with button-based selections for better UX (currently available in enterprise Rasa version).


## Get the Code

Clone the repository to your local machine:

```bash
git clone https://github.com/abhijitdeshpande83/NLP.git
cd NLP/SupportIQ/rasa
```