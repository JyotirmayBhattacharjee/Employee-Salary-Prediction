gr.Interface(
    fn=predict_salary,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Education Number"),
        gr.Dropdown(label_encoders['marital-status'].classes_.tolist(), label="Marital Status"),
        gr.Dropdown(label_encoders['occupation'].classes_.tolist(), label="Occupation"),
        gr.Dropdown(label_encoders['relationship'].classes_.tolist(), label="Relationship"),
        gr.Dropdown(label_encoders['race'].classes_.tolist(), label="Race"),
        gr.Dropdown(label_encoders['gender'].classes_.tolist(), label="Gender"),
        gr.Number(label="Capital Gain"),
        gr.Number(label="Capital Loss"),
        gr.Number(label="Hours per Week"),
        gr.Dropdown(label_encoders['workclass'].classes_.tolist(), label="Workclass"),
    ],
    outputs="text",
    title="Employee Salary Predictor",
).launch()
