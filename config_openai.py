from dotenv import load_dotenv,dotenv_values


load_dotenv(".env2",override=True)

# deployment_id with a model without a private end point 
#values_env_openai = dotenv_values(".env2")

# deployment_id with a model with a private end point
values_env_openai = dotenv_values(".env2")

key = values_env_openai['KEY']
location = values_env_openai['LOCATION']
endpoint = values_env_openai['ENDPOINT']
deployment_id=values_env_openai['DEPLOYMENT_ID']  

print(f"location: {location}")
print(f"endpoint: {endpoint}")
print(f"deployment_id: {deployment_id}")