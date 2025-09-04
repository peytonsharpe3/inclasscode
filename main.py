import supabase
from supabase import create_client, Client  
import os 
import dotenv 
dotenv.load_dotenv()

# set these as environment variables or replace them with your own
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

#Example: select all rows from a table 
supabase: Client = create_client(url, key)

# Only fetch driver_name and avg_ speed columns
response = supabase. table("donors") \
    .select("full_name", "city") \
    .execute()

print(response.data)