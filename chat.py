from openai import OpenAI, base_url

client = OpenAI(api_key="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",
                base_url = "https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model = "deepseek/deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "2+2 just answer no explanation"
        }
    ]
)

print(chat.choices[0].message.content)    #only response is printed




# ChatCompletion(id='gen-1747231169-biENQLzG7yDvxjHTvwvi', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='NASA stands for **National Aeronautics and Space Administration**. It is the United States government agency responsible for the nation\'s civilian space program, as well as aeronautics and aerospace research. Established in 1958 under the National Aeronautics and Space Act, NASA conducts missions in space exploration, scientific discovery (e.g., planetary probes, telescopes), Earth science, and technological innovation (e.g., the Apollo Moon landings, International Space Station, and Mars rovers). The inclusion of "Aeronautics" reflects its role in advancing flight technology alongside space endeavors.', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning='Okay, so I need to figure out what NASA stands for. Let me start by recalling any prior knowledge I have. I know NASA is a space agency, right? They do stuff related to space exploration, like sending astronauts to the moon, launching satellites, and maybe the Mars rovers? But what does the acronym NASA actually stand for?\n\nHmm, I think the \'N\' might stand for National. Then maybe the \'A\' is Aeronautics? Because I\'ve heard the term "aeronautics" related to aircraft and flight. So National Aeronautics... Then the \'S\' could be Space, and the last \'A\' Administration? So putting it together: National Aeronautics and Space Administration. That sounds familiar. Wait, is that correct?\n\nLet me check if there\'s any other possibility. Sometimes acronyms can be tricky. For example, sometimes people confuse NASA with other agencies like ESA (European Space Agency) or Roscosmos. But NASA is definitely American. So National Aeronautics and Space Administration. Yeah, I think that\'s right. Aeronautics refers to the science of flight, and space administration covers their space exploration missions. \n\nI should also consider when NASA was established. I think it was created in 1958, maybe in response to the Soviet Union\'s Sputnik launch. The National Aeronautics and Space Act of 1958 probably established it. So the name would have been part of that legislation. \n\nWait, could the \'A\' in the middle stand for something else? Like Aerospace? But no, I think it\'s Aeronautics. Because the full name is commonly referred to as the National Aeronautics and Space Administration. Also, their website is nasa.gov, and their official documents probably use that full name. \n\nAnother way to verify: if I think about other similar agencies, like the Federal Aviation Administration (FAA), which deals with aeronautics as well. So NASA\'s inclusion of Aeronautics makes sense because they might have started with aeronautics research before moving into space. \n\nSo putting it all together, the acronym NASA stands for National Aeronautics and Space Administration. It\'s the United States government agency responsible for the nation\'s civilian space program and for aeronautics and aerospace research. They handle everything from launching satellites, human spaceflight missions, robotic explorations, and scientific research about Earth and space. \n\nI think that\'s it. Let me just make sure there\'s no common misconception. Sometimes people might misspell it as "National Aeronautical" but the correct term is "Aeronautics". So the answer should be National Aeronautics and Space Administration.\n'), native_finish_reason='stop')], created=1747231170, model='deepseek/deepseek-r1:free', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=648, prompt_tokens=13, total_tokens=661, completion_tokens_details=None, prompt_tokens_details=None), provider='Chutes')
#
# Process finished with exit code 0



