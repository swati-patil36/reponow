import os

def print_system_uptime():
    # For Unix/Linux systems
    if os.name == 'posix':
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = uptime_seconds // 3600
            uptime_minutes = (uptime_seconds % 3600) // 60
            print(f"System Uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")
    # For Windows systems
    elif os.name == 'nt':
        import subprocess
        result = subprocess.check_output('net stats srv', shell=True, encoding='utf-8')
        for line in result.split('\n'):
            if 'Statistics since' in line:
                print(f"System Uptime (since): {line.split('Statistics since')[1].strip()}")
                break
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    print_system_uptime()
