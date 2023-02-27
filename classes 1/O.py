n = int(input())
m = int(input())
t = int(input())
hour = (t // 60 + n + (m + t % 60) // 60) % 24
minut = (m + t % 60) % 60
hour_str = str(hour)
minut_str = str(minut)
if hour < 10:
    hour_str = str(f"0{hour}")
if minut < 10:
    minut_str = str(f"0{minut}")
print(f"{hour_str}:{minut_str}")