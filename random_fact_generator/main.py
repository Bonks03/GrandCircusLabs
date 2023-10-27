from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel

with open('facts.txt', 'r') as file:
    facts = [line.strip() for line in file]

app = FastAPI()

class Fact(BaseModel):
    fact: str

# Endpoint is /facts/random or /facts/(number between 0-3091)

@app.get("/facts/{choice}")
async def read_item(choice: str):
    try:
        if choice.lower() == "random":
            rand_num = np.random.randint(0, len(facts))
            return {f"Random Fact #{rand_num}": facts[rand_num]}
        
        elif choice.isdigit() and (int(choice) <= len(facts)):
            choice = int(choice)
            return {f"Fact #{choice}": facts[choice]}

        else:
            return {"error": "invalid choice"}

    except ValueError:
        return {"error": "invalid choice"}

@app.post("/add/")
async def add_fact(fact: Fact):
    new_fact = fact.fact
    with open('facts.txt', 'a') as file:
        file.write(new_fact + "\n")
    return {"message": f"Fact added successfully. (#{len(facts)})"}