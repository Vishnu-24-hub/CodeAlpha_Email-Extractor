import re

# Open and read the text file
file = open("input1.txt", "r")
data = file.read()
file.close()

# Pattern to find email addresses
pattern = r'\S+@\S+\.\S+'

# Extract emails
email_list = re.findall(pattern, data)

# Remove duplicate emails
unique_emails = list(set(email_list))

# Save emails into output file
output = open("emails.txt", "w")

for email in unique_emails:
    output.write(email + "\n")

output.close()

# Display results
print("Email extraction completed")
print("Total emails found:", len(unique_emails))

print("\nExtracted Emails:")
for email in unique_emails:
    print(email)