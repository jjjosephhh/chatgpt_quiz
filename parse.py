import os
import yaml
import json

with open("example.yml", "r") as stream:
    try:
        questions = yaml.safe_load(stream)
        content = []
        for question, answers in questions.items():
            answer = answers.pop()
            content.append(
                {
                    "question": question,
                    "options": answers,
                    "answer": answer,
                }
            )
        content = json.dumps(content, indent=4, ensure_ascii=False)
        with open(os.path.join("src", "questions", "questions.json"), "w") as f:
            f.write(content)
    except yaml.YAMLError as exc:
        print(exc)
