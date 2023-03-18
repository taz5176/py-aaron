import random
import time
import pandas as pd

# Main sequence function
def check_device_status():
    # Simulate device status
    status = random.choice(["Normal", "No Disk", "No Disk", "No Disk"])
    # time.sleep(1)  # Simulate processing time
    return status

# Main program
num_loops = 20
retry_limit = 3

loop_count = 0
retry_count = 0
status_counts = {"Normal": 0, "Abnormal": 0, "No Disk": 0}
loop_results = []


print(f"\n>>> Beginning Check Device Status")
status = "Normal"
while ((loop_count < num_loops) and (status != "Abnormal")):
    print(status)
    retry_count = 0 # make sure the retry_count always starts from 0
    loop_count += 1
    status = check_device_status()
    loop_result = {"Loop": loop_count, "Status": status}
    loop_results.append(loop_result)
    print(f">>> Loop {loop_count}: {status}")
    
    if status == "Normal":
        #print(">>> Pass")
        loop_result["Result"] = "Pass"
        status_counts["Normal"] += 1

    elif status == "No Disk":
        print(">>>> No Disk Found, Beginning Retry")
        status_counts ["No Disk"] += 1
        #while retry_count < retry_limit:
        while retry_count < retry_limit:
            status = check_device_status()
            if status == "Normal":
                print(f">>>> Retry Count: {retry_count} --- Normal")
                loop_result["Result"] = "Retry Pass"
                #print(status)
                break
            elif status == "Abnormal":
                print(f">>>> Retry Count: {retry_count} --- Abnormal")
                loop_result["Result"] = "Retry Fail"
                #print(status)
                break
            elif status == "No Disk":
                print(f">>>> Retry Count: {retry_count} --- No Disk")
                loop_result["Result"] = "Retry Fail"
                #print(status)
            retry_count += 1    # make sure retry_count increments during the retry loop

    elif status == "Abnormal":
        print(">>> Fail")
        loop_result["Result"] = "Fail"
        status_counts ["Abnormal"] += 1
        break

    else:
        print(">>> Fail")
        
            
print()  # Print newline for readability
    
# Print final status counts
print("Status counts:")
for status, count in status_counts.items():
    print(f"{status}: {count}")

# Create summary table
summary_table = pd.DataFrame(loop_results)
summary_table = summary_table[["Loop", "Status", "Result"]]
print("\nSummary table:")
print(summary_table.to_string(index=False))