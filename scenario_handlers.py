def handle_student_loan_save():
    return "Tips: Refinance, Income-driven plans, Budgeting apps."

def handle_spending_summary():
    return "Spending Summary: 40% essentials, 30% lifestyle, 30% savings."

def handle_savings_goal():
    return "Set SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound."

def handle_credit_score():
    return "Pay bills on time, reduce debt, don’t close old credit cards."

def handle_general_advice():
    return "Financial health starts with tracking expenses and setting budgets."

def handle_user_suggestion(user_input):
    from ai_utils import evaluate_suggestion
    evaluation = evaluate_suggestion(user_input)

    return f"""### 📊 Suggestion Evaluation
**🧠 Status:** {evaluation['status']}

**📌 Analysis:** {evaluation['analysis']}

**✅ Action Plan:** {evaluation['action_plan']}

**🚪 Escape Plan:** {evaluation['escape_plan']}
"""
