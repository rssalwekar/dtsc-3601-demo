from supabase import create_client, Client
import os
import dotenv

dotenv.load_dotenv()

# Replace with your Supabase project details
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# Example: fetch data from "movies" table
response = supabase.table("movies").select("*").execute()
print(response.data)
