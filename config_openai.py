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


searchservice = values_env_openai['searchservice']
index = values_env_openai['index']
searchkey = values_env_openai['searchkey']
category=values_env_openai['category']

print(f"searchservice: {searchservice}")
print(f"index: {index}")
print(f"category: {category}")

AZ_ST_ACC_NAME = values_env_openai["AZ_ST_ACC_NAME"]
AZ_ST_ACC_KEY = values_env_openai["AZ_ST_ACC_KEY"]
AZ_ST_CONTAINER_NAME = values_env_openai["AZ_ST_CONTAINER_NAME"]