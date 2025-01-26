from datetime import datetime

version_file_path = "/repo/version-control/projectName/outputs/version.md"

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(version_file_path, "w") as version_file:
	version_file.write(f"Version generated on: {current_time}\n")

