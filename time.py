# Given values
characters = 95  # number of printable ASCII characters
password_length = 10  # length of the password
encryptions_per_second = 6.4 * 10**6  # encryptions per second

# Calculate the total number of possible passwords
total_passwords = characters ** password_length

# Calculate time in seconds to test all passwords
time_in_seconds = total_passwords // encryptions_per_second  # Use integer division for whole numbers

# Convert time from seconds to more readable format (days, hours, minutes)
time_in_days = time_in_seconds // (60 * 60 * 24)  # Whole number days
time_in_hours = time_in_seconds // (60 * 60)  # Whole number hours
time_in_minutes = time_in_seconds // 60  # Whole number minutes
# Convert time from days to years
time_in_years = time_in_days // 365  


# Print the results
print(f"Time to test all passwords:")
print(f"Time in years: {time_in_years}")
print(f"Time in days: {time_in_days}")
print(f"Time in hours: {time_in_hours}")
print(f"Time in minutes: {time_in_minutes}")
print(f"Time in seconds: {time_in_seconds}")

