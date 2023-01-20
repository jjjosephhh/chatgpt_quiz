import os
import openai
from dotenv import load_dotenv

load_dotenv()

MODEL = "text-davinci-003"
MAX_TOKENS = 3_050

prompts = [
"""
Create 4 unique multiple choice questions about the following content, each with 5 distinct and unique options, only one of which is correct, with the answer below the options.
There are three fundamental drivers of cost with AWS:
Compute
Storage
Outbound data transfer.
AWS offers pay-as-you-go for pricing.
For certain services like Amazon EC2, Amazon EMR, and Amazon RDS, you can invest in reserved capacity. With Reserved Instances, you can save up to 75% over equivalent on-demand capacity. When you buy Reserved Instances, the larger the upfront payment, the greater the discount.
With the All Upfront option, you pay for the entire Reserved Instance term with one upfront payment. This option provides you with the largest discount compared to On-Demand instance pricing.
With the Partial Upfront option, you make a low upfront payment and are then charged a discounted hourly rate for the instance for the duration of the Reserved Instance term.
The No Upfront option does not require any upfront payment and provides a discounted hourly rate for the duration of the term.
There are also volume-based discounts for services such as Amazon S3.
For new accounts, AWS Free Tier is available.
Free Tier offers limited usage of AWS products at no charge for 12 months since the account was created.
You can estimate your monthly AWS bill using AWS Pricing Calculator.
""",
]

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("example.yml", "a") as f:
    for prompt in prompts:
        try:
            result = openai.Completion.create(
                model=MODEL,
                prompt=prompt,
                temperature=0.2,
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
