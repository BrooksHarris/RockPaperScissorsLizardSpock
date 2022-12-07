import os
import openai

names = ["rock","paper","scissors","lizard","spock"]
b = ["rock","scissors","paper","spock","paper","spock","lizard","lizard","rock","scissors"]
w = ["scissors","paper","rock","rock","spock","scissors","spock","paper","lizard","lizard"]
import os
import openai

openai.api_key = input("Paste OpenAI key: ") #os.getenv("OPENAI_API_KEY")

NUMBER_OF_ELEMENTS = 10

for i in range(NUMBER_OF_ELEMENTS):
    #, and generate a list of {} uses
    prompt = """Write a new type of element for the game {}.
        """.format(", ".join(names)
        #,str(len(names))
        )
    prompt_append = ""
    for j in names:
        prompt_append = prompt_append + "\nElement: " + j + "\nUses: "
        for k in range(len(b)):
            if b[k] == j:
                prompt_append = prompt_append + "Wins against " + w[k] + ", "
            if w[k] == j:
                prompt_append = prompt_append + "Loses to " + b[k] + ", "
    prompt = prompt + prompt_append
    print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response["choices"][0]["text"]
    print(result)
    names.append(result[int(result.find("Element: ")) + 9:int(result.find("\nUses: "))].lower())
    find_within = result[result.find("Uses: ") + 6:]
    for element in find_within.split(", "):
        element = element.replace(".","").replace(",","").replace(";","").replace("/","").replace("\\","")
        if element.find("Wins against ") != -1:
            b.append(names[-1])
            w.append(element[element.find("Wins against ")+13:])
        if element.find("Loses to ") != -1:
            w.append(names[-1])
            b.append(element[element.find("Loses to ")+9:])
    #print(names)
    #print(b)
    #print(w)