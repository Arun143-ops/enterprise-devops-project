import os
import sys
import time

def main():
    # Fetch configurations from environment variables (Default to 'Development' if not set)
    environment = os.getenv("APP_ENV", "Development")
    data_limit = int(os.getenv("DATA_LIMIT", "50"))
    
    print(f"--- Starting Enterprise Data Pipeline [{environment} Mode] ---")
    
    try:
        print(f"Initializing connection to data stream... Target limit: {data_limit} records.")
        time.sleep(1)  # Simulate processing latency
        
        # Simulating data chunk processing
        for i in range(1, 6):
            processed_records = (data_limit // 5) * i
            print(f"[Processing] Chunk {i}/5 completed. Total processed: {processed_records} records.")
            time.sleep(0.5)
            
        print("--- Pipeline Executed Successfully. Container shutting down cleanly. ---")
        
    except Exception as e:
        print(f"[ERROR] Pipeline failed unexpectedly: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()