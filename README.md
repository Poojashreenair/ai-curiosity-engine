# 🚀 CS Curiosity Engine (AI Doubt Solver)

**Feed your brain. Decode the mystery. Level up your coding skills.**

The **CS Curiosity Engine** is an AI-powered educational tool designed specifically for Computer Science students. It bridges the gap between passive reading and active retention by instantly generating targeted explanations followed by interactive knowledge checks (quizzes). 

Built as a submission for the **Robokalam AI Developer Trainee** assignment.

## ✨ Features

* **Targeted CS Knowledge:** The AI is strictly prompt-engineered to only answer questions related to Computer Science, coding, and technology, rejecting off-topic prompts to maintain an educational focus.
* **Closed-Loop Learning:** Students read the explanation first, and then click to reveal a dynamically generated 3-question interactive quiz to test their retention.
* **Hacker UI/UX:** A modern, dark-mode interface built with Bootstrap and custom typography (`JetBrains Mono` and `Fredoka`) to make learning feel like an engaging coding mission.
* **Robust AI Architecture:** Utilizes the Google GenAI SDK with Pydantic to enforce **strict JSON schema outputs**. This ensures the Flask backend never crashes due to unstructured AI text generation.
* **Secure Setup:** Environment variables are strictly used to handle API credentials, ensuring no sensitive keys are hardcoded into the application.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI Engine:** Google Gemini API (`gemini-2.5-flash` via the modern `google-genai` SDK)
* **Data Validation:** Pydantic (for structured JSON LLM responses)
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API), Bootstrap 5 (CDN)

## 🚀 How to Run Locally

Follow these steps to get the Curiosity Engine running on your local machine.

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/cs-curiosity-engine.git](https://github.com/YOUR_GITHUB_USERNAME/cs-curiosity-engine.git)
cd cs-curiosity-engine
