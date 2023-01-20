import os
import openai
from dotenv import load_dotenv

load_dotenv()

MODEL = "text-davinci-003"
MAX_TOKENS = 3_000

prompts = [
    """
Create 5 unique multiple choice questions about the content below, each with 5 distinct and unique options, only one of which is correct, with the answer below the options.
An Availability Zone consists of one or more data centers, each with redundant power, networking, and connectivity. The data centers of a single Availability Zone, or “AZ” for short, are typically within 100 kilometers or 60 miles of each other. Think of it as a cluster of interconnected data centers in a specific geographic zone, that can help your applications become highly available – hence the name, Availability Zone. An AWS Region consists of multiple Availability Zones. AWS has various regions available in North America, South America, Europe, Asia, and other parts of the globe. Since a single availability zone consists of multiple data centers, your system can achieve a higher level of fault-tolerance by running it in two or more availability zones. This enables companies to build highly available, fault-tolerant, and scalable cloud architecture instead of running their applications on a single datacenter. Remember that a single availability zone consists of one or more data centers. Since you can deploy your application or your database to multiple availability zones in a single region, your systems will still be running even if three or more data centers experienced an outage simultaneously. To improve the durability of your data, you can also replicate it to two or more regions. This is helpful for disaster recovery and backups. The Availability Zones of a single AWS Region are typically within hundreds of kilometers or miles of each other. However, these availability zones are still within a specific country to comply with the data sovereignty requirement. This is particularly useful if you have sensitive data that must only be stored in a certain location or country for data privacy compliance.
""",
]

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("aws_cheatsheets.txt", "a") as f:
    for prompt in prompts:
        try:
            result = openai.Completion.create(
                model=MODEL,
                prompt=prompt,
                temperature=0.5,
                max_tokens=MAX_TOKENS,
                frequency_penalty=0,
                presence_penalty=0,
            )

            if result and result.get("choices"):
                answer = result.get("choices").pop()
                text = answer.get("text")
                f.write(f"{text} \n")
        except Exception as e:
            print("=============================")
            print(e)
            print(prompt)
            print("=============================")
