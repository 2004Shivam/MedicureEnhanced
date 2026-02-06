---
description: MedicureEnhanced Development Rules & Guidelines
---

# MedicureEnhanced Development Rules

## 🛡️ DEFENSIVE CODING PRINCIPLES

1.  **NEVER delete or completely rewrite files** - make small, incremental changes.
2.  **ALWAYS preserve existing functionality** - particularly the ML model loading logic and Razorpay integrations.
3.  **Add helpful comments** for complex logic, especially in `diet_exercise` services and `disease_prediction` views.
4.  **Before making big changes**, create an implementation plan and wait for approval.

## 🔒 PROTECTED FILES (Ask Before Modifying)

These files require explicit approval before any changes:
-   `medicure/settings.py` (Core Config)
-   `medicure/urls.py` (Root Routing)
-   `requirements.txt` (Dependencies)
-   Any `.pkl` files in `*/models/` (ML Artifacts)

## 📁 PROJECT STRUCTURE

-   **`medicure/`**: Project Configuration
-   **`users/`**: Custom Auth (Patient/Doctor roles) & Verification
-   **`doctors/`**: Doctor profiles & approvals
-   **`apps/appointments/`**: Booking logic
-   **`subscriptions/`**: Razorpay payments & Plan logic
-   **`disease_prediction/`**: General Disease ML (Symptom-based)
-   **`health_prediction/`**: Specialized ML (PCOS, Mental Health, Obesity)
-   **`diet_exercise/`**: Personalized plan generation (Spoonacular/ExerciseDB)

## 🌿 GIT BRANCHES

-   **Main Branch**: `main`
-   **Feature Branches**: Use `feat/<feature-name>` or `fix/<issue>`

## 🤖 AI MODEL

-   Use **gemini-2.5-flash** (NOT gemini-1.5-flash) for all coding tasks.

## 📝 COMMIT WORKFLOW

When user says "checkpoint" or "commit":

1.  **Check Status**: Run `git status` to view changes.
2.  **Verify**: Ensure no secrets (API Keys) are being committed. (Check `.env` usage).
3.  **Stage**: `git add <specific_files>` (Avoid `git add .` unless sure).
4.  **Commit**: Use Conventional Commits format:
    -   `feat: add new pcos prediction logic`
    -   `fix: resolve razorpay callback error`
    -   `refactor: move views out of models.py`
    -   `docs: update project audit`
5.  **Push**: `git push origin main`

### Best Practices
-   **Atomic Commits**: One feature/fix per commit.
-   **Descriptive Messages**: Explain *why* a change was made, not just *what*.
-   **Test First**: Run `python manage.py check` before committing core changes.
