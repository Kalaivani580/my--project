from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_roadmap(goal):
    # For simplicity, static 5-step roadmap - you can improve with AI later
    steps = [
        f"Define your goal clearly: {goal}",
        "Research and gather resources",
        "Create a detailed plan with deadlines",
        "Start working on each task step-by-step",
        "Review progress and adjust plan as needed"
    ]
    return steps

@app.route('/roadmap', methods=['POST'])
def roadmap():
    data = request.json
    goal = data.get('goal')
    if not goal:
        return jsonify({"error": "Goal is required"}), 400

    steps = generate_roadmap(goal)
    return jsonify({"goal": goal, "steps": steps})

if __name__ == '__main__':
    app.run(debug=True)
