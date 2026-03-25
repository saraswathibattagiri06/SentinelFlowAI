import os
from dotenv import load_dotenv
import gitlab


env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

token = os.getenv('GITLAB_TOKEN')
project_id = os.getenv('PROJECT_ID')

print(f"DEBUG: Token starts with: {token[:10]}...") 
print(f"DEBUG: Project ID is: {project_id}")

try:
    gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
    gl.auth() 
    print(f"✅ Authenticated as: {gl.user.username}")
    
    project = gl.projects.get(project_id)
    print(f"✅ Connected to Project: {project.name}")
except Exception as e:
    print(f"❌ Failed: {e}")